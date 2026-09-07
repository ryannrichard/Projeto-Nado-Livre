from nado_livre_ import NadoLivre
from servicos.AtendenteService import AtendenteService
from interface.menus.menu import Menu
from excecoes.NadoLivreError import NadoLivreError

class MenuAtendentes(Menu):
    """Menu das funcionalidades relacionadas aos atendentes."""

    def __init__(self, nado_livre: NadoLivre) -> None:
        self.__atendente_service = AtendenteService(nado_livre)

    def executar(self) -> None:
        while True:
            print("\n===== ATENDENTES =====")
            print("1 - Cadastrar um atendente")
            print("2 - Listar atendentes")
            print("3 - Consultar atendente")
            print("4 - Consultar utilizações")
            print("0 - Voltar")

            opcao = input("Escolha: ").strip()

            try:
                if opcao == "1":
                    self.cadastrar()
                elif opcao == "2":
                    self.listar()
                elif opcao == "3":
                    self.consultar()
                elif opcao == "4":
                    self.consultar_utilizacoes()
                elif opcao == "0":
                    return
                else:
                    print("Opção inválida.")
                    
            except (ValueError, NadoLivreError) as erro:
                print(f"\nErro: {erro}")
                input("Pressione ENTER para continuar...")

    def cadastrar(self) -> None:
        print("\n--- CADASTRAR ATENDENTE ---")
        identificador = int(input("ID do Atendente: "))
        nome = input("Nome do Atendente: ").strip()
        
        atendente = self.__atendente_service.cadastrar(identificador, nome)
        print(f"\nAtendente '{atendente.nome}' (ID: {atendente.id}) cadastrado com sucesso!")
        input("Pressione ENTER para continuar...")

    def listar(self) -> None:
        print("\n--- LISTA DE ATENDENTES ---")
        atendentes = self.__atendente_service.listar_todos()
        
        if not atendentes:
            print("Nenhum atendente cadastrado.")
        else:
            for a in atendentes:
                print(f"ID: {a.id} | Nome: {a.nome}")
                
        input("\nPressione ENTER para continuar...")

    def consultar(self) -> None:
        print("\n--- CONSULTAR ATENDENTE ---")
        identificador = int(input("Digite o ID do Atendente: "))
        
        atendente = self.__atendente_service.consultar(identificador)
        print(f"\nAtendente encontrado: ID: {atendente.id} | Nome: {atendente.nome}")
        input("Pressione ENTER para continuar...")

    def consultar_utilizacoes(self) -> None:
        print("\n--- CONSULTAR UTILIZAÇÕES DO ATENDENTE ---")
        identificador = int(input("Digite o ID do Atendente: "))
        
        utilizacoes = self.__atendente_service.consultar_utilizacoes(identificador)
        
        if not utilizacoes:
            print("Este atendente não possui registro de operações (entregas ou devoluções).")
        else:
            print(f"\nHistórico de Operações do Atendente ID {identificador}:")
            for u in utilizacoes:
                status = "Aberta" if u.aberta else "Concluída"
                print(f"- Toalha ID {u.toalha.id} para Nadador ID {u.nadador.id} | Status: {status}")
                
        input("\nPressione ENTER para continuar...")