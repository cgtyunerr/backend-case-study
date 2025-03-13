"""Core schemas."""

import enum

from pydantic import BaseModel


def extend_enum(inherited_enum):
    """Extend enum decorator."""

    def wrapper(added_enum):
        """Extend enum method."""
        joined = {}
        for item in inherited_enum:
            joined[item.name] = item.value
        for item in added_enum:
            joined[item.name] = item.value
        return enum.Enum(added_enum.__name__, joined)

    return wrapper


class SharedLedgerOperation(enum.Enum):
    """Shared operation schema."""

    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"


@extend_enum(SharedLedgerOperation)
class BaseLedgerOperation(enum.Enum):
    """Base ledger operation enum."""

    pass


class CreateTransactionBaseModel(BaseModel):
    """Create transaction base model.

    owner_id: Owner id.
    nonce: unique string.
    """

    owner_id: str
    nonce: str
