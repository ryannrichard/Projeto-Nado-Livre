from nado_livre_ import NadoLivre
from .menu_nadadores import MenuNadadores
from .menu_atendentes import MenuAtendentes
from .menu_toalhas import MenuToalhas
from .menu_utilizacoes import MenuUtilizacoes
from interface.menus.menu import Menu

class MenuPrincipal(Menu):
    """
    Representa o menu principal do sistema Nado Livre.
    """
    def __init__(self, nado_livre: NadoLivre) -> None:
        self.nado_livre = nado_livre

    def exibir(self) -> None:
        while True:
            print()
            print("=" * 40)
            print("          SISTEMA NADO LIVRE")
            print("=" * 40)
            print("1 - Nadadores")
            print("2 - Atendentes")
            print("3 - Toalhas")
            print("4 - Utilizações")
            print("0 - Sair")
            print("=" * 40)

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                menu = MenuNadadores(self.nado_livre)
                menu.executar()
            elif opcao == "2":
                menu = MenuAtendentes(self.nado_livre)
                menu.executar()
            elif opcao == "3":
                menu = MenuToalhas(self.nado_livre)
                menu.executar()
            elif opcao == "4":
                menu = MenuUtilizacoes(self.nado_livre)
                menu.executar()
            elif opcao == "0":
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida.")