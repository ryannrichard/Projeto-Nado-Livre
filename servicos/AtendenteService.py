from nado_livre_ import NadoLivre
from modelos.atendente import Atendente
from excecoes.NadoLivreError import NadoLivreError

class AtendenteService:
    """
    Serviço responsável por coordenar as operações de negócio 
    relacionadas aos atendentes do sistema.
    """

    def __init__(self, aplicacao: NadoLivre) -> None:
        self._aplicacao = aplicacao

    def cadastrar(self, identificador: int, nome: str) -> Atendente:
        """Cadastra um novo atendente após validar as regras de negócio."""
        
        for atendente in self._aplicacao.obter_atendentes():
            if atendente.id == identificador:
                raise NadoLivreError(f"O atendente com ID {identificador} já está cadastrado.")
        
        if not nome.strip():
            raise NadoLivreError("O nome do atendente não pode ser vazio.")
            
        novo_atendente = Atendente(nome, identificador)
        self._aplicacao.adicionar_atendente(novo_atendente)
        return novo_atendente

    def listar_todos(self) -> list[Atendente]:
        """Retorna todos os atendentes cadastrados."""
        return self._aplicacao.obter_atendentes()
    
    def consultar(self, identificador: int) -> Atendente:
        """Busca um atendente pelo ID. Lança exceção se não encontrar."""
        for atendente in self._aplicacao.obter_atendentes():
            if atendente.id == identificador:
                return atendente
        raise NadoLivreError(f"Atendente com ID {identificador} não encontrado.")
    
    def consultar_utilizacoes(self, atendente_id: int) -> list:
        """Retorna o histórico de utilizações vinculadas a um atendente específico."""
        self.consultar(atendente_id)
        
        utilizacoes = self._aplicacao.obter_utilizacoes()
        
        historico = []
        for u in utilizacoes:
            if u.atendente_entrega is not None and u.atendente_entrega.id == atendente_id:
                historico.append(u)
                
            elif u.atendente_devolucao is not None and u.atendente_devolucao.id == atendente_id:
                historico.append(u)
                
        return historico