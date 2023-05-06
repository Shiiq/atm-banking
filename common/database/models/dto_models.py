from pydantic import BaseModel, PositiveInt

from cli.constants import BankOperationsFromInput


class BankClientDTO(BaseModel):
    first_name: str
    last_name: str


class BankOperationDTO(BankClientDTO):
    operation: str


class BankStatementDTO(BankOperationDTO):
    since: str
    till: str


class DepositOrWithdrawDTO(BankOperationDTO):
    """Input deposit/withdraw model"""
    amount: PositiveInt


class DepositDTO(BankOperationDTO):
    """Output deposit model"""
    amount: PositiveInt
    operation: BankOperationsFromInput = BankOperationsFromInput.DEPOSIT


class WithdrawDTO(BankOperationDTO):
    """Output withdraw model"""
    amount: PositiveInt
    operation: BankOperationsFromInput = BankOperationsFromInput.WITHDRAW
