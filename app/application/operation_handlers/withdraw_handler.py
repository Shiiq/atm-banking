import logging

from app.application.dto import (BankAccountRead,
                                 BankAccountUpdate,
                                 BankAccountSearch,
                                 BankCustomerSearch,
                                 BankOperationCreate,
                                 BankOperationRead,
                                 WithdrawInput,
                                 SummaryOperationInfo)
from app.application.exceptions import AccountHasInsufficientFunds
from .base import BaseHandler


class Withdraw(BaseHandler):

    async def execute(
            self,
            input_data: WithdrawInput
    ) -> SummaryOperationInfo:

        async with self._uow:
            customer_search_data = BankCustomerSearch(first_name=input_data.first_name,
                                                      last_name=input_data.last_name)
            customer = await self._customer_service.by_fullname(search_data=customer_search_data)

            account_search_data = BankAccountSearch(id=customer.bank_account_id)
            account = await self._update_bank_account(account_search_data=account_search_data,
                                                      operation_amount=input_data.amount)
            logging.info("Withdraw operation was successful")
            operation_register_data = BankOperationCreate(amount=input_data.amount,
                                                          bank_account_id=account.id,
                                                          bank_customer_id=customer.id,
                                                          bank_operation_type=input_data.operation_type)
            operation = await self._register_bank_operation(operation_register_data=operation_register_data)
            logging.info("Withdraw operation was registered")
            return SummaryOperationInfo(account=account,
                                        customer=customer,
                                        operation=operation)

    async def _update_bank_account(
            self,
            account_search_data: BankAccountSearch,
            operation_amount: int
    ) -> BankAccountRead:
        current_account = await self._account_service.by_id(search_data=account_search_data)
        if not self._check_possibility_to_withdraw(current_balance=current_account.balance,
                                                   requested_amount=operation_amount):
            logging.info(f"An account with ID '{current_account.id}' has insufficient funds to withdraw")
            raise AccountHasInsufficientFunds(account_id=current_account.id)
        else:
            account_update_data = BankAccountUpdate(id=current_account.id,
                                                    balance=(current_account.balance - operation_amount))
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
            operation_register_data: BankOperationCreate
    ) -> BankOperationRead:
        operation = await self._operation_service.create(create_data=operation_register_data)
        return operation
