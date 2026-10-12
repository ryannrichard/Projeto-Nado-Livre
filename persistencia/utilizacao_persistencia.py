import json
import os


class UtilizacaoPersistencia:

    def __init__(self, arquivo):
        self.__arquivo = arquivo

    def salvar(self, utilizacoes):
        self.__criar_diretorio()

        dados = []

        for utilizacao in utilizacoes:
            dados.append({
                "nadador_id": utilizacao.nadador.id,
                "toalha_id": utilizacao.toalha.id,
                "atendente_entrega_id": (
                    utilizacao.atendente_entrega.id
                ),
                "atendente_devolucao_id": (
                    utilizacao.atendente_devolucao.id
                    if utilizacao.atendente_devolucao is not None
                    else None
                ),
                "aberta": utilizacao.aberta
            })

        with open(
            self.__arquivo,
            "w",
            encoding="utf-8"
        ) as arquivo:
            json.dump(
                dados,
                arquivo,
                ensure_ascii=False,
                indent=4
            )

    def carregar(
        self,
        nadadores,
        toalhas,
        atendentes
    ):
        from modelos.utilizacao import Utilizacao

        if not os.path.exists(self.__arquivo):
            return []

        with open(
            self.__arquivo,
            "r",
            encoding="utf-8"
        ) as arquivo:
            dados = json.load(arquivo)

        # Cria índices para localizar os objetos existentes.
        nadadores_por_id = {
            nadador.id: nadador
            for nadador in nadadores
        }

        toalhas_por_id = {
            toalha.id: toalha
            for toalha in toalhas
        }

        atendentes_por_id = {
            atendente.id: atendente
            for atendente in atendentes
        }

        utilizacoes = []

        for item in dados:
            nadador = nadadores_por_id[item["nadador_id"]]
            toalha = toalhas_por_id[item["toalha_id"]]
            atendente_entrega = atendentes_por_id[
                item["atendente_entrega_id"]
            ]

            utilizacao = Utilizacao(
                nadador,
                toalha,
                atendente_entrega
            )

            if not item["aberta"]:
                atendente_devolucao = atendentes_por_id[
                    item["atendente_devolucao_id"]
                ]
                utilizacao.encerrar(atendente_devolucao)
            else:
                toalha.utilizar()

            # Reconstrói os históricos associados aos objetos.
            nadador.adicionar_utilizacao(utilizacao)
            atendente_entrega.adicionar_utilizacao(utilizacao)

            if utilizacao.atendente_devolucao is not None:
                if (
                    utilizacao.atendente_devolucao
                    is not atendente_entrega
                ):
                    utilizacao.atendente_devolucao.adicionar_utilizacao(
                        utilizacao
                    )

            utilizacoes.append(utilizacao)

        return utilizacoes

    def __criar_diretorio(self):
        diretorio = os.path.dirname(self.__arquivo)

        if diretorio:
            os.makedirs(
                diretorio,
                exist_ok=True
            )