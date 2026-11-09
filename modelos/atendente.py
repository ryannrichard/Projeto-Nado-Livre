from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modelos.base import Base

if TYPE_CHECKING:
    from modelos.utilizacao import Utilizacao


class Atendente(Base):
    """
    Representa um funcionário responsável pelo controle das toalhas.
    """

    __tablename__ = "atendentes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    nome: Mapped[str] = mapped_column(String(100))

    utilizacoes_entregues: Mapped[list["Utilizacao"]] = relationship(
        back_populates="atendente_entrega",
        foreign_keys="Utilizacao.atendente_entrega_id"
    )
    utilizacoes_devolvidas: Mapped[list["Utilizacao"]] = relationship(
        back_populates="atendente_devolucao",
        foreign_keys="Utilizacao.atendente_devolucao_id"
    )

    def __init__(self, nome: str, id: int) -> None:
        self.nome = nome
        self.id = id

    def __str__(self) -> str:
        return f"Atendente [ID: {self.id} | Nome: {self.nome}]"

    def dados(self) -> str:
        return f"{self.nome} (ID: {self.id})"
