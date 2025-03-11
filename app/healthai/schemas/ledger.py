"""HealthAI schemas."""

from app.monorepo import BaseLedgerOperation


class HealthAILedgerOperation(BaseLedgerOperation):
    """HealthAI ledger operation schema."""

    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"
