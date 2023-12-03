import logging

from atm.application.dto import BankAccountRead
from atm.application.dto import BankAccountUpdate
from atm.application.dto import BankCustomerCreate
from atm.application.dto import BankOperationCreate
from atm.application.dto import BankOperationRead
from atm.application.dto import DepositRequest
from atm.application.dto import OperationShortResponse
from atm.application.exceptions import CustomerNotExist
from .base import BaseHandler

_logger = logging.getLogger(__name__)


class Deposit(BaseHandler):

    async def execute(
            self,
            input_data: DepositRequest
    ) -> OperationShortResponse:

        async with self._uow:
            try:
                customer = await self._customer_service.get_by_fullname(
                    customer_first_name=input_data.first_name,
                    customer_last_name=input_data.last_name
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
                new_customer_data = BankCustomerCreate(
                    first_name=input_data.first_name,
                    last_name=input_data.last_name
                )
                customer = await self._customer_service.create(
                    create_data=new_customer_data
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
                "was successful"
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
            return OperationShortResponse(
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
