"""Ledger orm model."""

from sqlalchemy.orm import Mapped

from .base import Base
from .mixin import text, integer


class LedgerBaseModel(Base):
    """Ledger model."""

    amount: Mapped[integer]
    nonce: Mapped[text]
    owner_id: Mapped[text]
