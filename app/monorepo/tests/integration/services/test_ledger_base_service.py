"""Ledger base service integration test module."""

from typing import Dict
from unittest.mock import patch

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.healthai import HealthAILedgerOperation
from app.healthai.models import HealthAILedgerEntryModel
from app.healthai.schemas import CreateTransactionModel as HealthAICreate

from app.monorepo import InvalidInputError
from app.monorepo.core.ledgers.services import BaseLedgerService
from app.monorepo.core.db.ledger_repository import LedgerRepository
from app.monorepo.tests import mock_async_func_returning_id
from app.travelai import TravelAILedgerOperation
from app.travelai.models import TravelAILedgerEntryModel
from app.travelai.schemas import CreateTransactionModel as TravelAICreate


class HealthAIRepository(LedgerRepository[HealthAILedgerEntryModel, HealthAICreate]):
    model = HealthAILedgerEntryModel
    schema = HealthAICreate


class TravelAIRepository(LedgerRepository[HealthAILedgerEntryModel, HealthAICreate]):
    model = TravelAILedgerEntryModel
    schema = TravelAICreate


travel_ai_create_model: TravelAICreate = TravelAICreate(
    owner_id="1", nonce="create1", operation=TravelAILedgerOperation.DAILY_REWARD
)

health_ai_create_model: HealthAICreate = HealthAICreate(
    owner_id="1", nonce="create1", operation=HealthAILedgerOperation.SIGNUP_CREDIT
)

health_ai_create_model_error: HealthAICreate = HealthAICreate(
    owner_id="1", nonce="create1", operation=HealthAILedgerOperation.CREDIT_ADD
)

LEDGER_OPERATION_CONFIG: Dict[str, int] = {
    "DAILY_REWARD": 1,
    "SIGNUP_CREDIT": 3,
    "CREDIT_SPEND": -1,
    "CONTENT_CREATION": -5,
    "CONTENT_ACCESS": 0,
}


@pytest.fixture
def base_ledger_service_health_ai() -> BaseLedgerService:
    return BaseLedgerService[HealthAICreate](
        ledger_repository=HealthAIRepository(),
        ledger_operation_config=LEDGER_OPERATION_CONFIG,
    )


@pytest.fixture
def base_ledger_service_travel_ai() -> BaseLedgerService:
    return BaseLedgerService[TravelAICreate](
        ledger_repository=TravelAIRepository(),
        ledger_operation_config=LEDGER_OPERATION_CONFIG,
    )


class TestGetCurrentBalance:
    @patch(
        "app.monorepo.core.ledgers.services.base_ledger_service"
        ".LedgerRepository.get_current_balance_by_owner_id",
        side_effect=mock_async_func_returning_id,
    )
    async def test_ok_health_ai(
        self,
        mock_repository,
        session: AsyncSession,
        base_ledger_service_health_ai: BaseLedgerService,
    ):
        result: int = await base_ledger_service_health_ai.get_current_balance(
            owner_id="1", session=session
        )
        assert result == 987
        mock_repository.assert_called_once_with(owner_id="1", session=session)

    @patch(
        "app.monorepo.core.ledgers.services.base_ledger_service"
        ".LedgerRepository.get_current_balance_by_owner_id",
        side_effect=mock_async_func_returning_id,
    )
    async def test_ok_travel_ai(
        self,
        mock_repository,
        session: AsyncSession,
        base_ledger_service_travel_ai: BaseLedgerService,
    ):
        result: int = await base_ledger_service_travel_ai.get_current_balance(
            owner_id="1", session=session
        )
        assert result == 987
        mock_repository.assert_called_once_with(owner_id="1", session=session)


class TestAddEntity:
    @patch(
        "app.monorepo.core.ledgers.services.base_ledger_service.LedgerRepository.add",
        side_effect=mock_async_func_returning_id,
    )
    async def test_ok_health_ai(
        self,
        mock_repository,
        session: AsyncSession,
        base_ledger_service_health_ai: BaseLedgerService,
    ):
        result: int = await base_ledger_service_health_ai.add_entity(
            session=session, create_model=health_ai_create_model
        )
        assert result == 987
        mock_repository.assert_called_once_with(
            session=session, create_model=health_ai_create_model, amount=3
        )

    @patch(
        "app.monorepo.core.ledgers.services.base_ledger_service.LedgerRepository.add",
        side_effect=mock_async_func_returning_id,
    )
    async def test_ok_travel_ai(
        self,
        mock_repository,
        session: AsyncSession,
        base_ledger_service_travel_ai: BaseLedgerService,
    ):
        result: int = await base_ledger_service_travel_ai.add_entity(
            session=session, create_model=travel_ai_create_model
        )
        assert result == 987
        mock_repository.assert_called_once_with(
            session=session, create_model=travel_ai_create_model, amount=1
        )

    @patch(
        "app.monorepo.core.ledgers.services.base_ledger_service.LedgerRepository.add",
        side_effect=mock_async_func_returning_id,
    )
    async def test_invalid_input_error(
        self,
        mock_repository,
        session: AsyncSession,
        base_ledger_service_travel_ai: BaseLedgerService,
    ):
        with pytest.raises(InvalidInputError) as error:
            await base_ledger_service_travel_ai.add_entity(
                session=session, create_model=health_ai_create_model_error
            )
        assert str(error.value) == "Operation not found."
