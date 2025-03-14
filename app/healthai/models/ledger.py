"""HealthAI orm model."""

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import ENUM

from app.healthai import HealthAILedgerOperation
from app.monorepo import LedgerBaseModel


class HealthAILedgerEntryModel(LedgerBaseModel):
    """HealthAI ledger entry orm model."""

    __tablename__ = "ledger_entries"
    __table_args__ = {"schema": "healthai"}

    operation = Column(
        ENUM(HealthAILedgerOperation, name="healthai_ledger_operation"), nullable=False
    )
