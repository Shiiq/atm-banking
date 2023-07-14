from typing import Annotated, Union

from fastapi import APIRouter, Depends, Request

from application.usecases import BankStatement, IUsecase
from infrastructure.database.models.dto import BankStatementInput, BankOperationsInfo
from infrastructure.provider import Provider
from presentation.api.providers import Stub

additional_router = APIRouter(prefix="/add")

async def common_parameters(q: str | None = "get", skip: int = 0, limit: int = 100):
    return (q, skip, limit)
    # return {"q": q, "skip": skip, "limit": limit}


@additional_router.get("/it/")
async def read_items(commons=Depends(common_parameters)):
# async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
