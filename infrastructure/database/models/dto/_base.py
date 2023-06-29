from pydantic import BaseModel, Extra


class DTO(BaseModel):

    class Config:
        anystr_lower = True
        extra = Extra.ignore
        orm_mode = True
        use_enum_values = True


class FrozenDTO(DTO):

    class Config:
        allow_mutation = False
