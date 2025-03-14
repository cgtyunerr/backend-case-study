"""Alembic environment."""

import asyncio

from alembic import context
from sqlalchemy import pool, text
from sqlalchemy.ext.asyncio import create_async_engine

from app.monorepo.settings import settings
from app.monorepo import LedgerBaseModel
from app.travelai.models import TravelAILedgerEntryModel

config = context.config

target_metadata = LedgerBaseModel.metadata


def do_run_migrations(connection):

    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        version_table_schema="travelai",
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_async_engine(
        settings.DB.db_url.unicode_string(),
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.execute(text("CREATE SCHEMA IF NOT EXISTS travelai"))
        await connection.commit()
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


asyncio.run(run_migrations_online())
