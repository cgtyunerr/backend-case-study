"""TravelAI entry orm model."""

from typing import Annotated

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.travelai import TravelAILedgerOperation
from app.monorepo import LedgerBaseModel


class TravelAILedgerEntryModel(LedgerBaseModel):
    """TravelAI ledger entry orm model."""

    # Sqlalchemy model
    __tablename__ = "ledger_entries"

    operation: Mapped[
        Annotated[TravelAILedgerOperation, mapped_column(Enum, nullable=False)]
    ]
