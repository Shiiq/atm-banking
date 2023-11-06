from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Extra


class BankOperationType(StrEnum):

    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    BANK_STATEMENT = "bank_statement"


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
