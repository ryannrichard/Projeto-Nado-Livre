from sqlalchemy import select

from modelos.atendente import Atendente
from modelos.nadador import Nadador
from modelos.toalha import Toalha
from modelos.utilizacao import Utilizacao
from excecoes.NadoLivreError import NadoLivreError
from persistencia.sessao import obter_sessao


class UtilizacaoService:
    """
    Serviço responsável por coordenar empréstimos e devoluções de toalhas,
    garantindo a aplicação das regras de negócio.
    """

    def registrar_retirada(
        self,
        toalha_id: int,
        nadador_id: int,
        atendente_id: int
    ) -> Utilizacao:
        """Registra a retirada de uma toalha validando as regras de negócio."""
        toalha_id = int(toalha_id)
        nadador_id = int(nadador_id)
        atendente_id = int(atendente_id)

        with obter_sessao() as sessao:
            toalha = sessao.get(Toalha, toalha_id)
            if toalha is None:
                raise NadoLivreError(
                    f"Toalha com ID {toalha_id} não encontrada."
                )

            nadador = sessao.get(Nadador, nadador_id)
            if nadador is None:
                raise NadoLivreError(
                    f"Nadador com ID {nadador_id} não encontrado."
                )

            if nadador.bloqueio:
                raise NadoLivreError(
                    f"Nadador '{nadador.nome}' (ID {nadador_id}) está "
                    f"bloqueado e não pode retirar toalhas."
                )

            utilizacao_aberta = sessao.scalars(
                select(Utilizacao).where(
                    Utilizacao.nadador_id == nadador_id,
                    Utilizacao.aberta.is_(True),
                )
            ).first()
            if utilizacao_aberta is not None:
                raise NadoLivreError(
                    "Não é possível realizar a retirada.\n"
                    "O nadador já possui uma toalha retirada."
                )

            atendente = sessao.get(Atendente, atendente_id)
            if atendente is None:
                raise NadoLivreError(
                    f"Atendente com ID {atendente_id} não encontrado."
                )

            if toalha.em_uso:
                raise NadoLivreError(
                    f"A toalha ID {toalha_id} já está em uso."
                )

            toalha.utilizar()
            nova_utilizacao = Utilizacao(nadador, toalha, atendente)
            sessao.add(nova_utilizacao)
            sessao.commit()
            return nova_utilizacao

    def registrar_devolucao(
        self,
        toalha_id: int,
        atendente_id: int
    ) -> Utilizacao:
        """Registra a devolução de uma toalha que está em uso."""
        toalha_id = int(toalha_id)
        atendente_id = int(atendente_id)

        with obter_sessao() as sessao:
            utilizacao = sessao.scalars(
                select(Utilizacao).where(
                    Utilizacao.toalha_id == toalha_id,
                    Utilizacao.aberta.is_(True),
                )
            ).first()
            if utilizacao is None:
                raise NadoLivreError(
                    f"Não há empréstimo em aberto para a toalha ID {toalha_id}."
                )

            atendente = sessao.get(Atendente, atendente_id)
            if atendente is None:
                raise NadoLivreError(
                    f"Atendente com ID {atendente_id} não encontrado."
                )

            utilizacao.encerrar(atendente)
            sessao.commit()
            return utilizacao