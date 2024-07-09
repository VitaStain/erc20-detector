from typing import List, TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import Base

if TYPE_CHECKING:
    from src.apps.contracts.models.contracts import Contract
    from src.apps.standards.models.functions import Function


class Standard(Base):
    __tablename__ = "standards"

    name: Mapped[str] = mapped_column(String(100))
    contracts: Mapped[List["Contract"]] = relationship(
        secondary="standard__contract",
        back_populates="standards",
    )
    functions: Mapped[List["Function"]] = relationship(
        secondary="function__contract",
        back_populates="standards",
    )


class ContractStandardSecondary(Base):
    __tablename__ = "contract__standard"

    contract_id: Mapped[int] = mapped_column(
        ForeignKey(
            "contracts.id",
            ondelete="CASCADE",
        ),
    )
    standard_id: Mapped[int] = mapped_column(
        ForeignKey(
            "standards.id",
            ondelete="CASCADE",
        ),
    )


class FunctionStandardSecondary(Base):
    __tablename__ = "function__standard"

    function_id: Mapped[int] = mapped_column(
        ForeignKey(
            "functions.id",
            ondelete="CASCADE",
        ),
    )
    standard_id: Mapped[int] = mapped_column(
        ForeignKey(
            "standards.id",
            ondelete="CASCADE",
        ),
    )