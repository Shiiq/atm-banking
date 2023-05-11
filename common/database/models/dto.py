from datetime import date

from pydantic import BaseModel, NonNegativeInt, PositiveInt

from cli.constants import BankOperationsFromInput


class BankCustomerDTO(BaseModel):
    """Bank customer model"""
    first_name: str
    last_name: str


# class BankAccountToDB(BaseModel):
#     customer: BankCustomerDTO
#     deposit: NonNegativeInt
#
#
# class BankAccountFromDB(BaseModel):
#     customer: BankCustomerDTO
#     deposit: NonNegativeInt


class BankStatementDTO(BaseModel):
    """Output 'Bank Statement' model"""
    customer: BankCustomerDTO
    operation: BankOperationsFromInput = BankOperationsFromInput.BANK_STATEMENT
    since: date
    till: date


class DepositOrWithdrawBaseDTO(BaseModel):
    """Base model for 'Deposit' or 'Withdraw' DTO"""
    customer: BankCustomerDTO
    amount: PositiveInt


class DepositDTO(DepositOrWithdrawBaseDTO):
    """Output 'Deposit' model"""
    operation: BankOperationsFromInput = BankOperationsFromInput.DEPOSIT


class WithdrawDTO(DepositOrWithdrawBaseDTO):
    """Output 'Withdraw' model"""
    operation: BankOperationsFromInput = BankOperationsFromInput.WITHDRAW
