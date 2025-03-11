"""Core ledger repository module."""

from typing import Sequence

from pydantic import BaseModel, ConfigDict, InstanceOf, validate_call
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.monorepo import LedgerBaseModel


class LedgerRepository(BaseModel):
    """Core ledger repository module."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @validate_call
    async def get_all(
        self, session: InstanceOf[AsyncSession]
    ) -> Sequence[LedgerBaseModel]:
        """Get all the entities.

        Arguments:
            session: db session.

        Return:
            All the ledger entities.
        """
        result = await session.execute(select(LedgerBaseModel))
        ledger_entities = result.scalars().all()
        return ledger_entities

    async def get(self):
        """Get a entity."""

    async def update(self):
        """Update a db row."""

    async def delete(self):
        """Delete a db row."""
