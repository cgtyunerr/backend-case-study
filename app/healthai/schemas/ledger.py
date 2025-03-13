"""HealthAI schemas."""

from enum import Enum

from app.monorepo import BaseLedgerOperation, CreateTransactionBaseModel
from app.monorepo.core.commons import extend_enum


@extend_enum(BaseLedgerOperation)
class HealthAILedgerOperation(Enum):
    """HealthAI ledger operation schema."""

    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"


class CreateTransactionModel(CreateTransactionBaseModel):
    """Create transaction model.

    ledger_operation: The type of ledger operation.
    """

    ledger_operation: HealthAILedgerOperation
