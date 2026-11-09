from sqlalchemy import select

from modelos.nadador import Nadador
from excecoes.NadoLivreError import NadoLivreError
from persistencia.sessao import obter_sessao


class NadadorService:
    """
    Serviço responsável por coordenar as operações de negócio
    relacionadas aos nadadores do sistema.
    """

    def cadastrar(self, identificador: int, nome: str) -> Nadador:
        """Cadastra um novo nadador após validar as regras de negócio."""
        with obter_sessao() as sessao:
            if sessao.get(Nadador, identificador) is not None:
                raise NadoLivreError(
                    f"O nadador com ID {identificador} já está cadastrado."
                )

            if not nome.strip():
                raise NadoLivreError("O nome do nadador não pode ser vazio.")

            novo_nadador = Nadador(nome, identificador)
            sessao.add(novo_nadador)
            sessao.commit()
            return novo_nadador

    def listar_todos(self) -> list[Nadador]:
        """Retorna todos os nadadores cadastrados."""
        with obter_sessao() as sessao:
            return list(sessao.scalars(select(Nadador).order_by(Nadador.id)))

    def consultar(self, identificador: int) -> Nadador:
        """Busca um nadador pelo ID. Lança exceção se não encontrar."""
        with obter_sessao() as sessao:
            nadador = sessao.get(Nadador, identificador)
            if nadador is None:
                raise NadoLivreError(
                    f"Nadador com ID {identificador} não encontrado."
                )
            return nadador

    def consultar_utilizacoes(self, nadador_id: int) -> list:
        """Retorna o histórico de utilizações de um nadador específico."""
        return self.consultar(nadador_id).consultar_utilizacoes()

    def bloquear(self, identificador: int) -> Nadador:
        """Bloqueia um nadador e persiste a alteração."""
        return self._definir_bloqueio(identificador, True)

    def desbloquear(self, identificador: int) -> Nadador:
        """Desbloqueia um nadador e persiste a alteração."""
        return self._definir_bloqueio(identificador, False)

    def _definir_bloqueio(self, identificador: int, bloqueado: bool) -> Nadador:
        with obter_sessao() as sessao:
            nadador = sessao.get(Nadador, identificador)
            if nadador is None:
                raise NadoLivreError(
                    f"Nadador com ID {identificador} não encontrado."
                )
            nadador.bloqueio = bloqueado
            sessao.commit()
            return nadador