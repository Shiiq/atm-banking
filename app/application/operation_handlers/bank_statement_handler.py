import logging

from app.application.dto import (BankCustomerSearch,
                                 BankOperationSearch,
                                 BankStatementInput,
                                 ShortBankStatementInfo,
                                 FullBankStatementInfo)
from .base import BaseHandler

_logger = logging.getLogger(__name__)


class BankStatement(BaseHandler):

    async def execute(
            self,
            input_data: BankStatementInput
    ) -> FullBankStatementInfo:

        async with self._uow:
            customer_search_data = BankCustomerSearch(first_name=input_data.first_name,
                                                      last_name=input_data.last_name)
            customer = await self._customer_service.by_fullname(search_data=customer_search_data)
            _logger.info(
                f"The customer '{customer.id}' requested"
                f" a bank statement for the period {input_data.since} {input_data.till}"
            )
            operations_search_data = BankOperationSearch(bank_account_id=customer.bank_account_id,
                                                         bank_customer_id=customer.id,
                                                         since=input_data.since,
                                                         till=input_data.till)
            operations = await self._operation_service.by_date_interval(search_data=operations_search_data)
            _logger.info(
                f"A bank statement for customer '{customer.id}' is prepared"
            )
            # return ShortBankStatementInfo(since=input_data.since,
            #                               till=input_data.till,
            #                               operations=...)
            return FullBankStatementInfo(customer=customer,
                                         since=input_data.since,
                                         till=input_data.till,
                                         operations=operations)
