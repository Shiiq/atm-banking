class BaseService:

    # TODO annotations?[input - Pydantic, output - ORM]
    def _from_dto_to_orm(self, input_data, output_model):
        return output_model(**input_data.dict())

    # TODO annotations?[input - ORM, output - Pydantic]
    def _from_orm_to_dto(self, input_data, output_model):
        return output_model.from_orm(input_data)
