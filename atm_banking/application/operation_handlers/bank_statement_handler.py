import logging

from atm_banking.application.dto import BankStatementRequest
from atm_banking.application.dto import BankStatementShortResponse
from .base import BaseHandler

_logger = logging.getLogger(__name__)


class BankStatement(BaseHandler):

    async def execute(
            self,
            input_data: BankStatementRequest
    ) -> BankStatementShortResponse:

        async with self._uow:
            customer = await self._customer_service.get_by_fullname(
                customer_first_name=input_data.first_name,
                customer_last_name=input_data.last_name
            )
            _logger.info(
                f"The customer '{customer.id}' requested "
                f"a bank statement for the period "
                f"{input_data.since} {input_data.till}"
            )
            operations = await self._operation_service.get_by_date_interval(
                account_id=customer.bank_account_id,
                customer_id=customer.id,
                since=input_data.since,
                till=input_data.till
            )
            _logger.info(
                f"A bank statement for customer '{customer.id}' is prepared"
            )
            return BankStatementShortResponse(
                since=input_data.since,
                till=input_data.till,
                current_balance=customer.bank_account.balance,
                operations=operations
            )
