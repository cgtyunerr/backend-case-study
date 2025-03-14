"""Ledger repository unit test package."""

import pytest
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.healthai.models import HealthAILedgerEntryModel
from app.healthai.schemas import (
    CreateTransactionModel as HealthAICreate,
    HealthAILedgerOperation,
)
from app.monorepo.core.commons import NotFoundError, InvalidInputError
from app.monorepo.core.db.ledger_repository import LedgerRepository
from app.travelai.models import TravelAILedgerEntryModel
from app.travelai.schemas import (
    CreateTransactionModel as TravelAICreate,
    TravelAILedgerOperation,
)


class HealthAIRepository(LedgerRepository[HealthAILedgerEntryModel, HealthAICreate]):
    model = HealthAILedgerEntryModel
    schema = HealthAICreate


class TravelAIRepository(LedgerRepository[HealthAILedgerEntryModel, HealthAICreate]):
    model = TravelAILedgerEntryModel
    schema = TravelAICreate


@pytest.fixture
def ledger_repository_healthai() -> LedgerRepository:
    return HealthAIRepository()


@pytest.fixture
def ledger_repository_travelai() -> LedgerRepository:
    return TravelAIRepository()


travel_ai_create_model1: TravelAICreate = TravelAICreate(
    owner_id="1", nonce="create1", operation=TravelAILedgerOperation.DAILY_REWARD
)

health_ai_create_model1: HealthAICreate = HealthAICreate(
    owner_id="1", nonce="create1", operation=HealthAILedgerOperation.DAILY_REWARD
)

health_ai_create_model2: HealthAICreate = HealthAICreate(
    owner_id="2", nonce="create1", operation=HealthAILedgerOperation.DAILY_REWARD
)

health_ai_create_model3: HealthAICreate = HealthAICreate(
    owner_id="1", nonce="entry1", operation=HealthAILedgerOperation.DAILY_REWARD
)


class TestCurrentBalanceByOwnerId:
    async def test_current_balance_healthai(
        self, session: AsyncSession, ledger_repository_healthai: LedgerRepository
    ):
        balance: int = await ledger_repository_healthai.get_current_balance_by_owner_id(
            session=session, owner_id="1"
        )
        assert balance == 4

    async def test_not_found_error(
        self, session: AsyncSession, ledger_repository_healthai: LedgerRepository
    ):
        with pytest.raises(NotFoundError) as error:
            await ledger_repository_healthai.get_current_balance_by_owner_id(
                session=session, owner_id="2"
            )
        assert str(error.value) == "There has no any ledger record about the owner."

    async def test_current_balance_travelai(
        self, session: AsyncSession, ledger_repository_travelai: LedgerRepository
    ):
        balance: int = await ledger_repository_travelai.get_current_balance_by_owner_id(
            session=session, owner_id="1"
        )
        assert balance == 4


class TestAddLedgerEntry:
    async def test_add_entry_health_ai(
        self, session: AsyncSession, ledger_repository_healthai: LedgerRepository
    ):
        try:
            await ledger_repository_healthai.add(
                session=session, amount=3, create_model=health_ai_create_model1
            )
        finally:
            await session.execute(
                delete(HealthAILedgerEntryModel).where(
                    HealthAILedgerEntryModel.nonce == health_ai_create_model1.nonce
                )
            )
            await session.commit()

    async def test_add_entry_travel_ai(
        self, session: AsyncSession, ledger_repository_travelai: LedgerRepository
    ):
        try:
            await ledger_repository_travelai.add(
                session=session, amount=3, create_model=travel_ai_create_model1
            )
        finally:
            await session.execute(
                delete(TravelAILedgerEntryModel).where(
                    TravelAILedgerEntryModel.nonce == travel_ai_create_model1.nonce
                )
            )
            await session.commit()

    async def test_add_new_user_entry(
        self, session: AsyncSession, ledger_repository_healthai: LedgerRepository
    ):
        try:
            await ledger_repository_healthai.add(
                session=session, amount=3, create_model=health_ai_create_model2
            )
        finally:
            await session.execute(
                delete(HealthAILedgerEntryModel).where(
                    HealthAILedgerEntryModel.nonce == health_ai_create_model2.nonce
                )
            )
            await session.commit()

    async def test_invalid_input_error_insufficient_balance(
        self, session: AsyncSession, ledger_repository_healthai: LedgerRepository
    ):
        with pytest.raises(InvalidInputError) as error:
            await ledger_repository_healthai.add(
                session=session, amount=-5, create_model=health_ai_create_model2
            )
        assert str(error.value) == "Insufficient balance."

    async def test_invalid_input_error_duplicate_transaction(
        self, session: AsyncSession, ledger_repository_healthai: LedgerRepository
    ):
        with pytest.raises(InvalidInputError) as error:
            await ledger_repository_healthai.add(
                session=session, amount=3, create_model=health_ai_create_model3
            )
        assert str(error.value) == "This transaction was already happened."
