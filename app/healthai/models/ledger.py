"""HealthAI orm model."""

from typing import Annotated

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.healthai import HealthAILedgerOperation
from app.monorepo import LedgerBaseModel


class HealthAILedgerEntryModel(LedgerBaseModel):
    """HealthAI ledger entry orm model."""

    __tablename__ = "ledger_entries"

    operation: Mapped[
        Annotated[HealthAILedgerOperation, mapped_column(Enum, nullable=False)]
    ]
