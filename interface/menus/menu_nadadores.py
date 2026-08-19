from interface.telas.tela_nadadores import TelaNadadores
from interface.menus.menu import Menu

class MenuNadadores(Menu):
    """Menu de operações relacionadas aos nadadores."""

    def __init__(self, app) -> None:
        self.__app = app
        self.__tela = TelaNadadores(app)

    def executar(self) -> None:
        while True:
            print("\n===== NADADORES =====")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("3 - Consultar")
            print("4 - Consultar utilizações")
            print("0 - Voltar")
            opcao = input("Escolha: ").strip()

            if opcao == "1":
                self.__tela.cadastrar()
            elif opcao == "2":
                self.__tela.listar()
            elif opcao == "3":
                self.__tela.consultar()
            elif opcao == "4":
                self.__tela.utilizacoes()
            elif opcao == "0":
                return
            else:
                print("Opção inválida.")