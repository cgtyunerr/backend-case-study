"""TravelAI ledger operation schemas."""

# from app.monorepo import BaseLedgerOperation


class TravelAILedgerOperation:
    """TravelAI ledger operation schema."""

    # Shared operations
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"

    # App-specific operations
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"
