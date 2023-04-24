from pydantic import BaseModel


class BankClientDTO(BaseModel):
    first_name: str
    last_name: str


class BankOperationDTO(BankClientDTO):
    operation: str


class BankStatementDTO(BankOperationDTO):
    since: str
    till: str


class DepositOrWithdrawDTO(BankOperationDTO):
    amount: int
