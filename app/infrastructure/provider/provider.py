from app.application.dto import BankOperationsFromInput
from app.application.operation_handlers import BankStatement, Deposit, Withdraw
from app.infrastructure.di.container import DIContainer, DIScope



class Provider:

    def __init__(self, di_container: DIContainer, app_state):
        self._app_state = app_state
        self._di_container = di_container
        self._bank_statement_handler = BankStatement
        self._deposit_handler = Deposit
        self._withdraw_handler = Withdraw
        self._handlers = {
            # BankOperationsFromInput.BANK_STATEMENT: self._build_handler(BankStatement),
            # BankOperationsFromInput.DEPOSIT: self._build_handler(Deposit),
            # BankOperationsFromInput.WITHDRAW: self._build_handler(Withdraw),
            BankStatement: self._build_handler(BankStatement),
            Deposit: self._build_handler(Deposit),
            Withdraw: self._build_handler(Withdraw),
        }

    def get_handler(self, key_class):
        print("GET", key_class)
        print("ENTERING GET HANDLER METHOD")
        return self._handlers[key_class]

    async def _build_handler(self, handler_class):
        print("ENTERING BUILD HANDLER METHOD")
        async with self._di_container.enter_scope(
                scope=DIScope.REQUEST, state=self._app_state
        ) as request_state:
            handler = await self._di_container.execute(
                required_dependency=handler_class,
                scope=DIScope.REQUEST,
                state=request_state
            )
            print(id(handler))
            return handler

    async def get_bank_statement_handler(self):
        async with self._di_container.enter_scope(
                scope=DIScope.REQUEST, state=self._app_state
        ) as request_state:
            bank_statement_handler = await self._di_container.execute(
                required_dependency=self._bank_statement_handler,
                scope=DIScope.REQUEST,
                state=request_state
            )
            return bank_statement_handler

    async def get_deposit_handler(self):
        async with self._di_container.enter_scope(
                scope=DIScope.REQUEST, state=self._app_state
        ) as request_state:
            deposit_handler = await self._di_container.execute(
                required_dependency=self._deposit_handler,
                scope=DIScope.REQUEST,
                state=request_state
            )
            return deposit_handler

    async def get_withdraw_handler(self):
        async with self._di_container.enter_scope(
            scope=DIScope.REQUEST, state=self._app_state
        ) as request_state:
            withdraw_handler = await self._di_container.execute(
                required_dependency=self._withdraw_handler,
                scope=DIScope.REQUEST,
                state=request_state
            )
            return withdraw_handler
