from nado_livre_ import NadoLivre
from modelos.nadador import Nadador
from excecoes.NadoLivreError import NadoLivreError

class NadadorService:
    """
    Serviço responsável por coordenar as operações de negócio 
    relacionadas aos nadadores do sistema.
    """

    def __init__(self, aplicacao: NadoLivre) -> None:
        self._aplicacao = aplicacao

    def cadastrar(self, identificador: int, nome: str) -> Nadador:
        """Cadastra um novo nadador após validar as regras de negócio."""
        
        for nadador in self._aplicacao.obter_nadadores():
            if nadador.id == identificador:
                raise NadoLivreError(f"O nadador com ID {identificador} já está cadastrado.")
        
        if not nome.strip():
            raise NadoLivreError("O nome do nadador não pode ser vazio.")
        novo_nadador = Nadador(nome, identificador)
        
        self._aplicacao.adicionar_nadador(novo_nadador)
        return novo_nadador
    
    def listar_todos(self) -> list[Nadador]:
        """Retorna todos os nadadores cadastrados."""
        return self._aplicacao.obter_nadadores()
    
    def consultar(self, identificador: int) -> Nadador:
        """Busca um nadador pelo ID. Lança exceção se não encontrar."""
        for nadador in self._aplicacao.obter_nadadores():
            if nadador.id == identificador:
                return nadador
        raise NadoLivreError(f"Nadador com ID {identificador} não encontrado.")

    def consultar_utilizacoes(self, nadador_id: int) -> list:
        """Retorna o histórico de utilizações de um nadador específico."""
        self.consultar(nadador_id)
        utilizacoes = self._aplicacao.obter_utilizacoes()
        return [u for u in utilizacoes if u.nadador.id == nadador_id]