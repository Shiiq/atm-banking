from sqlalchemy.ext.asyncio import AsyncSession


class SARepo:

    def __init__(self, session: AsyncSession):
        self._session = session
