from datetime import date

from pydantic import NonNegativeInt, PositiveInt

from ._base import DTO, BankOperationsFromInput


class AccountDTO(DTO):
    """Base bank account model"""
    balance: NonNegativeInt = 0


class CustomerDTO(DTO):
    """Base bank customer model"""
    first_name: str
    last_name: str


class BankAccountRead(DTO):
    """Bank account output model from DB"""
    id: int
    balance: NonNegativeInt


class BankCustomerCreate(CustomerDTO):
    """Bank customer model to write to DB"""
    # first_name
    # last_name
    bank_account: AccountDTO


class BankCustomerRead(CustomerDTO):
    """Bank customer output model from DB"""
    # first_name
    # last_name
    id: int
    bank_account_id: int
    bank_account: BankAccountRead


# class BankAccountRead(DTO):
#     customer: CustomerDTO
#     balance: NonNegativeInt


class BankStatementDTO(DTO):
    customer: CustomerDTO | BankCustomerRead
    operation: BankOperationsFromInput = BankOperationsFromInput.BANK_STATEMENT
    since: date
    till: date


class DepositDTO(DTO):
    customer: CustomerDTO | BankCustomerRead
    operation: BankOperationsFromInput = BankOperationsFromInput.DEPOSIT
    amount: PositiveInt


class WithdrawDTO(DTO):
    customer: CustomerDTO | BankCustomerRead
    operation: BankOperationsFromInput = BankOperationsFromInput.WITHDRAW
    amount: PositiveInt
