from .bank_statement import bank_statement_router
# from .deposit import deposit_router

from .notes import additional_router

__all__ = (
    "bank_statement_router",
    # "deposit_router",
    "additional_router",
)
