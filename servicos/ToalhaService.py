from nado_livre_ import NadoLivre
from modelos.toalha import Toalha
from excecoes.NadoLivreError import NadoLivreError

class ToalhaService:
    """
    Serviço responsável pelas regras de negócio e operações de Toalhas.
    """

    def __init__(self, aplicacao: NadoLivre) -> None:
        self._aplicacao = aplicacao

    def cadastrar(self, identificador: int) -> Toalha:
        """Cadastra uma nova toalha validando duplicidade de ID."""
        for toalha in self._aplicacao.obter_toalhas():
            if toalha.id == identificador:
                raise NadoLivreError(f"A toalha com ID {identificador} já está cadastrada.")
        
        nova_toalha = Toalha(identificador)
        self._aplicacao.adicionar_toalha(nova_toalha)
        return nova_toalha

    def listar_todas(self) -> list[Toalha]:
        """Retorna todas as toalhas cadastradas."""
        return self._aplicacao.obter_toalhas()

    def consultar_disponiveis(self) -> list[Toalha]:
        """Retorna apenas toalhas livres para uso."""
        return [t for t in self._aplicacao.obter_toalhas() if not t.em_uso]

    def consultar_em_uso(self) -> list[Toalha]:
        """Retorna apenas toalhas atualmente emprestadas."""
        return [t for t in self._aplicacao.obter_toalhas() if t.em_uso]