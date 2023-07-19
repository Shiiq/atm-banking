

class DataConverter:

    def _from_dto_to_orm(self, input_data, output_model):
        return output_model(**input_data.model_dump())

    def _from_orm_to_dto(self, input_data, output_model):
        return output_model.from_orm(input_data)
