from src.infrastructure.config import load_config
from src.infrastructure.logger import setup_root_logger
from src.presentation.api.app import create_app


def get_app():
    """Creating the application api for remote deploying."""

    config = load_config()
    setup_root_logger(log_config=config.logging)
    return create_app(api_config=config.api, db_config=config.db)


app = get_app()
