from interface.telas.tela_utilizacoes import TelaUtilizacoes
from interface.menus.menu import Menu

class MenuUtilizacoes(Menu):
    """Menu de operações do ciclo de utilização das toalhas."""

    def __init__(self, app) -> None:
        self.__tela = TelaUtilizacoes(app)

    def executar(self) -> None:
        while True:
            print("\n===== UTILIZAÇÕES =====")
            print("1 - Registrar retirada")
            print("2 - Registrar devolução")
            print("3 - Consultar utilização")
            print("4 - Listar toalhas em uso")
            print("5 - Consultar histórico")
            print("6 - Utilizações abertas")
            print("0 - Voltar")
            opcao = input("Escolha: ").strip()

            if opcao == "1":
                self.__tela.retirada()
            elif opcao == "2":
                self.__tela.devolucao()
            elif opcao == "3":
                self.__tela.consultar()
            elif opcao == "4":
                self.__tela.toalhas_em_uso()
            elif opcao == "5":
                self.__tela.historico()
            elif opcao == "6":
                self.__tela.abertas()
            elif opcao == "0":
                return
            else:
                print("Opção inválida.")
