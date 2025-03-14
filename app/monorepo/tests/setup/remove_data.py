"""Remove data module."""

from app.healthai.models import HealthAILedgerEntryModel
from app.monorepo.core import database_session_manager
from app.travelai.models import TravelAILedgerEntryModel


class RemoveData:
    """Remove data."""

    @staticmethod
    async def remove_ledger_entry_health_ai():
        """Teardown ledger entries from healthai."""
        async with database_session_manager.get_session() as session:
            await session.execute(
                HealthAILedgerEntryModel.delete().where(
                    HealthAILedgerEntryModel.nonce.in_(["entry1", "entry2"])
                )
            )
            await session.commit()

    @staticmethod
    async def remove_ledger_entry_travel_ai():
        """Teardown ledger entries from travelai."""
        async with database_session_manager.get_session() as session:
            await session.execute(
                TravelAILedgerEntryModel.delete().where(
                    TravelAILedgerEntryModel.nonce.in_(["entry1", "entry2"])
                )
            )
            await session.commit()
