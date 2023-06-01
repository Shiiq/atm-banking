from infrastructure.database.db_core import create_engine, create_session_factory
from infrastructure.database.db_config import db_config

async with create_engine(db_config) as engine:
    session_factory = create_session_factory(engine)

    pass
