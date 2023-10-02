from src.application.dto import BankOperationType
from src.application.operation_handlers import BankStatement, Deposit, Withdraw
from src.infrastructure.di.container import DIContainer, DIScope

from .provider import Provider


def build_provider(di_container: DIContainer, app_state: DIScope):
    provider = Provider(di_container=di_container,
                        app_state=app_state)
    return provider


def setup_handlers(provider: Provider):
    provider.register_handler(BankOperationType.BANK_STATEMENT, BankStatement)
    provider.register_handler(BankOperationType.DEPOSIT, Deposit)
    provider.register_handler(BankOperationType.WITHDRAW, Withdraw)
