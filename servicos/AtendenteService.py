from sqlalchemy import or_, select

from modelos.atendente import Atendente
from modelos.utilizacao import Utilizacao
from excecoes.NadoLivreError import NadoLivreError
from persistencia.sessao import obter_sessao


class AtendenteService:
    """
    Serviço responsável por coordenar as operações de negócio
    relacionadas aos atendentes do sistema.
    """

    def cadastrar(self, identificador: int, nome: str) -> Atendente:
        """Cadastra um novo atendente após validar as regras de negócio."""
        with obter_sessao() as sessao:
            if sessao.get(Atendente, identificador) is not None:
                raise NadoLivreError(
                    f"O atendente com ID {identificador} já está cadastrado."
                )

            if not nome.strip():
                raise NadoLivreError("O nome do atendente não pode ser vazio.")

            novo_atendente = Atendente(nome, identificador)
            sessao.add(novo_atendente)
            sessao.commit()
            return novo_atendente

    def listar_todos(self) -> list[Atendente]:
        """Retorna todos os atendentes cadastrados."""
        with obter_sessao() as sessao:
            return list(sessao.scalars(select(Atendente).order_by(Atendente.id)))

    def consultar(self, identificador: int) -> Atendente:
        """Busca um atendente pelo ID. Lança exceção se não encontrar."""
        with obter_sessao() as sessao:
            atendente = sessao.get(Atendente, identificador)
            if atendente is None:
                raise NadoLivreError(
                    f"Atendente com ID {identificador} não encontrado."
                )
            return atendente

    def consultar_utilizacoes(self, atendente_id: int) -> list[Utilizacao]:
        """Retorna as utilizações em que o atendente entregou ou recebeu."""
        self.consultar(atendente_id)

        with obter_sessao() as sessao:
            return list(sessao.scalars(
                select(Utilizacao)
                .where(or_(
                    Utilizacao.atendente_entrega_id == atendente_id,
                    Utilizacao.atendente_devolucao_id == atendente_id,
                ))
                .order_by(Utilizacao.id)
            ))