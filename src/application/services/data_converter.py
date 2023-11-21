from typing import Generic, Type, TypeVar

DBModelT = TypeVar("DBModelT")
DTOModelT = TypeVar("DTOModelT")


class DataConverterMixin(Generic[DBModelT, DTOModelT]):

    def from_dto_to_orm(
            self,
            input_data: DTOModelT,
            output_model: Type[DBModelT]
    ) -> DBModelT:
        return output_model(**input_data.model_dump())

    def from_orm_to_dto(
            self,
            input_data: DBModelT,
            output_model: Type[DTOModelT]
    ) -> DTOModelT:
        return output_model.model_validate(input_data)
