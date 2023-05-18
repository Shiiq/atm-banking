from enum import StrEnum

from pydantic import BaseModel, Extra


class BankOperationsFromInput(StrEnum):
    """Possible bank operations to choose from CLI or API"""
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    BANK_STATEMENT = "bank_statement"


class DTO(BaseModel):

    class Config:
        extra = Extra.ignore
        orm_mode = True
        use_enum_value = True
