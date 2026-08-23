from modelos.nadador import Nadador
from modelos.atendente import Atendente
from modelos.toalha import Toalha
from modelos.utilizacao import Utilizacao

from excecoes.nado_livre_error import NadoLivreError
from excecoes.nadador_nao_encontrado_error import NadadorNaoEncontradoError
from excecoes.atendente_nao_encontrado_error import AtendenteNaoEncontradoError
from excecoes.toalha_nao_encontrada_error import ToalhaNaoEncontradaError
from excecoes.toalha_indisponivel_error import ToalhaIndisponivelError
from excecoes.utilizacao_nao_encontrada_error import UtilizacaoNaoEncontradaError
from excecoes.utilizacao_encerrada_error import UtilizacaoEncerradaError


class NadoLivre():
    """
    Controla os cadastros e as utilizações das toalhas
    da escola de natação.
    """

    def __init__(self) -> None:
        self.__nadadores: list[Nadador] = []
        self.__atendentes: list[Atendente] = []
        self.__toalhas: list[Toalha] = []
        self.__utilizacoes: list[Utilizacao] = []

    # ---------------- NADADORES ----------------

    def cadastrar_nadador(self, nome: str, id: str) -> Nadador:
        for nadador in self.__nadadores:  
            if nadador.id == id: 
                raise NadoLivreError(f"O ID {id} já está em uso!")
        novo_nadador = Nadador(nome, id)
        self.__nadadores.append(novo_nadador)
        return novo_nadador

    def listar_nadadores(self) -> list[Nadador]:
        return self.__nadadores

    def localizar_nadador(self, id: str) -> Nadador:
        for nadador in self.__nadadores:
            if nadador.id == id:
                return nadador

        raise NadadorNaoEncontradoError(
            f"Nadador {id} não encontrado."
        )

    def utilizacoes_do_nadador(self, id: str) -> list[Utilizacao]:
        self.localizar_nadador(id)

        historico = []
        for utilizacao in self.__utilizacoes:
            if utilizacao.nadador.id == id: 
                historico.append(utilizacao)
        return historico

    # ---------------- ATENDENTES ----------------

    def cadastrar_atendente(self, nome: str, id: str) -> Atendente:
        for atendente in self.__atendentes:  
            if atendente.id == id: 
                raise NadoLivreError(f"O ID {id} já está em uso!")
        atendente = Atendente(nome, id)
        self.__atendentes.append(atendente)
        return atendente

    def listar_atendentes(self) -> list[Atendente]:
        return self.__atendentes

    def localizar_atendente(self, id: str) -> Atendente:
        for atendente in self.__atendentes:
            if atendente.id == id:
                return atendente

        raise AtendenteNaoEncontradoError(
            f"Atendente {id} não encontrado."
        )

    def utilizacoes_do_atendente(self, id: str) -> list[Utilizacao]:
        self.localizar_atendente(id)

        historico = []

        for utilizacao in self.__utilizacoes:
            participou_entrega = (
                utilizacao.atendente_entrega is not None and 
                utilizacao.atendente_entrega.id == id
            )

            participou_devolucao = (
                utilizacao.atendente_devolucao is not None and 
                utilizacao.atendente_devolucao.id == id
            )

            if participou_entrega or participou_devolucao:
                historico.append(utilizacao)

        return historico

    # ---------------- TOALHAS ----------------

    def cadastrar_toalha(self, id: str) -> Toalha:
        for toalha in self.__toalhas:
            if toalha.id == id:
                raise NadoLivreError(f"A toalha com ID {id} já está cadastrada.")
        toalha = Toalha(id)
        self.__toalhas.append(toalha)
        return toalha

    def listar_toalhas(self) -> list[Toalha]:
        return self.__toalhas

    def localizar_toalha(self, id: str) -> Toalha:
        for toalha in self.__toalhas:
            if toalha.id == id:
                return toalha

        raise ToalhaNaoEncontradaError(
            f"Toalha {id} não encontrada."
        )

    def consultar_toalhas_disponiveis(self) -> list[Toalha]:
        toalhas = []

        for toalha in self.__toalhas:
            if not toalha.em_uso:
                toalhas.append(toalha)

        return toalhas

    def consultar_toalhas_em_uso(self) -> list[Toalha]:
        toalhas = []

        for toalha in self.__toalhas:
            if toalha.em_uso:
                toalhas.append(toalha)

        return toalhas

    # ---------------- UTILIZAÇÕES ----------------

    def registrar_retirada(
        self,
        nadador_id: str,
        toalha_id: str,
        atendente_id: str
    ) -> Utilizacao:

        nadador = self.localizar_nadador(nadador_id)
        toalha = self.localizar_toalha(toalha_id)
        atendente = self.localizar_atendente(atendente_id)

        toalha.utilizar()

        utilizacao = Utilizacao(
            nadador,
            toalha,
            atendente
        )

        nadador.adicionar_utilizacao(utilizacao)
        atendente.adicionar_utilizacao(utilizacao)

        self.__utilizacoes.append(utilizacao)

        return utilizacao

    def localizar_utilizacao_aberta(
        self,
        toalha_id: str
    ) -> Utilizacao:

        toalha = self.localizar_toalha(toalha_id)

        for utilizacao in self.__utilizacoes:
            if (
                utilizacao.toalha == toalha
                and utilizacao.aberta
            ):
                return utilizacao

        raise UtilizacaoNaoEncontradaError(
            f"Não existe utilização aberta para a toalha {toalha_id}."
        )

    def registrar_devolucao(
        self,
        toalha_id: str,
        atendente_id: str
    ) -> None:

        utilizacao = self.localizar_utilizacao_aberta(toalha_id)
        atendente = self.localizar_atendente(atendente_id)

        utilizacao.encerrar(atendente)

    def listar_utilizacoes(self) -> list[Utilizacao]:
        return self.__utilizacoes

    def consultar_historico(self) -> list[Utilizacao]:
        return self.__utilizacoes

    def listar_utilizacoes_abertas(self) -> list[Utilizacao]:
        abertas = []
        for utilizacao in self.__utilizacoes:
            if utilizacao.aberta:
                abertas.append(utilizacao)
        return abertas
