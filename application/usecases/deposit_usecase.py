from application.exceptions import CustomerNotExist
from application.services import (AccountService,
                                  CustomerService,
                                  OperationService)
from infrastructure.database.models import dto
from infrastructure.unit_of_work import UnitOfWork

from .base import BaseUsecase


class Deposit(BaseUsecase):

    # def __init__(self, uow: UnitOfWork):
    #     self.uow = uow
    #     self._account_service = AccountService(uow=uow)
    #     self._customer_service = CustomerService(uow=uow)
    #     self._operation_service = OperationService(uow=uow)

    async def __call__(
            self,
            input_data: dto.DepositInput
    ) -> dto.SummaryOperationInfo:
        async with self._uow:
            try:
                customer_search_data = dto.BankCustomerSearch(first_name=input_data.first_name,
                                                              last_name=input_data.last_name)
                customer = await self._customer_service.by_fullname(search_data=customer_search_data)

            except CustomerNotExist as err:
                # logging err
                customer_create_data = dto.BankCustomerCreate(first_name=input_data.first_name,
                                                              last_name=input_data.last_name)
                customer = await self._customer_service.create(create_data=customer_create_data)
                # logging customer registration

            account_search_data = dto.BankAccountSearch(id=customer.bank_account_id)
            account = await self._update_bank_account(account_search_data=account_search_data,
                                                      operation_amount=input_data.amount)
            # logging updated account

            operation_register_data = dto.BankOperationCreate(amount=input_data.amount,
                                                              bank_account_id=account.id,
                                                              bank_customer_id=customer.id,
                                                              bank_operation_type=input_data.operation_type)
            operation = await self._register_bank_operation(operation_register_data=operation_register_data)
            # logging registered operation

            return dto.SummaryOperationInfo(account=account,
                                            customer=customer,
                                            operation=operation)

    async def _update_bank_account(
            self,
            account_search_data: dto.BankAccountSearch,
            operation_amount: int
    ) -> dto.BankAccountRead:
        current_account = await self._account_service.by_id(search_data=account_search_data)
        account_update_data = dto.BankAccountUpdate(id=current_account.id,
                                                    balance=(current_account.balance + operation_amount))
        updated_account = await self._account_service.update(update_data=account_update_data)
        return updated_account

    async def _register_bank_operation(
            self,
            operation_register_data: dto.BankOperationCreate
    ) -> dto.BankOperationRead:
        operation = await self._operation_service.create(create_data=operation_register_data)
        return operation
