import json
import os

from modelos.atendente import Atendente


class AtendentePersistencia:

    def __init__(self, arquivo):
        self.__arquivo = arquivo

    def salvar(self, atendentes):
        self.__criar_diretorio()

        dados = []

        for atendente in atendentes:
            dados.append({
                "id": atendente.id,
                "nome": atendente.nome
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

    def carregar(self):
        if not os.path.exists(self.__arquivo):
            return []

        with open(
            self.__arquivo,
            "r",
            encoding="utf-8"
        ) as arquivo:
            dados = json.load(arquivo)

        atendentes = []

        for item in dados:
            atendente = Atendente(
                item["nome"],
                item["id"]
            )

            atendentes.append(atendente)

        return atendentes

    def __criar_diretorio(self):
        diretorio = os.path.dirname(
            self.__arquivo
        )

        if diretorio:
            os.makedirs(
                diretorio,
                exist_ok=True
            )