"""Test database."""

import pytest
from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.ext.asyncio import AsyncSession

from app.monorepo.core.db import database_session_manager


class TestDatabase:
    async def test_database(self):
        """Test db for one transaction."""
        async with database_session_manager.get_session() as session:
            assert isinstance(session, AsyncSession)
            await session.execute(
                text("create table databaseconnectiontest (id int primary key)")
            )
            await session.execute(
                text("insert into databaseconnectiontest (id) values (1), (2)")
            )

            check_query = await session.execute(
                text("select id from databaseconnectiontest")
            )

            assert check_query

            await session.execute(text("drop table databaseconnectiontest"))

            with pytest.raises(ProgrammingError):
                await session.execute(text("select id from databaseconnectiontest"))
