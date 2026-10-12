from modelos.nadador import Nadador
from modelos.toalha import Toalha
from modelos.atendente import Atendente
from nado_livre_ import NadoLivre
from modelos.utilizacao import Utilizacao
from excecoes.NadoLivreError import NadoLivreError


class UtilizacaoService:
    """
    Serviço responsável por coordenar empréstimos e devoluções de toalhas,
    garantindo a aplicação das regras de negócio.
    """

    def __init__(self, aplicacao: NadoLivre) -> None:
        self._aplicacao = aplicacao

    def registrar_retirada(
        self,
        toalha_id: int,
        nadador_id: int,
        atendente_id: int
    ) -> Utilizacao:
        """Registra a retirada de uma toalha validando as regras de negócio."""

        toalha_id = int(toalha_id)
        nadador_id = int(nadador_id)
        atendente_id = int(atendente_id)

        # Localiza a toalha
        toalha = None
        for t in self._aplicacao.obter_toalhas():
            if int(t.id) == toalha_id:
                toalha = t
                break

        if toalha is None:
            raise NadoLivreError(
                f"Toalha com ID {toalha_id} não encontrada."
            )

        # Localiza o nadador
        nadador = None
        for n in self._aplicacao.obter_nadadores():
            if int(n.id) == nadador_id:
                nadador = n
                break

        if nadador is None:
            raise NadoLivreError(
                f"Nadador com ID {nadador_id} não encontrado."
            )

        # Localiza o atendente responsável pela entrega
        atendente = None
        for a in self._aplicacao.obter_atendentes():
            if int(a.id) == atendente_id:
                atendente = a
                break

        if atendente is None:
            raise NadoLivreError(
                f"Atendente com ID {atendente_id} não encontrado."
            )

        # Verifica se a toalha já está emprestada
        if toalha.em_uso:
            raise NadoLivreError(
                f"A toalha ID {toalha_id} já está em uso."
            )

        # Marca a toalha como ocupada
        toalha.utilizar()

        # Cria e registra a utilização
        nova_utilizacao = Utilizacao(nadador, toalha, atendente)

        self._aplicacao.adicionar_utilizacao(nova_utilizacao)

        # Atualiza os históricos do nadador e do atendente
        nadador.adicionar_utilizacao(nova_utilizacao)
        atendente.adicionar_utilizacao(nova_utilizacao)

        # Persiste o estado atualizado da toalha e da utilização
        self._aplicacao.salvar_dados()

        return nova_utilizacao

    def registrar_devolucao(
        self,
        toalha_id: int,
        atendente_id: int
    ) -> Utilizacao:
        """Registra a devolução de uma toalha que está em uso."""

        toalha_id = int(toalha_id)
        atendente_id = int(atendente_id)

        # Localiza a utilização em aberto da toalha
        utilizacao_encontrada = None

        for u in self._aplicacao.obter_utilizacoes():
            if int(u.toalha.id) == toalha_id and u.aberta:
                utilizacao_encontrada = u
                break

        if utilizacao_encontrada is None:
            raise NadoLivreError(
                f"Não há empréstimo em aberto para a toalha ID {toalha_id}."
            )

        # Localiza o atendente responsável pela devolução
        atendente = None

        for a in self._aplicacao.obter_atendentes():
            if int(a.id) == atendente_id:
                atendente = a
                break

        if atendente is None:
            raise NadoLivreError(
                f"Atendente com ID {atendente_id} não encontrado."
            )

        # Guarda o atendente que realizou a entrega
        atendente_entrega = utilizacao_encontrada.atendente_entrega

        # Encerra a utilização e libera a toalha
        utilizacao_encontrada.encerrar(atendente)

        # Atualiza o histórico do atendente da devolução,
        # sem duplicar o registro se ele também fez a entrega
        if atendente is not atendente_entrega:
            atendente.adicionar_utilizacao(utilizacao_encontrada)

        # Salva a devolução e o novo estado da toalha
        self._aplicacao.salvar_dados()

        return utilizacao_encontrada

    def _localizar_nadador(self, identificador: int) -> Nadador:
        """Localiza um nadador pelo ID."""
        for n in self._aplicacao.obter_nadadores():
            if int(n.id) == int(identificador):
                return n

        raise NadoLivreError(
            f"Nadador {identificador} não encontrado."
        )

    def _localizar_toalha(self, identificador: int) -> Toalha:
        """Localiza uma toalha pelo ID."""
        for t in self._aplicacao.obter_toalhas():
            if int(t.id) == int(identificador):
                return t

        raise NadoLivreError(
            f"Toalha {identificador} não encontrada."
        )

    def _localizar_atendente(self, identificador: int) -> Atendente:
        """Localiza um atendente pelo ID."""
        for a in self._aplicacao.obter_atendentes():
            if int(a.id) == int(identificador):
                return a

        raise NadoLivreError(
            f"Atendente {identificador} não encontrado."
        )
    