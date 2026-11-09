from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modelos.base import Base

if TYPE_CHECKING:
    from modelos.utilizacao import Utilizacao


class Nadador(Base):
    """
    Representa um nadador cadastrado na escola,
    com foco em armazenar os dados e vincular as utilizações.
    """

    __tablename__ = "nadadores"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    nome: Mapped[str] = mapped_column(String(100))
    bloqueio: Mapped[bool] = mapped_column(default=False)

    utilizacoes: Mapped[list["Utilizacao"]] = relationship(
        back_populates="nadador", lazy="selectin"
    )

    def __init__(self, nome: str, id: int) -> None:
        self.nome = nome
        self.id = id
        self.bloqueio = False

    def __str__(self) -> str:
        return f"Nadador [ID: {self.id} | Nome: {self.nome}]"

    def dados(self) -> str:
        return f"{self.nome} (ID: {self.id})"

    def consultar_utilizacoes(self) -> list["Utilizacao"]:
        """Retorna o histórico de utilizações do nadador."""
        return list(self.utilizacoes)

    def tem_toalha_retirada(self) -> bool:
        """Indica se o nadador possui uma utilização em aberto."""
        return any(utilizacao.aberta for utilizacao in self.utilizacoes)