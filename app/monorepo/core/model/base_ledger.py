"""Ledger orm model."""

from sqlalchemy.orm import as_declarative, Mapped

from .mixin import text, integer, unique_text, IdMixin, CreatedAtMixin


@as_declarative()
class LedgerBaseModel(IdMixin, CreatedAtMixin):
    """Ledger model."""

    amount: Mapped[integer]
    nonce: Mapped[unique_text]
    owner_id: Mapped[text]
