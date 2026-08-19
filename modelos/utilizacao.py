from modelos.nadador import Nadador
from modelos.atendente import Atendente
from modelos.toalha import Toalha
from excecoes.utilizacao_encerrada_error import UtilizacaoEncerradaError

class Utilizacao:
    """
    Representa a utilização de uma toalha por um nadador,
    incluindo sua entrega e posterior devolução.
    """

    def __init__(
        self,
        nadador: Nadador,
        toalha: Toalha,
        atendente_entrega: Atendente
    ) -> None:
        self.__nadador = nadador
        self.__toalha = toalha
        self.__atendente_entrega = atendente_entrega
        self.__atendente_devolucao = None
        self.__aberta: bool = True

    @property
    def nadador(self) -> Nadador:
        return self.__nadador

    @property
    def toalha(self) -> Toalha:
        return self.__toalha

    @property
    def atendente_entrega(self) -> Atendente:
        return self.__atendente_entrega

    @property
    def atendente_devolucao(self) -> Atendente:
        return self.__atendente_devolucao

    @property
    def aberta(self) -> bool:
        return self.__aberta

    def encerrar(self, atendente: Atendente) -> None:
        if not self.__aberta:
            raise UtilizacaoEncerradaError("A utilização já está encerrada.")

        self.__atendente_devolucao = atendente
        self.__aberta = False
        self.__toalha.disponibilizar()

    def dados(self) -> str:
        estado = "Aberta" if self.__aberta else "Encerrada"

        return (
            f"Nadador: {self.__nadador.nome} | "
            f"Toalha: {self.__toalha.id} | "
            f"Entrega: {self.__atendente_entrega.nome} | "
            f"Estado: {estado}"
        )
