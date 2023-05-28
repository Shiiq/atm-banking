from application.services import (AccountService,
                                  CustomerService,
                                  OperationService)
from infrastructure.database.models import dto
from infrastructure.unit_of_work import UnitOfWork


class Withdraw:

    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self._account_service = AccountService(uow=uow)
        self._customer_service = CustomerService(uow=uow)
        self._operation_service = OperationService(uow=uow)

    async def __call__(self, input_data: dto.WithdrawInput) -> dto.SummaryOperationInfo:
        customer = await self._get_customer(
            customer_data=input_data.customer
        )
        bank_account = await self._update_bank_account(
            bank_account_id=customer.bank_account_id,
            operation_data=input_data.operation
        )
        operation = await self._register_operation(
            operation_data=dto.BankOperationCreate(amount=input_data.operation.amount,
                                                   bank_account_id=bank_account.id,
                                                   bank_customer_id=customer.id,
                                                   bank_operation=input_data.operation.type_)
        )
        await self.uow.commit()
        return dto.SummaryOperationInfo(account=bank_account,
                                        customer=customer,
                                        operation=operation)

    async def _get_customer(self, customer_data: dto.CustomerInput) -> dto.BankCustomerRead:
        try:
            customer = await self._customer_service.customer_by_fullname(
                customer_search_data=dto.BankCustomerSearch(first_name=customer_data.first_name,
                                                            last_name=customer_data.last_name)
            )
            return customer
        # TODO custom exceptions
        except ValueError:
            pass

    def _check_withdraw_possibility(self, current_balance: int, withdraw_amount: int) -> bool:
        return (current_balance - withdraw_amount) >= 0

    async def _update_bank_account(self, bank_account_id: int, operation_data: dto.OperationInput):
        current_bank_account = await self._account_service.account_by_id(
            account_search_data=dto.BankAccountSearch(id=bank_account_id)
        )
        if not self._check_withdraw_possibility(current_bank_account.balance, operation_data.amount):
            # TODO custom exceptions
            raise ValueError
        updated_balance = current_bank_account.balance - operation_data.amount
        updated_bank_account = await self._account_service.account_update(
            account_update_data=dto.BankAccountUpdate(id=bank_account_id,
                                                      balance=updated_balance)
        )
        return updated_bank_account

    async def _register_operation(self, operation_data: dto.BankOperationCreate):
        operation = await self._operation_service.operation_create(
            operation_data=operation_data
        )
        return operation
