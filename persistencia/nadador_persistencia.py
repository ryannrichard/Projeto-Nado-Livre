import json
import os

from modelos.nadador import Nadador


class NadadorPersistencia:

    def __init__(self, arquivo):
        self.__arquivo = arquivo

    def salvar(self, nadadores):

        self.__criar_diretorio()

        dados = []

        for nadador in nadadores:
            dados.append({
                "id": nadador.id,
                "nome": nadador.nome
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

        nadadores = []

        for item in dados:

            nadador = Nadador(
                item["nome"],
                item["id"]
            )

            nadadores.append(nadador)

        return nadadores

    def __criar_diretorio(self):

        diretorio = os.path.dirname(
            self.__arquivo
        )

        if diretorio:
            os.makedirs(
                diretorio,
                exist_ok=True
            )