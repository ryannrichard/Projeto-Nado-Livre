class Tela:
    """Classe base para todas as telas do sistema."""
    
    def titulo(self, texto: str) -> None:
        print(f"\n===== {texto} =====")

    def pausar(self) -> None:
        """Pausa a execução até o usuário apertar Enter."""
        input("\nPressione Enter para continuar...")