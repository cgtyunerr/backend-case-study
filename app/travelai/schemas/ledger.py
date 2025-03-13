"""TravelAI ledger operation schemas."""

from app.monorepo import BaseLedgerOperation, CreateTransactionBaseModel


class TravelAILedgerOperation(BaseLedgerOperation):
    """TravelAI ledger operation schema."""

    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"


class CreateTransactionModel(CreateTransactionBaseModel):
    """Create transaction model.

    ledger_operation: The type of ledger operation.
    """

    ledger_operation: TravelAILedgerOperation
