from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Extra


class BankOperationType(StrEnum):
    """Possible operations for interaction with the app."""

    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    BANK_STATEMENT = "bank_statement"


class DTO(BaseModel):
    """Base DTO model config."""

    model_config = ConfigDict(
        extra=Extra.ignore,
        from_attributes=True,
        str_to_lower=True,
        use_enum_values=True
    )


class FrozenDTO(DTO):
    """Base frozen DTO model config."""

    model_config = ConfigDict(
        frozen=True
    )
