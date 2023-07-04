from sqlalchemy.ext.asyncio import AsyncSession


class SARepo:

    def __init__(self, session: AsyncSession):
        print("hello from INIT SARepo")
        self._session = session
