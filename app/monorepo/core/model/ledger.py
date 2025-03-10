"""Ledger orm model."""

from sqlalchemy.orm import Mapped

from .base import Base
from .mixin import text, integer


class LedgerModel(Base):
    """Ledger model."""

    amount: Mapped[integer]
    nonce: Mapped[text]
    owner_id: Mapped[text]
