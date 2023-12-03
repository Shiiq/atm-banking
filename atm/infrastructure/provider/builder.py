from di import ScopeState

from atm.application.dto import BankOperationType
from atm.application.operation_handlers import BankStatement
from atm.application.operation_handlers import Deposit
from atm.application.operation_handlers import Withdraw
from atm.infrastructure.dependency_injection import DIContainer
from .provider import Provider


def build_provider(
        di_container: DIContainer,
        app_state: ScopeState
) -> Provider:
    provider = Provider(di_container=di_container, app_state=app_state)
    return provider


def setup_provider(provider: Provider):
    provider.register_handler(BankOperationType.BANK_STATEMENT, BankStatement)
    provider.register_handler(BankOperationType.DEPOSIT, Deposit)
    provider.register_handler(BankOperationType.WITHDRAW, Withdraw)
