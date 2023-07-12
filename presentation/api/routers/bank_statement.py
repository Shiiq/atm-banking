from typing import Annotated, Union

from fastapi import APIRouter, Depends, Request

from infrastructure.database.models.dto import BankStatementInput, BankOperationsInfo
from infrastructure.mediator import Mediator
from presentation.api.providers import Stub


bank_statement_router = APIRouter(prefix="/bank_statement")


@bank_statement_router.post(path="/")
async def bank_statement(
        bank_statement_input: BankStatementInput,
        mediator: Annotated[Mediator, Depends(Stub(Mediator))]
) -> BankOperationsInfo:
    res = await mediator(bank_statement_input)
    return res
