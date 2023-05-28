from pydantic import BaseModel, Extra


class DTO(BaseModel):

    class Config:
        extra = Extra.ignore
        orm_mode = True
        use_enum_value = True
