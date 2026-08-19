from interface.telas.tela import Tela
from excecoes.NadoLivreError import NadoLivreError

class TelaUtilizacoes(Tela):
    """Tela responsável pelas interações de retiradas e devoluções."""
    
    def __init__(self, app) -> None:
        self.__app = app

    def exibir(self, titulo: str = "") -> None:
        if titulo:
            print(f"\n=== {titulo} ===")

    def retirada(self) -> None:
        self.exibir("REGISTRAR RETIRADA")
        try:
            id_nadador = int(input("ID do Nadador: "))
            id_toalha = input("ID da Toalha: ").strip()
            id_atendente = int(input("ID do Atendente: "))

            self.__app.registrar_retirada(id_nadador, id_toalha, id_atendente)
            print("Retirada registrada com sucesso!")
        except ValueError:
            print("Erro: Digite apenas números para os IDs.")
        except NadoLivreError as erro:
            print(f"Atenção: {erro}")
        self.pausar()

    def devolucao(self) -> None:
        self.exibir("REGISTRAR DEVOLUÇÃO")
        try:
            id_toalha = input("ID da Toalha sendo devolvida: ")
            id_atendente = int(input("ID do Atendente recebendo: "))
            
            self.__app.registrar_devolucao(id_toalha, id_atendente)
            print("Devolução registrada com sucesso!")
        except ValueError:
            print("Erro: Digite apenas números para os IDs.")
        except NadoLivreError as erro:
            print(f"Atenção: {erro}")
        self.pausar()

    def consultar(self) -> None:
        self.exibir("CONSULTAR UTILIZAÇÃO")
        try:
            id_nadador = int(input("ID do Nadador: "))
            utilizacoes = self.__app.utilizacoes_do_nadador(id_nadador)
            
            if not utilizacoes:
                print("Nenhuma utilização encontrada para este nadador.")
            else:
                for util in utilizacoes:
                    print(util.dados())
        except ValueError:
            print("Erro: Digite apenas números.")
        except NadoLivreError as erro:
            print(f"Atenção: {erro}")
        self.pausar()

    def toalhas_em_uso(self) -> None:
        self.exibir("TOALHAS EM USO")
        toalhas = self.__app.listar_toalhas_em_uso()
        if not toalhas:
            print("Nenhuma toalha está em uso no momento.")
        else:
            for toalha in toalhas:
                print(toalha)
        self.pausar()

    def historico(self) -> None:
        self.exibir("HISTÓRICO GERAL")
        utilizacoes = self.__app.consultar_historico() 
        
        if not utilizacoes:
            print("Nenhum histórico registrado.")
        else:
            for util in utilizacoes:
                print(util.dados())
        self.pausar()

    def abertas(self) -> None:
        self.exibir("UTILIZAÇÕES ABERTAS (PENDENTES)")
        abertas = self.__app.listar_utilizacoes_abertas()
        if not abertas:
            print("Não há devoluções pendentes.")
        else:
            for util in abertas:
                print(util.dados())
        self.pausar()