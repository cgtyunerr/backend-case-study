"""HealthAI main app."""

from fastapi import FastAPI

from app.travelai import ledger_router
from app.monorepo.middleware import ErrorHandlerMiddleware

api: FastAPI = FastAPI(
    title="TravelAI API", description="TravelAI http API.", version="1.0.0"
)

api.add_middleware(ErrorHandlerMiddleware)
api.include_router(ledger_router)
