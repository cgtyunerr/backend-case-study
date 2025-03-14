"""Pytest configurations."""

from typing import AsyncGenerator

from fastapi.testclient import TestClient
import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.healthai.src.api.main import api as health_api
from app.monorepo.settings import settings
from app.monorepo.core.db.session.session import DatabaseSessionManager


@pytest.fixture(scope="function")
async def session() -> AsyncGenerator[AsyncSession, None]:
    database_session_manager: DatabaseSessionManager = DatabaseSessionManager(
        str(settings.DB.db_url)
    )
    async with database_session_manager.get_session() as session:
        yield session


@pytest.fixture(scope="session")
def health_client():
    with TestClient(health_api) as client:
        yield client
