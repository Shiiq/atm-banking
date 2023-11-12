from typing import Generic, TypeVar

from pydantic import BaseModel

from src.infrastructure.database.models import Base

DBModelT = TypeVar("DBModelT", bound=Base)
DTOModelT = TypeVar("DTOModelT", bound=BaseModel)


class DataConverterMixin(Generic[DBModelT, DTOModelT]):

    def from_dto_to_orm(
            self,
            input_data: DTOModelT,
            output_model: type[DBModelT]
    ) -> DBModelT:
        return output_model(**input_data.model_dump())

    def from_orm_to_dto(
            self,
            input_data: DBModelT,
            output_model: type[DTOModelT]
    ) -> DTOModelT:
        return output_model.model_validate(input_data)
