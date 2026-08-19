from abc import ABC, abstractmethod

class Menu(ABC):
    """
    Classe abstrata base para todos os menus do sistema Nado Livre.
    Garante a padronização e a separação de responsabilidades na interface.
    """

    @abstractmethod
    def executar(self) -> None:
        pass