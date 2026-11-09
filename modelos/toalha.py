from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from modelos.base import Base

if TYPE_CHECKING:
    from modelos.utilizacao import Utilizacao


class Toalha(Base):
    """
    Representa uma toalha disponibilizada pela escola.
    """

    __tablename__ = "toalhas"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    _em_uso: Mapped[bool] = mapped_column("em_uso", default=False)

    utilizacoes: Mapped[list["Utilizacao"]] = relationship(
        back_populates="toalha"
    )

    def __init__(self, id: int) -> None:
        self.id = id
        self._em_uso = False

    @property
    def em_uso(self) -> bool:
        return self._em_uso

    def utilizar(self) -> None:
        """Marca a toalha como em uso."""
        self._em_uso = True

    def disponibilizar(self) -> None:
        """Marca a toalha como disponível."""
        self._em_uso = False

    def dados(self) -> str:
        estado = "Em uso" if self._em_uso else "Disponível"
        return f"Toalha {self.id} - {estado}"