from uuid import UUID

from pydantic import BaseModel, ConfigDict, Extra


class DTO(BaseModel):

    model_config = ConfigDict(
        extra=Extra.ignore,
        from_attributes=True,
        str_to_lower=True,
        use_enum_values=True
    )


class FrozenDTO(DTO):

    model_config = ConfigDict(
        frozen=True
    )
