from interface.menus.menu_principal import MenuPrincipal
from nado_livre_ import NadoLivre


def main():
    nado_livre = NadoLivre()

    menu_principal = MenuPrincipal(nado_livre)

    menu_principal.exibir()


if __name__ == "__main__":
    main()