"""Core schemas."""

import enum

from pydantic import BaseModel

from app.monorepo.core.commons import extend_enum


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
