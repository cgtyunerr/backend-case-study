"""Base ledger service module."""

from typing import TypeVar, Generic, Dict

from pydantic import validate_call, InstanceOf, ConfigDict
from sqlalchemy.ext.asyncio import AsyncSession

from app.monorepo import CreateTransactionBaseModel, InvalidInputError
from app.monorepo.core.db.ledger_repository import LedgerRepository

T = TypeVar("T", bound=CreateTransactionBaseModel)


class BaseLedgerService(Generic[T]):
    """Base ledger service."""

    ledger_repository: LedgerRepository
    ledger_operation_config: Dict[str, int]
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __init__(
        self,
        ledger_repository: LedgerRepository,
        ledger_operation_config: Dict[str, int],
    ):
        """Initialize Ledger Repository."""
        super().__init__()
        self.ledger_repository = ledger_repository
        self.ledger_operation_config = ledger_operation_config

    @validate_call
    async def get_current_balance(
        self, owner_id: str, session: InstanceOf[AsyncSession]
    ) -> int:
        """Get current balance.

        Arguments:
            owner_id: related owner id.
            session: db session.

        Return:
            current balance.
        """
        return await self.ledger_repository.get_current_balance_by_owner_id(
            owner_id=owner_id, session=session
        )

    @validate_call
    async def add_entity(
        self, session: InstanceOf[AsyncSession], create_model: T
    ) -> int:
        """Add new entity.

        Arguments:
            session: db session.
            create_model: create model.

        Raises:
            InvalidInputError: If operation not in config.
        """
        try:
            amount: int = self.ledger_operation_config[
                create_model.operation.value  # type: ignore
            ]
        except KeyError:
            raise InvalidInputError("Operation not found.")

        return await self.ledger_repository.add(
            session=session, create_model=create_model, amount=amount
        )
