from pydantic import BaseModel, ConfigDict, Extra


class DTO(BaseModel):

    model_config = ConfigDict(
        str_to_lower=True,
        extra=Extra.ignore,
        from_attributes=True,
        use_enum_values=True
    )


class FrozenDTO(DTO):

    model_config = ConfigDict(
        frozen=True
    )
