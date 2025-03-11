"""Core schemas."""

import enum


class BaseLedgerOperation(enum.Enum):
    """Base ledger operation enum."""

    @classmethod
    def _include_shared_operation(cls):
        """Include all the shared ledger operations."""
        for name, member in SharedLedgerOperation.__members__.items():
            if name not in cls.__members__:
                cls._member_map_[name] = member

    @classmethod
    def __init_subclass__(cls):
        """Init subclass method."""
        super().__init__()
        cls._include_shared_operation()


class SharedLedgerOperation(BaseLedgerOperation):
    """Shared operation schema."""

    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"
