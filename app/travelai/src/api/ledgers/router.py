"""TravelAI api router."""

from typing import Annotated

from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse
from starlette import status

from app.travelai.schemas import CreateTransactionModel
from app.travelai.src.factory import Factory
from app.monorepo import SessionDep, OwnerIDPathDependency
from app.monorepo.core.ledgers.services.base_ledger_service import (
    BaseLedgerService,
)

base_ledger_service: BaseLedgerService = Factory.create_ledger_service()

ledger_router: APIRouter = APIRouter(tags=["ledger"], prefix="/ledger")


@ledger_router.get(
    path="/{owner_id}", summary="Get current balance.", response_model=int
)
async def get_current_balance(
    session: SessionDep,
    owner_id_dependency: Annotated[OwnerIDPathDependency, Depends()],
):
    """Get current balance."""
    result: int = await base_ledger_service.get_current_balance(
        session=session, owner_id=owner_id_dependency.owner_id
    )
    return ORJSONResponse(content=jsonable_encoder(result))


@ledger_router.post(
    path="/", summary="Create new ledger entity.", status_code=status.HTTP_201_CREATED
)
async def create_entity(
    session: SessionDep, create_model: CreateTransactionModel = Body(...)
):
    """Create entity."""
    await base_ledger_service.add_entity(session=session, create_model=create_model)
