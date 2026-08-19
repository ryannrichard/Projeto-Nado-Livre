class Toalha:
    """
    Representa uma toalha disponibilizada pela escola.
    """

    def __init__(self, id: int) -> None:
        self.__id: int = id
        self.__em_uso: bool = False

    @property
    def id(self) -> str:
        return self.__id

    @property
    def em_uso(self) -> bool:
        return self.__em_uso

    def utilizar(self) -> None:
        self.__em_uso = True

    def disponibilizar(self) -> None:
        self.__em_uso = False

    def dados(self) -> int:
        estado = "Em uso" if self.__em_uso else "Disponível"
        return f"Toalha {self.__id} - {estado}"