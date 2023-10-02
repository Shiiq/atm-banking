import logging

from src.application.dto import (BankAccountRead,
                                 BankAccountUpdate,
                                 BankCustomerCreate,
                                 BankCustomerSearch,
                                 BankOperationCreate,
                                 BankOperationRead,
                                 DepositInput,
                                 ShortOperationInfo)
from src.application.exceptions import CustomerNotExist
from .base import BaseHandler

_logger = logging.getLogger(__name__)


class Deposit(BaseHandler):

    async def execute(
            self,
            input_data: DepositInput
    ) -> ShortOperationInfo:

        async with self._uow:
            try:
                customer_search_data = BankCustomerSearch(
                    first_name=input_data.first_name,
                    last_name=input_data.last_name
                )
                customer = await self._customer_service.by_fullname(
                    search_data=customer_search_data
                )
                _logger.info(
                    f"The customer '{customer.id}' requested "
                    f"a deposit operation in the amount "
                    f"of '{input_data.amount}'"
                )
            except CustomerNotExist:
                _logger.info(
                    f"A customer '{input_data.first_name} "
                    f"{input_data.last_name}' does not exist"
                )
                customer_create_data = BankCustomerCreate(
                    first_name=input_data.first_name,
                    last_name=input_data.last_name
                )
                customer = await self._customer_service.create(
                    create_data=customer_create_data
                )
                _logger.info(
                    f"Customer '{customer.first_name} {customer.last_name}' "
                    f"has been registered with ID '{customer.id}'"
                )
            account_update_data = BankAccountUpdate(
                id=customer.bank_account_id,
                balance=(customer.bank_account.balance + input_data.amount)
            )
            updated_account = await self._update_bank_account(
                update_data=account_update_data,
            )
            _logger.info(
                f"Deposit operation for customer '{customer.id}' "
                f"was successful"
            )
            operation_register_data = BankOperationCreate(
                amount=input_data.amount,
                bank_account_id=updated_account.id,
                bank_customer_id=customer.id,
                bank_operation_type=input_data.operation_type
            )
            operation = await self._register_bank_operation(
                operation_register_data=operation_register_data
            )
            _logger.info(
                f"Deposit operation for customer '{customer.id}' "
                f"was registered"
            )
            return ShortOperationInfo(
                created_at=operation.created_at,
                bank_operation_type=operation.bank_operation_type,
                amount=operation.amount,
                current_balance=updated_account.balance
            )

    async def _update_bank_account(
            self,
            update_data: BankAccountUpdate
    ) -> BankAccountRead:

        updated_account = await self._account_service.update(
            update_data=update_data
        )
        return updated_account

    async def _register_bank_operation(
            self,
            operation_register_data: BankOperationCreate
    ) -> BankOperationRead:

        operation = await self._operation_service.create(
            create_data=operation_register_data
        )
        return operation
