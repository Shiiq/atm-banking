from typing import Annotated, Union

from fastapi import APIRouter, Depends, Request

from application.usecases import BankStatement, IUsecase
from infrastructure.database.models.dto import BankStatementInput, BankOperationsInfo
from infrastructure.provider import Provider
from presentation.api.providers import Stub

bank_statement_router = APIRouter(prefix="/bank_statement")


@bank_statement_router.post(path="/")
async def bank_statement(
        bank_statement_input: BankStatementInput,
        provider=Depends(BankStatement)
) -> BankOperationsInfo:
    res = await provider(bank_statement_input)
    return res
