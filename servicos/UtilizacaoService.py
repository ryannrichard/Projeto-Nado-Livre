from nado_livre_ import NadoLivre
from modelos.utilizacao import Utilizacao
from excecoes.NadoLivreError import NadoLivreError

class UtilizacaoService:
    """
    Serviço responsável por coordenar empréstimos e devoluções de toalhas,
    garantindo a aplicação das regras de negócio.
    """

    def __init__(self, aplicacao: NadoLivre) -> None:
        self._aplicacao = aplicacao

    def registrar_retirada(self, toalha_id: int, nadador_id: int, atendente_id: int) -> Utilizacao:
        """Registra a retirada de uma toalha validando as regras de negócio."""
        
        toalha_id = int(toalha_id)
        nadador_id = int(nadador_id)
        atendente_id = int(atendente_id)

        toalha = None
        for t in self._aplicacao.obter_toalhas():
            if int(t.id) == toalha_id:
                toalha = t
                break
        if not toalha:
            raise NadoLivreError(f"Toalha com ID {toalha_id} não encontrada.")

        nadador = None
        for n in self._aplicacao.obter_nadadores():
            if int(n.id) == nadador_id:
                nadador = n
                break
        if not nadador:
            raise NadoLivreError(f"Nadador com ID {nadador_id} não encontrado.")

        atendente = None
        for a in self._aplicacao.obter_atendentes():
            if int(a.id) == atendente_id:
                atendente = a
                break
        if not atendente:
            raise NadoLivreError(f"Atendente com ID {atendente_id} não encontrado.")

        if toalha.em_uso:
            raise NadoLivreError(f"A toalha ID {toalha_id} já está em uso.")

        toalha.utilizar()

        nova_utilizacao = Utilizacao(nadador, toalha, atendente)
        self._aplicacao.adicionar_utilizacao(nova_utilizacao)
        return nova_utilizacao
    
    def registrar_devolucao(self, toalha_id: int, atendente_id: int) -> Utilizacao:
        """Registra a devolução de uma toalha que está em uso."""
        
        toalha_id = int(toalha_id)
        atendente_id = int(atendente_id)

        utilizacao_encontrada = None
        for u in self._aplicacao.obter_utilizacoes():
            if int(u.toalha.id) == toalha_id and u.aberta:
                utilizacao_encontrada = u
                break

        if not utilizacao_encontrada:
            raise NadoLivreError(f"Não há empréstimo em aberto para a toalha ID {toalha_id}.")

        atendente = None
        for a in self._aplicacao.obter_atendentes():
            if int(a.id) == atendente_id:
                atendente = a
                break

        if not atendente:
            raise NadoLivreError(f"Atendente com ID {atendente_id} não encontrado.")

        utilizacao_encontrada.encerrar(atendente)
        return utilizacao_encontrada

    def _localizar_nadador(self, identificador: int):
        for n in self._aplicacao.obter_nadadores():
            if n.id == identificador: return n
        raise NadoLivreError(f"Nadador {identificador} não encontrado.")

    def _localizar_toalha(self, identificador: int):
        for t in self._aplicacao.obter_toalhas():
            if t.id == identificador: return t
        raise NadoLivreError(f"Toalha {identificador} não encontrada.")

    def _localizar_atendente(self, identificador: int):
        for a in self._aplicacao.obter_atendentes():
            if a.id == identificador: return a
        raise NadoLivreError(f"Atendente {identificador} não encontrado.")