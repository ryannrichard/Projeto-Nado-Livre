from modelos.nadador import Nadador
from modelos.atendente import Atendente
from modelos.toalha import Toalha
from modelos.utilizacao import Utilizacao

class NadoLivre():
    """
    Controla os cadastros e as utilizações das toalhas
    da escola de natação. Atua como o local dos dados em memória do sistema.
    """
    def __init__(self) -> None:
        self.__nadadores: list[Nadador] = []
        self.__atendentes: list[Atendente] = []
        self.__toalhas: list[Toalha] = []
        self.__utilizacoes: list[Utilizacao] = []

    def obter_toalhas(self) -> list:
        return self.__toalhas.copy()

    def adicionar_toalha(self, toalha) -> None:
        self.__toalhas.append(toalha)

    def obter_utilizacoes(self) -> list:
        return self.__utilizacoes.copy()

    def adicionar_utilizacao(self, utilizacao) -> None:
        self.__utilizacoes.append(utilizacao)
    
    def obter_nadadores(self) -> list:
        return self.__nadadores.copy()

    def adicionar_nadador(self, nadador) -> None:
        self.__nadadores.append(nadador)

    def obter_atendentes(self) -> list:
        return self.__atendentes.copy()

    def adicionar_atendente(self, atendente) -> None:
        self.__atendentes.append(atendente)