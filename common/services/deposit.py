from common.uow import UnitOfWork

class DepositOperationService:

    def __init__(self, unit_of_work: UnitOfWork):
        self.uow = unit_of_work

    async def get_or_register_customer(self, first_name, last_name):
        current_customer = await self.uow.customer_repo.get_by_fullname(first_name=first_name,
                                                                        last_name=last_name)
    pass
