"""HealthAI orm model."""


class HealthAILedgerEntryModel:
    """HealthAI ledger entry orm model."""

    # Sqlalchemy model

    __tablename__ = "ledger_entries"

    # operation:  # What type should this be? Note: It should not be str.
