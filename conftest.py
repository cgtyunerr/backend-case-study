"""Pytest configurations."""

from typing import AsyncGenerator

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.monorepo.settings import settings
from app.monorepo.core.db.session.session import DatabaseSessionManager


@pytest.fixture(scope="function")
async def session() -> AsyncGenerator[AsyncSession, None]:
    database_session_manager: DatabaseSessionManager = DatabaseSessionManager(
        str(settings.DB.db_url)
    )
    async with database_session_manager.get_session() as session:
        yield session
