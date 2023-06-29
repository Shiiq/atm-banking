from fastapi import APIRouter


deposit_router = APIRouter(
    prefix="/depostit"
)


@deposit_router.post(
    "/"
)
async def deposit_operation():
    pass
