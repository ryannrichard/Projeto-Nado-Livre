from nado_livre_ import NadoLivre
from servicos.ToalhaService import ToalhaService
from interface.telas.tela_toalhas import TelaToalhas
from interface.menus.menu import Menu
from excecoes.NadoLivreError import NadoLivreError

class MenuToalhas(Menu):
    """Menu das funcionalidades relacionadas às toalhas."""

    def __init__(self, nado_livre: NadoLivre) -> None:
        self.__toalha_service = ToalhaService(nado_livre)
        self.__tela = TelaToalhas()

    def executar(self) -> None:
        while True:
            print("\n===== TOALHAS =====")
            print("1 - Cadastrar toalha")
            print("2 - Listar toalhas")
            print("3 - Consultar toalhas disponíveis")
            print("4 - Consultar toalhas em uso")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            try:
                if opcao == "1":
                    self.cadastrar()
                elif opcao == "2":
                    self.listar()
                elif opcao == "3":
                    self.disponiveis()
                elif opcao == "4":
                    self.em_uso()
                elif opcao == "0":
                    return
                else:
                    print("Opção inválida.")
                    
            except (ValueError, NadoLivreError) as erro:
                print(f"Erro: {erro}")
                self.__tela.pausar()

    def cadastrar(self) -> None:
        identificador = self.__tela.solicitar_cadastro()
        toalha = self.__toalha_service.cadastrar(identificador)
        
        print(f"Toalha cadastrada com sucesso: ID {toalha.id}")
        self.__tela.pausar()

    def listar(self) -> None:
        toalhas = self.__toalha_service.listar_todas()
        self.__tela.mostrar_toalhas(toalhas, "TODAS AS TOALHAS")
        self.__tela.pausar()

    def disponiveis(self) -> None:
        toalhas = self.__toalha_service.consultar_disponiveis()
        self.__tela.mostrar_toalhas(toalhas, "TOALHAS DISPONÍVEIS")
        self.__tela.pausar()

    def em_uso(self) -> None:
        toalhas = self.__toalha_service.consultar_em_uso()
        self.__tela.mostrar_toalhas(toalhas, "TOALHAS EM USO")
        self.__tela.pausar()