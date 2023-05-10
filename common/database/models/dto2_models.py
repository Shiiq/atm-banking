from pydantic import BaseModel, NonNegativeInt, PositiveInt

from cli.constants import BankOperationsFromInput


class BankCustomerDTO(BaseModel):
    first_name: str
    last_name: str


# class BankAccountToDB(BaseModel):
#     customer: BankCustomerDTO
#     deposit: NonNegativeInt
#
#
# class BankAccountFromDB(BaseModel):
#     customer: int
#     deposit: NonNegativeInt


class BankStatementDTO(BaseModel):
    """Output bank statement model"""
    customer: BankCustomerDTO
    operation: BankOperationsFromInput = BankOperationsFromInput.BANK_STATEMENT
    # TODO convert to datetime fields
    since: str
    till: str


class DepositDTO(BaseModel):
    """Output deposit model"""
    customer: BankCustomerDTO
    operation: BankOperationsFromInput = BankOperationsFromInput.DEPOSIT
    amount: PositiveInt


class WithdrawDTO(BaseModel):
    """Output withdraw model"""
    customer: BankCustomerDTO
    operation: BankOperationsFromInput = BankOperationsFromInput.WITHDRAW
    amount: PositiveInt
