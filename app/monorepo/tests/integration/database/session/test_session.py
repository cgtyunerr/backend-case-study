"""Test session."""

from typing import AsyncGenerator

import pytest
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from app import settings
from app.monorepo.core.db.session.base_session import BaseSessionManager


class SessionManager(BaseSessionManager):
    """Concrete implementation for testing."""

    def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        pass


@pytest.fixture
def base_session_manager() -> SessionManager:
    return SessionManager(database_url=str(settings.DB.db_url))


class TestDatabase:
    async def test_session(self, base_session_manager):
        assert isinstance(base_session_manager.engine, AsyncEngine)
        async with base_session_manager.async_session() as session:
            assert session is not None
