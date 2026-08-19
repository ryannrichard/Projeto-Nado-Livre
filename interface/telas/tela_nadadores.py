from interface.telas.tela import Tela
from excecoes.NadoLivreError import NadoLivreError


class TelaNadadores(Tela):
    """Realiza a interação textual com os cadastros de nadadores."""

    def __init__(self, app) -> None:
        self.__app = app

    def cadastrar(self) -> None:
        try:
            identificador = int(input("ID do nadador: "))
            nome = input("Nome: ")
            self.__app.cadastrar_nadador(nome, identificador)
            print("Nadador cadastrado com sucesso.")
        except (ValueError, NadoLivreError) as erro:
            print(f"Erro: Já existe nadador com esse ID")
        self.pausar()

    def listar(self) -> None:
        nadadores = self.__app.listar_nadadores()
        print("\n--- Nadadores ---")
        if not nadadores:
            print("Nenhum nadador cadastrado.")
        for n in nadadores:
            print(f"Número: {n.id} / Nadador: {n.nome}")
        self.pausar()

    def consultar(self) -> None:
        try:
            identificador = int(input("ID do nadador: "))
            nadador = self.__app.localizar_nadador(identificador)
            print(nadador)
        except ValueError:
            print("Erro: ID inválido. Digite apenas números.")
        except NadoLivreError as erro:
            print(f"Atenção: {erro}")
        self.pausar()

    def utilizacoes(self) -> None:
        try:
            identificador = int(input("ID do nadador: "))
            utilizacoes = self.__app.utilizacoes_do_nadador(identificador)
            for i, u in enumerate(utilizacoes):
                print(f"{i}: {u.dados()}")
            if not utilizacoes:
                print("Nenhuma utilização encontrada.")
        except (ValueError, NadoLivreError) as erro:
            print(f"Erro: {erro}")
        self.pausar()