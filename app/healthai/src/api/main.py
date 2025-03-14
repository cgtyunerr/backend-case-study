"""HealthAI main app."""

from fastapi import FastAPI

from app.healthai import ledger_router
from app.monorepo.middleware import ErrorHandlerMiddleware

api: FastAPI = FastAPI(
    title="HealthAI API", description="HealthAI http API.", version="1.1.0"
)

api.add_middleware(ErrorHandlerMiddleware)
api.include_router(ledger_router)
