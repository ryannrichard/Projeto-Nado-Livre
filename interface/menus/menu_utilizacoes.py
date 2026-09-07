from nado_livre_ import NadoLivre
from servicos.UtilizacaoService import UtilizacaoService
from interface.menus.menu import Menu
from excecoes.NadoLivreError import NadoLivreError
from interface.telas.tela_utilizacoes import TelaUtilizacoes

class MenuUtilizacoes(Menu):
    """
    Menu responsável pela interação com o usuário para registros 
    de retiradas e devoluções.
    """

    def __init__(self, nado_livre: NadoLivre) -> None:
        self.__utilizacao_service = UtilizacaoService(nado_livre)
        self.__tela = TelaUtilizacoes(nado_livre)

    def executar(self) -> None:
        while True:
            print("\n===== EMPRÉSTIMOS E DEVOLUÇÕES =====")
            print("1 - Registrar Retirada de Toalha")
            print("2 - Registrar Devolução de Toalha")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            try:
                if opcao == "1":
                    self.registrar_retirada()
                elif opcao == "2":
                    self.registrar_devolucao()
                elif opcao == "0":
                    return
                else:
                    print("Opção inválida.")
                    
            except (ValueError, NadoLivreError) as erro:
                print(f"\nAtenção: {erro}")
                self.__tela.pausar()

    def registrar_retirada(self) -> None:
        print("\n--- REGISTRO DE RETIRADA ---")
        nadador_id = int(input("ID do Nadador: "))
        toalha_id = int(input("ID da Toalha: "))
        atendente_id = int(input("ID do Atendente: "))
        self.__utilizacao_service.registrar_retirada(toalha_id, nadador_id, atendente_id)
        
        print("\nRetirada registrada com sucesso! A toalha agora consta como em uso.")
        self.__tela.pausar()

    def registrar_devolucao(self) -> None:
        print("\n--- REGISTRO DE DEVOLUÇÃO ---")
        toalha_id = int(input("ID da Toalha sendo devolvida: "))
        atendente_id = int(input("ID do Atendente que está recebendo: "))
        self.__utilizacao_service.registrar_devolucao(toalha_id, atendente_id)
        
        print("\nDevolução registrada com sucesso! A toalha está livre novamente.")
        self.__tela.pausar()