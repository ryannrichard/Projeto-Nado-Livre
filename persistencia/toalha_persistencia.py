import json
import os

from modelos.toalha import Toalha


class ToalhaPersistencia:

    def __init__(self, arquivo):
        self.__arquivo = arquivo

    def salvar(self, toalhas):
        self.__criar_diretorio()

        dados = []

        for toalha in toalhas:
            dados.append({
                "id": toalha.id,
                "em_uso": toalha.em_uso
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

        toalhas = []

        for item in dados:
            toalha = Toalha(item["id"])

            if item["em_uso"]:
                toalha.utilizar()

            toalhas.append(toalha)

        return toalhas

    def __criar_diretorio(self):
        diretorio = os.path.dirname(
            self.__arquivo
        )

        if diretorio:
            os.makedirs(
                diretorio,
                exist_ok=True
            )