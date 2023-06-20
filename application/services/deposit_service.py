from infrastructure.database.models import db
from infrastructure.database.models import dto

from ._base_service import BaseService


class DepositService(BaseService):

    # def __init__(self, uow):
    #     self.__uow = uow

    async def register_customer(self, customer_create_data):
        customer_orm = db.BankCustomerModel(
            first_name=customer_create_data.first_name,
            last_name=customer_create_data.last_name,
            bank_account=db.BankAccountModel()

        )
        customer = await self.__uow.customer_repo.create(customer_orm)
        return customer

    async def get_customer(self, customer_search_data):
        customer = await self.__uow.customer_repo.get_by_fullname(
            first_name=customer_search_data.first_name,
            last_name=customer_search_data.last_name
        )


    pass
