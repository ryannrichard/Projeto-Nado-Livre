from nado_livre_ import NadoLivre
from interface.telas.tela_toalhas import TelaToalhas
from interface.menus.menu import Menu

class MenuToalhas(Menu):
    """Menu das funcionalidades relacionadas às toalhas."""

    def __init__(self, nado_livre: NadoLivre) -> None:
        self.__nado_livre = nado_livre
        self.__tela = TelaToalhas()

    def executar(self) -> None:
        while True:
            print("\n===== TOALHAS =====")
            print("1 - Cadastrar toalha")
            print("2 - Listar toalhas")
            print("3 - Consultar toalhas disponíveis")
            print("4 - Consultar toalhas em uso")
            print("5 - Identificar nadador responsável por uma toalha")
            print("6 - Consultar histórico de uma toalha")
            print("0 - Voltar")
            opcao = input("Escolha uma opção: ").strip()
            try:
                if opcao == "1": self.cadastrar()
                elif opcao == "2": self.listar()
                elif opcao == "3": self.disponiveis()
                elif opcao == "4": self.em_uso()
                elif opcao == "5": self.responsavel()
                elif opcao == "6": self.historico()
                elif opcao == "0": return
                else: print("Opção inválida.")
            except Exception as erro:
                print(f"Erro: {erro}")

    def cadastrar(self) -> None:
        identificador = self.__tela.solicitar_cadastro()
        if not identificador:
            print("ID é obrigatório.")
            return
        toalha = self.__nado_livre.cadastrar_toalha(identificador)
        print(f"Toalha cadastrada: {toalha.dados()}")

    def listar(self) -> None:
        self.__tela.mostrar_toalhas(self.__nado_livre.listar_toalhas(), "TODAS AS TOALHAS")
        self.__tela.pausar()

    def disponiveis(self) -> None:
        self.__tela.mostrar_toalhas(self.__nado_livre.consultar_toalhas_disponiveis(), "TOALHAS DISPONÍVEIS")
        self.__tela.pausar()

    def em_uso(self) -> None:
        self.__tela.mostrar_toalhas(self.__nado_livre.consultar_toalhas_em_uso(), "TOALHAS EM USO")
        self.__tela.pausar()

    def responsavel(self) -> None:
        toalha = self.__nado_livre.localizar_toalha(self.__tela.solicitar_id("TOALHA EM USO"))
        utilizacao = next(
            (u for u in self.__nado_livre.listar_utilizacoes() if u.toalha == toalha and u.aberta),
            None,
        )
        self.__tela.mostrar_responsavel(toalha, utilizacao)
        self.__tela.pausar()

    def historico(self) -> None:
        toalha = self.__nado_livre.localizar_toalha(self.__tela.solicitar_id("HISTÓRICO DA TOALHA"))
        utilizacoes = [u for u in self.__nado_livre.listar_utilizacoes() if u.toalha == toalha]
        self.__tela.mostrar_toalhas([toalha], "TOALHA")
        if utilizacoes:
            print("\nHistórico:")
            for u in utilizacoes:
                print(f"- {u.dados()}")
                if u.atendente_devolucao:
                    print(f"  Atendente da devolução: {u.atendente_devolucao.dados()}")
        else:
            print("Nenhuma utilização registrada para esta toalha.")
        self.__tela.pausar()
