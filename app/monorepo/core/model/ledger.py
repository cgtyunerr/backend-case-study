"""Ledger orm model."""

from sqlalchemy.orm import Mapped

from .base import Base
from .mixin import text, integer, unique_text


class LedgerBaseModel(Base):
    """Ledger model."""

    amount: Mapped[integer]
    nonce: Mapped[unique_text]
    owner_id: Mapped[text]
