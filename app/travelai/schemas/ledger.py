"""TravelAI ledger operation schemas."""

from app.monorepo import BaseLedgerOperation


class TravelAILedgerOperation(BaseLedgerOperation):
    """TravelAI ledger operation schema."""

    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"
