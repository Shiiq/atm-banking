from common.database.models.constants import BankOperationsToDB, BankOperationsFromInput
from common.database.models.dto import *
from common.services import AccountService, CustomerService, OperationService
from common.unit_of_work import UnitOfWork


class Deposit:

    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self._account_service = AccountService(uow=uow)
        self._customer_service = CustomerService(uow=uow)
        self._operation_service = OperationService(uow=uow)

    async def __call__(self, input_data: DepositInput):
        customer = await self._get_customer(
            customer_data=input_data.customer
        )
        acc = await self.uow.account_repo.get_by_id(obj_id=1)
        acc.balance = acc.balance + 666
        acc = await self.uow.account_repo.update(obj=acc)
        print("*" * 50)
        # print(acc.customer.id, acc.customer.created_at, acc.customer.updated_at, acc.customer.first_name, acc.customer.last_name)
        print(BankAccountRead(id=acc.id,
                              balance=acc.balance,
                              created_at=acc.created_at,
                              updated_at=acc.updated_at))
        # a = BankAccountRead.from_orm(acc)
        # print(a)
        # bu = BankAccountUpdate(id=1, amount=40000)
        # acc = await self._account_service.account_update(account_update_data=bu)
        # print(acc.balance)
        # bank_account = await self._update_bank_account(
        #     bank_account_id=customer.bank_account_id,
        #     operation_data=input_data.operation
        # )
        # operation = await self._register_operation(
        #     operation_data=BankOperationCreate(amount=input_data.operation.amount,
        #                                        bank_account_id=bank_account.id,
        #                                        bank_customer_id=customer.id,
        #                                        bank_operation=input_data.operation.type_)
        # )
        # commit
        await self.uow.commit()
        # return SummaryOperationInfo(account=bank_account,
        #                             customer=customer,
        #                             operation=operation)

    async def _register_customer(self, customer_data: CustomerInput):
        customer = await self._customer_service.customer_create(
            customer_create_data=BankCustomerCreate(customer=customer_data)
        )
        # await self.uow.commit()
        return customer

    async def _get_customer(self, customer_data: CustomerInput) -> BankCustomerRead:
        try:
            customer = await self._customer_service.customer_by_fullname(
                customer_search_data=BankCustomerSearch(first_name=customer_data.first_name,
                                                        last_name=customer_data.last_name)
            )
            print("try statement")
        except ValueError:
            customer = await self._register_customer(customer_data=customer_data)
            print("except statement")
        return customer

    async def _update_bank_account(self, bank_account_id: int, operation_data: OperationInput):
        # current_bank_account = await self._account_service.account_by_id(
        #     account_search_data=BankAccountSearch(id=bank_account_id)
        # )
        # updated_balance = current_bank_account.balance + operation_data.amount
        updated_bank_account = await self._account_service.account_update(
            account_update_data=BankAccountUpdate(id=bank_account_id,
                                                  amount=operation_data.amount)
        )
        return updated_bank_account

    async def _register_operation(self, operation_data: BankOperationCreate):
        operation = await self._operation_service.operation_create(
            operation_data=operation_data
        )
        return operation
