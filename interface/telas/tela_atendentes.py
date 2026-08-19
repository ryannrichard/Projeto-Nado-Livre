from interface.telas.tela import Tela
from excecoes.NadoLivreError import NadoLivreError

class TelaAtendentes(Tela):
    """Tela responsável pelas operações de interação com atendentes."""
    
    def __init__(self, app) -> None:
        self.__app = app

    def exibir(self, *args, **kwargs) -> None:
        pass

    def cadastrar(self) -> None:
        self.exibir("CADASTRO DE ATENDENTE")
        nome = input("Nome: ").strip()
        
        try:
            identificador = int(input("ID: ").strip())
            self.__app.cadastrar_atendente(nome, identificador)
            print("Atendente cadastrado com sucesso!")
        except ValueError:
            print("Erro: O ID deve ser um número.")
        except NadoLivreError as erro:
            print(f"Atenção: {erro}")
        self.pausar()

    def consultar(self) -> None:
        self.exibir("CONSULTA DE ATENDENTE")
        try:
            identificador = int(input("ID do atendente: "))
            atendente = self.__app.localizar_atendente(identificador)
            print(atendente)
        except ValueError:
            print("Erro: Digite apenas números para o ID.")
        except NadoLivreError:
            print("Atenção: Atendente não encontrado!")
        self.pausar()

    def listar(self) -> None:
        self.exibir("ATENDENTES CADASTRADOS")
        atendentes = self.__app.listar_atendentes()
        
        if not atendentes:
            print("Nenhum atendente cadastrado.")
        else:
            for atendente in atendentes:
                print(f"- {atendente.dados()}") 
        self.pausar()

    def consultar_utilizacoes(self) -> None:
        self.exibir("UTILIZAÇÕES DO ATENDENTE")
        try:
            identificador = int(input("ID do atendente: "))
            utilizacoes = self.__app.utilizacoes_do_atendente(identificador)
            
            if not utilizacoes:
                print("Nenhuma utilização encontrada para este atendente.")
            else:
                for util in utilizacoes:
                    print(util)
        except ValueError:
            print("Erro: Digite apenas números para o ID.")
        except NadoLivreError as erro:
            print(f"Atenção: {erro}")
        self.pausar()