from typing import List, TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import Base

if TYPE_CHECKING:
    from src.apps.standards.models.standards import Standard
    from src.apps.standards.models.extensions import Extension


class Function(Base):
    __tablename__ = "functions"

    name: Mapped[str] = mapped_column(String(100))
    standard: Mapped[List["Standard"]] = relationship(
        secondary="function__standard",
        back_populates="functions",
    )
    extension: Mapped[List["Extension"]] = relationship(
        secondary="function__extension",
        back_populates="functions",
    )
