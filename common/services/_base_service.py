from common.unit_of_work import UnitOfWork


class BaseService:

    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    # TODO annotations?[input - Pydantic, output - ORM]
    def _from_dto_to_orm(self, input_data, output_model):
        return output_model(**input_data.dict())

    # TODO annotations?[input - ORM, output - Pydantic]
    def _from_orm_to_dto(self, input_data, output_model):
        return output_model.from_orm(input_data)
