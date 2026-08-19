from interface.telas.tela import Tela

class TelaToalhas(Tela):
    """Tela responsável pelas consultas e cadastro de toalhas."""

    def solicitar_cadastro(self) -> str:
        self.titulo("CADASTRO DE TOALHA")
        return input("ID da toalha: ").strip()

    def solicitar_id(self, titulo: str = "CONSULTA DE TOALHA") -> str:
        self.titulo(titulo)
        return input("ID da toalha: ").strip()

    def mostrar_toalhas(self, toalhas, titulo: str = "TOALHAS") -> None:
        self.titulo(titulo)

        if not toalhas:
            print("Nenhuma toalha encontrada.")
            return

        for toalha in toalhas:
            print(f"- {toalha.dados()}")

    def mostrar_responsavel(self, toalha, utilizacao) -> None:
        if toalha is None:
            print("Toalha não encontrada.")
            return

        self.titulo(f"RESPONSÁVEL PELA TOALHA {toalha.id}")

        if utilizacao is None:
            print("A toalha está disponível.")
            return

        print(f"Nadador: {utilizacao.nadador.dados()}")
        print(
            f"Atendente da entrega: "
            f"{utilizacao.atendente_entrega.dados()}"
        )