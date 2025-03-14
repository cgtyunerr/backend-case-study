"""Add data module."""

from datetime import datetime

from app.healthai.models import HealthAILedgerEntryModel
from app.healthai.schemas import HealthAILedgerOperation
from app.monorepo.core import database_session_manager
from app.travelai.models import TravelAILedgerEntryModel
from app.travelai.schemas import TravelAILedgerOperation


class AddData:
    """Add data."""

    @staticmethod
    async def add_ledger_entry_health_ai():
        """Add ledger entry to healthai."""
        async with database_session_manager.get_session() as session:
            new_entry = HealthAILedgerEntryModel(
                operation=HealthAILedgerOperation.SIGNUP_CREDIT,
                amount=3,
                nonce="entry1",
                owner_id="1",
                created_on=datetime.now(),
            )
            new_entry1 = HealthAILedgerEntryModel(
                operation=HealthAILedgerOperation.DAILY_REWARD,
                amount=1,
                nonce="entry2",
                owner_id="1",
                created_on=datetime.now(),
            )
            session.add(new_entry)
            session.add(new_entry1)
            await session.commit()

    @staticmethod
    async def add_ledger_entry_travel_ai():
        """Add ledger entry to travelai."""
        async with database_session_manager.get_session() as session:
            new_entry = TravelAILedgerEntryModel(
                operation=TravelAILedgerOperation.SIGNUP_CREDIT,
                amount=3,
                nonce="entry1",
                owner_id="1",
                created_on=datetime.now(),
            )
            new_entry1 = TravelAILedgerEntryModel(
                operation=TravelAILedgerOperation.DAILY_REWARD,
                amount=1,
                nonce="entry2",
                owner_id="1",
                created_on=datetime.now(),
            )
            session.add(new_entry)
            session.add(new_entry1)
            await session.commit()
