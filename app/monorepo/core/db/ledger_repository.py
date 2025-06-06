"""Core ledger repository module."""

from typing import Generic, Type, TypeVar

from pydantic import ConfigDict, InstanceOf, validate_call
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.monorepo import (
    LedgerBaseModel,
    NotFoundError,
    InvalidInputError,
    CreateTransactionBaseModel,
)


T = TypeVar("T", bound=LedgerBaseModel)
G = TypeVar("G", bound=CreateTransactionBaseModel)


class LedgerRepository(Generic[T, G]):
    """Core ledger repository module."""

    model: Type[T]
    schema: Type[G]
    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    @validate_call
    async def get_current_balance_by_owner_id(
        cls, owner_id: str, session: InstanceOf[AsyncSession]
    ) -> int:
        """Get a entity.

        Arguments:
            session: db session.
            owner_id: owner id.

        Return:
            Ledger entities about owner.

        Raises:
            NotFoundError.
        """
        result = await session.execute(
            select(func.sum(cls.model.amount)).filter(cls.model.owner_id == owner_id)
        )
        current_balance: int = result.scalar()
        if current_balance is None:
            raise NotFoundError("There has no any ledger record about the owner.")

        return current_balance

    @classmethod
    @validate_call
    async def add(
        cls, session: InstanceOf[AsyncSession], amount: int, create_model: G
    ) -> int:
        """Add a ledger transaction.

        Arguments:
            session: db session.
            amount: amount.
            create_model: create model.

        Return:
            Id of the new entity.

        Raises:
            InvalidInputError: If the nonce values are conflict.
        """
        try:
            current_balance = await cls.get_current_balance_by_owner_id(
                owner_id=create_model.owner_id, session=session
            )
        except NotFoundError:
            current_balance = 0

        if current_balance + amount >= 0:
            new_entry: cls.model = cls.model(**create_model.model_dump())  # type:ignore
            new_entry.amount = amount
            session.add(new_entry)
            try:
                await session.commit()
                await session.refresh(new_entry)
            except IntegrityError:
                await session.rollback()
                raise InvalidInputError("This transaction was already happened.")

            return new_entry.id
        else:
            raise InvalidInputError("Insufficient balance.")
