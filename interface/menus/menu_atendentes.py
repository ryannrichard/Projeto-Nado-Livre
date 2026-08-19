from interface.telas.tela_atendentes import TelaAtendentes
from interface.menus.menu import Menu

class MenuAtendentes(Menu):
    """Menu de operações relacionadas aos atendentes."""

    def __init__(self, app) -> None:
        self.__tela = TelaAtendentes(app)

    def executar(self) -> None:
        while True:
            print("\n===== ATENDENTES =====")
            print("1 - Cadastrar um atendente")
            print("2 - Listar atendentes")
            print("3 - Consultar atendente")
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
                self.__tela.consultar_utilizacoes()
            elif opcao == "0":
                return
            else:
                print("Opção inválida.")
