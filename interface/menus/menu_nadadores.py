from nado_livre_ import NadoLivre
from servicos.NadadorService import NadadorService
from interface.menus.menu import Menu
from excecoes.NadoLivreError import NadoLivreError

class MenuNadadores(Menu):
    """Menu das funcionalidades relacionadas aos nadadores."""

    def __init__(self, nado_livre: NadoLivre) -> None:
        self.__nadador_service = NadadorService(nado_livre)

    def executar(self) -> None:
        while True:
            print("\n===== NADADORES =====")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("3 - Consultar")
            print("4 - Consultar utilizações")
            print("5 - Bloquear Nadador")
            print("6 - Desbloquear Nadador")
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
                elif opcao == "5":
                    self.bloquear()
                elif opcao == "6":
                    self.desbloquear()
                elif opcao == "0":
                    return
                else:
                    print("Opção inválida.")
                    
            except (ValueError, NadoLivreError) as erro:
                print(f"\nErro: {erro}")
                input("Pressione ENTER para continuar...")

    def cadastrar(self) -> None:
        print("\n--- CADASTRAR NADADOR ---")
        identificador = int(input("ID do Nadador: "))
        nome = input("Nome do Nadador: ").strip()
        
        nadador = self.__nadador_service.cadastrar(identificador, nome)
        print(f"\nNadador '{nadador.nome}' (ID: {nadador.id}) cadastrado com sucesso!")
        input("Pressione ENTER para continuar...")

    def listar(self) -> None:
        print("\n--- LISTA DE NADADORES ---")
        nadadores = self.__nadador_service.listar_todos()
        
        if not nadadores:
            print("Nenhum nadador cadastrado.")
        else:
           for n in nadadores:
                situacao_toalha = "Toalha retirada" if n.tem_toalha_retirada() else "Sem toalha"
                status_bloqueio = " [Bloqueado]" if getattr(n, "bloqueio", False) else "[Desbloqueado]"
                
                print(f"ID: {n.id} - {n.nome} - {situacao_toalha} - {status_bloqueio}")
                
        input("\nPressione ENTER para continuar...")

    def consultar(self) -> None:
        print("\n--- CONSULTAR NADADOR ---")
        identificador = int(input("Digite o ID do Nadador: "))
        
        nadador = self.__nadador_service.consultar(identificador)
        
        situacao_toalha = "Toalha retirada" if nadador.tem_toalha_retirada() else "Sem toalha"
        status_bloqueio = "[Bloqueado]" if getattr(nadador, "bloqueio", False) else "[Desbloqueado]"
        
        print(
            f"\nNadador encontrado: ID: {nadador.id} - {nadador.nome} - "
            f"{situacao_toalha} - {status_bloqueio}"
        )
        
        input("\nPressione ENTER para continuar...")

    def consultar_utilizacoes(self) -> None:
        print("\n--- CONSULTAR UTILIZAÇÕES DO NADADOR ---")
        identificador = int(input("Digite o ID do Nadador: "))
        
        utilizacoes = self.__nadador_service.consultar_utilizacoes(identificador)
        
        if not utilizacoes:
            print("Este nadador não possui registro de utilizações.")
        else:
            print(f"\nHistórico de Utilizações do Nadador ID {identificador}:")
            for u in utilizacoes:
                status = "Aberta" if u.aberta else "Concluída"
                print(f"- Toalha ID {u.toalha.id} | Status: {status}")
                
        input("\nPressione ENTER para continuar...")
    
    def bloquear(self) -> None:
        print("\n--- BLOQUEIO DE NADADOR ---")
        try:
            identificador = int(input("Digite o ID do Nadador: "))
            nadador = self.__nadador_service.bloquear(identificador)
            print(f"Nadador '{nadador.nome}' bloqueado com sucesso!")
        except ValueError:
            print("Erro: ID inválido. Digite apenas números.")
        except NadoLivreError as erro:
            print(f"Erro: {erro}")
        input("\nPressione ENTER para continuar...")
    
    def desbloquear(self) -> None:
        print("\n--- DESBLOQUEIO DE NADADOR ---")
        try:
            identificador = int(input("Digite o ID do Nadador: "))
            nadador = self.__nadador_service.desbloquear(identificador)
            print(f"Nadador '{nadador.nome}' desbloqueado com sucesso!")
        except ValueError:
            print("Erro: ID inválido. Digite apenas números.")
        except NadoLivreError as erro:
            print(f"Erro: {erro}")
        input("\nPressione ENTER para continuar...")