from sqlalchemy import select

from modelos.toalha import Toalha
from excecoes.NadoLivreError import NadoLivreError
from persistencia.sessao import obter_sessao


class ToalhaService:
    """
    Serviço responsável pelas regras de negócio e operações de Toalhas.
    """

    def cadastrar(self, identificador: int) -> Toalha:
        """Cadastra uma nova toalha validando duplicidade de ID."""
        identificador = int(identificador)

        with obter_sessao() as sessao:
            if sessao.get(Toalha, identificador) is not None:
                raise NadoLivreError(
                    f"A toalha com ID {identificador} já está cadastrada."
                )

            nova_toalha = Toalha(identificador)
            sessao.add(nova_toalha)
            sessao.commit()
            return nova_toalha

    def listar_todas(self) -> list[Toalha]:
        """Retorna todas as toalhas cadastradas."""
        with obter_sessao() as sessao:
            return list(sessao.scalars(select(Toalha).order_by(Toalha.id)))

    def consultar_disponiveis(self) -> list[Toalha]:
        """Retorna apenas toalhas livres para uso."""
        with obter_sessao() as sessao:
            return list(sessao.scalars(
                select(Toalha)
                .where(Toalha._em_uso.is_(False))
                .order_by(Toalha.id)
            ))

    def consultar_em_uso(self) -> list[Toalha]:
        """Retorna apenas toalhas atualmente emprestadas."""
        with obter_sessao() as sessao:
            return list(sessao.scalars(
                select(Toalha)
                .where(Toalha._em_uso.is_(True))
                .order_by(Toalha.id)
            ))