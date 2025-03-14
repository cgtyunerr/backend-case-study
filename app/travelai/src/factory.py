"""TravelAI service factory module."""

from functools import lru_cache

from app.travelai.src.ledgers import LEDGER_OPERATION_CONFIG
from app.travelai.models import TravelAILedgerEntryModel
from app.monorepo.core.db.ledger_repository import LedgerRepository
from app.monorepo.core.ledgers.services import BaseLedgerService
from app.travelai.schemas import CreateTransactionModel


class TravelAIRepository(
    LedgerRepository[TravelAILedgerEntryModel, CreateTransactionModel]
):
    """TravelAI repository."""

    model = TravelAILedgerEntryModel
    schema = CreateTransactionModel


class Factory:
    """Service factory class."""

    @staticmethod
    @lru_cache(maxsize=1)
    def create_ledger_service() -> BaseLedgerService:
        """Create BaseLedgerService."""
        return BaseLedgerService[CreateTransactionModel](
            ledger_repository=TravelAIRepository(),
            ledger_operation_config=LEDGER_OPERATION_CONFIG,
        )
