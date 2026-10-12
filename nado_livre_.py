from modelos.nadador import Nadador
from modelos.atendente import Atendente
from modelos.toalha import Toalha
from modelos.utilizacao import Utilizacao

from persistencia.nadador_persistencia import NadadorPersistencia
from persistencia.atendente_persistencia import AtendentePersistencia
from persistencia.toalha_persistencia import ToalhaPersistencia
from persistencia.utilizacao_persistencia import UtilizacaoPersistencia


class NadoLivre:
    """
    Controla os cadastros e as utilizações das toalhas
    da escola de natação, mantendo os dados em memória
    e realizando a persistência em arquivos JSON.
    """

    def __init__(self) -> None:
        # Listas que armazenam os objetos em memória
        self.__nadadores: list[Nadador] = []
        self.__atendentes: list[Atendente] = []
        self.__toalhas: list[Toalha] = []
        self.__utilizacoes: list[Utilizacao] = []

        # Objetos responsáveis pela persistência
        self.__persistencia_nadadores = NadadorPersistencia(
            "dados/nadadores.json"
        )
        self.__persistencia_atendentes = AtendentePersistencia(
            "dados/atendentes.json"
        )
        self.__persistencia_toalhas = ToalhaPersistencia(
            "dados/toalhas.json"
        )
        self.__persistencia_utilizacoes = UtilizacaoPersistencia(
            "dados/utilizacoes.json"
        )

        # Recupera os dados salvos anteriormente
        self.__carregar_dados()

    def __carregar_dados(self) -> None:
        """Carrega os cadastros e depois reconstrói os históricos."""

        # Primeiro, carrega os objetos principais
        self.__nadadores = self.__persistencia_nadadores.carregar()
        self.__atendentes = self.__persistencia_atendentes.carregar()
        self.__toalhas = self.__persistencia_toalhas.carregar()

        # Depois, carrega as utilizações e reconstrói os vínculos
        self.__utilizacoes = self.__persistencia_utilizacoes.carregar(
            self.__nadadores,
            self.__toalhas,
            self.__atendentes
        )

    def salvar_dados(self) -> None:
        """Salva todos os dados do sistema nos arquivos JSON."""

        self.__persistencia_nadadores.salvar(self.__nadadores)
        self.__persistencia_atendentes.salvar(self.__atendentes)
        self.__persistencia_toalhas.salvar(self.__toalhas)
        self.__persistencia_utilizacoes.salvar(self.__utilizacoes)

    # Métodos de toalhas

    def obter_toalhas(self) -> list[Toalha]:
        return self.__toalhas.copy()

    def adicionar_toalha(self, toalha: Toalha) -> None:
        self.__toalhas.append(toalha)
        self.salvar_dados()

    # Métodos de utilizações

    def obter_utilizacoes(self) -> list[Utilizacao]:
        return self.__utilizacoes.copy()

    def adicionar_utilizacao(self, utilizacao: Utilizacao) -> None:
        self.__utilizacoes.append(utilizacao)
        self.salvar_dados()

    # Métodos de nadadores

    def obter_nadadores(self) -> list[Nadador]:
        return self.__nadadores.copy()

    def adicionar_nadador(self, nadador: Nadador) -> None:
        self.__nadadores.append(nadador)
        self.salvar_dados()

    # Métodos de atendentes

    def obter_atendentes(self) -> list[Atendente]:
        return self.__atendentes.copy()

    def adicionar_atendente(self, atendente: Atendente) -> None:
        self.__atendentes.append(atendente)
        self.salvar_dados()