from fastapi import APIRouter, Request

from application.operation_mediator import OperationMediator
from infrastructure.database.models.dto import BankStatementInput, BankOperationSearch

bank_statement_router = APIRouter(prefix="/bank_statement")


@bank_statement_router.post(path="/")
async def bank_statement(bank_statement_input: BankStatementInput, request: Request):
    operation_mediator = OperationMediator()
    base_usecase = request.state.base_usecase
    print(base_usecase.uow)
    print(base_usecase.uow._session)
    print(base_usecase._operation_service)
    # handler_class = operation_mediator.get_operation_handler(bank_statement_input.operation_type)
    # handler = handler_class(base_usecase)
    # result = await handler(bank_statement_input)
    # print(result)
    return bank_statement_input
