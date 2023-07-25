from fastapi import FastAPI

from app.application.operation_handlers import BankStatement, Deposit, Withdraw
from app.infrastructure.provider import Provider


def setup_dependencies(app: FastAPI, provider: Provider):
    # app.dependency_overrides[BankStatement] = provider.get_bank_statement_handler
    # app.dependency_overrides[Deposit] = provider.get_deposit_handler
    # app.dependency_overrides[Withdraw] = provider.get_withdraw_handler
    app.dependency_overrides[BankStatement] = lambda: provider.get_handler(BankStatement)
    app.dependency_overrides[Deposit] = lambda: provider.get_handler(Deposit)
    app.dependency_overrides[Withdraw] = lambda: provider.get_handler(Withdraw)
