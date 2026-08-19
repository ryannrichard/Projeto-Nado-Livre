class Nadador:
    """
    Representa um nadador cadastrado na escola,
    com foco em armazenar os dados e vincular as utilizações.
    """

    def __init__(self, nome: str, id: int) -> None:
        self.nome: str = nome
        self.id: int = id
        self.__utilizacoes: list = []

    def __str__(self):
        return f"Nadador [ID: {self.id} | Nome: {self.nome}]"
    
    def dados(self) -> str:
        return f"{self.nome} (ID: {self.id})"

    def adicionar_utilizacao(self, utilizacao) -> None:
        self.__utilizacoes.append(utilizacao)

    def consultar_utilizacoes(self) -> list:
        return self.__utilizacoes