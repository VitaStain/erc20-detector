from typing import TYPE_CHECKING

from sqlalchemy import String, Text, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.apps.urils.constants import ContractStatus
from src.models import Base

if TYPE_CHECKING:
    from src.apps.standards.models.standards import Standard


class Contract(Base):
    __tablename__ = "contracts"

    contract_address: Mapped[str] = mapped_column(String(50), unique=True)
    source_code: Mapped[str] = mapped_column(Text)
    is_erc20: Mapped[bool] = mapped_column(Boolean, default=False)
    erc20_version: Mapped[str] = mapped_column(String(50), default=None, nullable=True)
    status: Mapped[ContractStatus] = mapped_column(
        String(20), default=ContractStatus.WAIT_PROCESSING
    )
    standard_id: Mapped[int] = mapped_column(
        ForeignKey(
            "standards.id",
            ondelete="CASCADE",
        )
    )
    standard: Mapped["Standard"] = relationship(
        back_populates="contracts",
    )
