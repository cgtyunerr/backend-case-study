"""TravelAI entry orm model."""

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import ENUM

from app.travelai import TravelAILedgerOperation
from app.monorepo import LedgerBaseModel


class TravelAILedgerEntryModel(LedgerBaseModel):
    """TravelAI ledger entry orm model."""

    # Sqlalchemy model
    __tablename__ = "ledger_entries"

    operation = Column(
        ENUM(TravelAILedgerOperation, name="travelai_ledger_operation"), nullable=False
    )
