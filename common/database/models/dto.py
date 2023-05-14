from datetime import date

from pydantic import BaseModel, Extra, NonNegativeInt, PositiveInt

from cli.constants import BankOperationsFromInput


class BaseDTO(BaseModel):

    class Config:
        extra = Extra.ignore
        orm_mode = True
        use_enum_value = True


class CustomerBaseDTO(BaseDTO):
    """Base bank customer model"""
    first_name: str
    last_name: str


class AccountBaseDTO(BaseDTO):
    """Base bank account model"""
    deposit: NonNegativeInt = 0


class BankCustomerToDB(CustomerBaseDTO):
    """Bank customer model to add to db"""
    bank_account: AccountBaseDTO


class BankCustomerFromDB(CustomerBaseDTO):
    """Bank customer output model"""
    id: int
    bank_account_id: int


# class BankAccountFromDB(BaseModel):
#     customer: BankCustomerDTO
#     deposit: NonNegativeInt


class BankStatementDTO(BaseDTO):
    """Output 'Bank Statement' model"""
    customer: CustomerBaseDTO
    operation: BankOperationsFromInput = BankOperationsFromInput.BANK_STATEMENT
    since: date
    till: date


class DepositDTO(BaseDTO):
    """Output 'Deposit' model"""
    customer: CustomerBaseDTO
    operation: BankOperationsFromInput = BankOperationsFromInput.DEPOSIT
    amount: PositiveInt


class WithdrawDTO(BaseDTO):
    """Output 'Withdraw' model"""
    customer: CustomerBaseDTO
    operation: BankOperationsFromInput = BankOperationsFromInput.WITHDRAW
    amount: PositiveInt
