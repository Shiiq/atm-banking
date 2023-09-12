import logging

from app.application.dto import (BankAccountRead,
                                 BankAccountUpdate,
                                 BankAccountSearch,
                                 BankCustomerSearch,
                                 BankOperationCreate,
                                 BankOperationRead,
                                 WithdrawInput,
                                 ShortOperationInfo)
from app.application.exceptions import AccountHasInsufficientFunds
from .base import BaseHandler

_logger = logging.getLogger(__name__)


class Withdraw(BaseHandler):

    async def execute(
            self,
            input_data: WithdrawInput
    ) -> ShortOperationInfo:

        async with self._uow:
            customer_search_data = BankCustomerSearch(
                first_name=input_data.first_name,
                last_name=input_data.last_name
            )
            customer = await self._customer_service.by_fullname(
                search_data=customer_search_data
            )
            _logger.info(
                f"The customer '{customer.id}' requested "
                f"a withdraw operation in the amount "
                f"of '{input_data.amount}'"
            )

            if not self._check_possibility_to_withdraw(
                    current_balance=customer.bank_account.balance,
                    requested_amount=input_data.amount
            ):
                _logger.info(
                    f"An account '{customer.bank_account.id}' "
                    f"has insufficient funds"
                )
                raise AccountHasInsufficientFunds(account_id=customer.bank_account_id)

            account_update_data = BankAccountUpdate(
                id=customer.bank_account_id,
                balance=(customer.bank_account.balance - input_data.amount)
            )
            updated_account = await self._update_bank_account(
                update_data=account_update_data,
            )
            _logger.info(
                f"Withdraw operation for customer '{customer.id}' "
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
                f"Withdraw operation for customer '{customer.id}' "
                f"was registered"
            )
            return ShortOperationInfo(
                created_at=operation.created_at,
                bank_operation_type=operation.bank_operation_type,
                amount=operation.amount,
                current_balance=updated_account.balance
            )

    def _check_possibility_to_withdraw(
            self,
            current_balance: int,
            requested_amount: int
    ) -> bool:

        return (current_balance - requested_amount) >= 0

    async def _update_bank_account(
            self,
            update_data: BankAccountUpdate,
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
