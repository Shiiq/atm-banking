from datetime import date

from pydantic import BaseModel, NonNegativeInt, PositiveInt

from cli.constants import BankOperationsFromInput


class BankCustomerBaseDTO(BaseModel):
    """Bank customer input model"""
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class BankAccountDefaultDTO(BaseModel):
    deposit: NonNegativeInt = 0


class BankCustomerToDB(BankCustomerBaseDTO):
    bank_account: BankAccountDefaultDTO


class BankCustomerFromDB(BankCustomerBaseDTO):
    """Bank customer output model"""
    id: int
    bank_account_id: int


# class BankAccountFromDB(BaseModel):
#     customer: BankCustomerDTO
#     deposit: NonNegativeInt


class BankStatementDTO(BaseModel):
    """Output 'Bank Statement' model"""
    customer: BankCustomerBaseDTO
    operation: BankOperationsFromInput = BankOperationsFromInput.BANK_STATEMENT
    since: date
    till: date


class DepositOrWithdrawBaseDTO(BaseModel):
    """Base model for 'Deposit' or 'Withdraw' DTO"""
    customer: BankCustomerBaseDTO
    amount: PositiveInt


class DepositDTO(DepositOrWithdrawBaseDTO):
    """Output 'Deposit' model"""
    operation: BankOperationsFromInput = BankOperationsFromInput.DEPOSIT


class WithdrawDTO(DepositOrWithdrawBaseDTO):
    """Output 'Withdraw' model"""
    operation: BankOperationsFromInput = BankOperationsFromInput.WITHDRAW
