from typing import List, TYPE_CHECKING

from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import Base

if TYPE_CHECKING:
    from src.apps.standards.models.functions import Function
    from src.apps.standards.models.standards import Standard


class Extension(Base):
    __tablename__ = "extensions"

    name: Mapped[str] = mapped_column(String(100), unique=True)
    standard_id: Mapped[int] = mapped_column(
        ForeignKey(
            "standards.id",
            ondelete="CASCADE",
        ),
        nullable=True,
        default=None,
    )
    standard: Mapped["Standard"] = relationship(
        back_populates="extensions",
    )
    functions: Mapped[List["Function"]] = relationship(
        secondary="function__extension",
        back_populates="extension",
    )
    is_parsed: Mapped[bool] = mapped_column(Boolean, default=False)


class FunctionExtensionSecondary(Base):
    __tablename__ = "function__extension"

    function_id: Mapped[int] = mapped_column(
        ForeignKey(
            "functions.id",
            ondelete="CASCADE",
        ),
    )
    extension_id: Mapped[int] = mapped_column(
        ForeignKey(
            "extensions.id",
            ondelete="CASCADE",
        ),
    )
