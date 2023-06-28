from application.exceptions import AccountHasInsufficientFunds
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

    async def __call__(
            self,
            input_data: dto.WithdrawInput
    ) -> dto.SummaryOperationInfo:
        async with self.uow:
            customer_search_data = dto.BankCustomerSearch(first_name=input_data.customer.first_name,
                                                          last_name=input_data.customer.last_name)
            customer = await self._customer_service.by_fullname(search_data=customer_search_data)

            account_search_data = dto.BankAccountSearch(id=customer.bank_account_id)
            account = await self._update_bank_account(account_search_data=account_search_data,
                                                      operation_data=input_data.operation)
            # logging updated account

            operation_register_data = dto.BankOperationCreate(amount=input_data.operation.amount,
                                                              bank_account_id=account.id,
                                                              bank_customer_id=customer.id,
                                                              bank_operation_type=input_data.operation.type_)
            operation = await self._register_bank_operation(operation_register_data=operation_register_data)
            # logging registered operation

            return dto.SummaryOperationInfo(account=account,
                                            customer=customer,
                                            operation=operation)

    async def _update_bank_account(
            self,
            account_search_data: dto.BankAccountSearch,
            operation_data: dto.OperationInput
    ) -> dto.BankAccountRead:
        current_account = await self._account_service.by_id(search_data=account_search_data)

        if not self._check_possibility_to_withdraw(current_balance=current_account.balance,
                                                   requested_amount=operation_data.amount):
            raise AccountHasInsufficientFunds(account_id=current_account.id)

        else:
            account_update_data = dto.BankAccountUpdate(id=current_account.id,
                                                        balance=(current_account.balance - operation_data.amount))
            updated_account = await self._account_service.update(update_data=account_update_data)
            return updated_account

    def _check_possibility_to_withdraw(
            self,
            current_balance: int,
            requested_amount: int
    ) -> bool:
        return (current_balance - requested_amount) >= 0

    async def _register_bank_operation(
            self,
            operation_register_data: dto.BankOperationCreate
    ) -> dto.BankOperationRead:
        operation = await self._operation_service.create(create_data=operation_register_data)
        return operation
