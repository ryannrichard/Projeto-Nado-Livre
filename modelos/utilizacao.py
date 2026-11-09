from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from modelos.base import Base
from excecoes.utilizacao_encerrada_error import UtilizacaoEncerradaError

if TYPE_CHECKING:
    from modelos.atendente import Atendente
    from modelos.nadador import Nadador
    from modelos.toalha import Toalha


class Utilizacao(Base):
    """
    Representa a utilização de uma toalha por um nadador,
    incluindo sua entrega e posterior devolução.
    """

    __tablename__ = "utilizacoes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nadador_id: Mapped[int] = mapped_column(ForeignKey("nadadores.id"))
    toalha_id: Mapped[int] = mapped_column(ForeignKey("toalhas.id"))
    atendente_entrega_id: Mapped[int] = mapped_column(
        ForeignKey("atendentes.id")
    )
    atendente_devolucao_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("atendentes.id"), nullable=True
    )
    aberta: Mapped[bool] = mapped_column(default=True)

    nadador: Mapped["Nadador"] = relationship(
        back_populates="utilizacoes", lazy="selectin"
    )
    toalha: Mapped["Toalha"] = relationship(
        back_populates="utilizacoes", lazy="selectin"
    )
    atendente_entrega: Mapped["Atendente"] = relationship(
        back_populates="utilizacoes_entregues",
        foreign_keys=[atendente_entrega_id],
        lazy="selectin",
    )
    atendente_devolucao: Mapped[Optional["Atendente"]] = relationship(
        back_populates="utilizacoes_devolvidas",
        foreign_keys=[atendente_devolucao_id],
        lazy="selectin",
    )

    def __init__(
        self,
        nadador: "Nadador",
        toalha: "Toalha",
        atendente_entrega: "Atendente",
    ) -> None:
        self.nadador = nadador
        self.toalha = toalha
        self.atendente_entrega = atendente_entrega
        self.aberta = True

    def encerrar(self, atendente: "Atendente") -> None:
        """Encerra a utilização e libera a toalha."""
        if not self.aberta:
            raise UtilizacaoEncerradaError("A utilização já está encerrada.")

        self.atendente_devolucao = atendente
        self.aberta = False
        self.toalha.disponibilizar()

    def dados(self) -> str:
        estado = "Aberta" if self.aberta else "Encerrada"

        return (
            f"Nadador: {self.nadador.nome} | "
            f"Toalha: {self.toalha.id} | "
            f"Entrega: {self.atendente_entrega.nome} | "
            f"Estado: {estado}"
        )