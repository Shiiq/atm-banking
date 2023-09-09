import logging

from app.application.dto import (BankAccountRead,
                                 BankAccountUpdate,
                                 BankAccountSearch,
                                 BankCustomerCreate,
                                 BankCustomerSearch,
                                 BankOperationCreate,
                                 BankOperationRead,
                                 DepositInput,
                                 ShortOperationInfo)
from app.application.exceptions import CustomerNotExist
from .base import BaseHandler

_logger = logging.getLogger(__name__)


class Deposit(BaseHandler):

    async def execute(
            self,
            input_data: DepositInput
    ) -> ShortOperationInfo:

        async with self._uow:
            try:
                customer_search_data = BankCustomerSearch(first_name=input_data.first_name,
                                                          last_name=input_data.last_name)
                customer = await self._customer_service.by_fullname(search_data=customer_search_data)
                _logger.info(
                    f"The customer '{customer.id}' requested"
                    f" a deposit operation in the amount of '{input_data.amount}'"
                )
            except CustomerNotExist as err:
                _logger.info(
                    f"A customer '{input_data.first_name} {input_data.last_name}' does not exist"
                )
                customer_create_data = BankCustomerCreate(first_name=input_data.first_name,
                                                          last_name=input_data.last_name)
                customer = await self._customer_service.create(create_data=customer_create_data)
                _logger.info(
                    f"Customer '{customer.first_name} {customer.last_name}' has been registered"
                    f" with ID '{customer.id}'"
                )
            account_search_data = BankAccountSearch(id=customer.bank_account_id)
            account = await self._update_bank_account(account_search_data=account_search_data,
                                                      operation_amount=input_data.amount)
            _logger.info(
                f"Deposit operation for customer '{customer.id}' was successful"
            )
            operation_register_data = BankOperationCreate(amount=input_data.amount,
                                                          bank_account_id=account.id,
                                                          bank_customer_id=customer.id,
                                                          bank_operation_type=input_data.operation_type)
            operation = await self._register_bank_operation(operation_register_data=operation_register_data)
        _logger.info(
            f"Deposit operation for customer '{customer.id}' was registered"
        )
        return ShortOperationInfo(operation_datetime=operation.created_at,
                                  operation_type=operation.bank_operation_type,
                                  operation_amount=operation.amount,
                                  current_balance=account.balance)

    async def _update_bank_account(
            self,
            account_search_data: BankAccountSearch,
            operation_amount: int
    ) -> BankAccountRead:
        current_account = await self._account_service.by_id(search_data=account_search_data)
        account_update_data = BankAccountUpdate(id=current_account.id,
                                                balance=(current_account.balance + operation_amount))
        updated_account = await self._account_service.update(update_data=account_update_data)
        return updated_account

    async def _register_bank_operation(
            self,
            operation_register_data: BankOperationCreate
    ) -> BankOperationRead:
        operation = await self._operation_service.create(create_data=operation_register_data)
        return operation
