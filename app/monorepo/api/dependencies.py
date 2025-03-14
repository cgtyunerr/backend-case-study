"""Common api dependencies module."""

from typing import AsyncGenerator, Annotated

from fastapi import Depends, Path
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.monorepo.core.db import database_session_manager


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Get a database session."""
    async with database_session_manager.get_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]


class OwnerIDPathDependency(BaseModel):
    """Event log ID path dependency."""

    owner_id: str = Path(
        description="Owner ID.",
    )
