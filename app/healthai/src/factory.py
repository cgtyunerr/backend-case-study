"""HealthAI service factory module."""

from functools import lru_cache

from app.healthai.src.ledgers import LEDGER_OPERATION_CONFIG
from app.healthai.models import HealthAILedgerEntryModel
from app.monorepo.core.db.ledger_repository import LedgerRepository
from app.monorepo.core.ledgers.services import BaseLedgerService
from app.healthai.schemas import CreateTransactionModel


class HealthAIRepository(
    LedgerRepository[HealthAILedgerEntryModel, CreateTransactionModel]
):
    """HealthAI repository."""

    model = HealthAILedgerEntryModel
    schema = CreateTransactionModel


class Factory:
    """Service factory class."""

    @staticmethod
    @lru_cache(maxsize=1)
    def create_ledger_service() -> BaseLedgerService:
        """Create BaseLedgerService."""
        return BaseLedgerService[CreateTransactionModel](
            ledger_repository=HealthAIRepository(),
            ledger_operation_config=LEDGER_OPERATION_CONFIG,
        )
