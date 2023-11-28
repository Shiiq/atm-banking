from dataclasses import dataclass
import os
import tomllib

from atm_banking.infrastructure.database.db_config import DBConfig
from atm_banking.infrastructure.logger.log_config import LoggingConfig
from atm_banking.presentation.api.api_config import APIConfig
from .constants import CONFIG_TEMPLATE_PATH, ConfigLoaderError, LaunchType


@dataclass(frozen=True, slots=True)
class Config:

    launch_type: LaunchType
    api: APIConfig
    db: DBConfig
    logging: LoggingConfig


def load_config() -> Config:

    launch_type = os.environ.get("LAUNCH")
    if not launch_type or launch_type not in iter(LaunchType):
        raise ConfigLoaderError

    if launch_type == LaunchType.LOCAL:
        return Config(
            launch_type=LaunchType.LOCAL,
            api=APIConfig(),
            db=DBConfig(),
            logging=LoggingConfig()
        )

    elif launch_type == LaunchType.REMOTE:
        with open(CONFIG_TEMPLATE_PATH, "rb") as f:
            config_data = tomllib.load(f)
        api_config = APIConfig(**config_data["api"])
        db_config = DBConfig(**config_data["database"])
        logging_config = LoggingConfig(**config_data["logging"])
        return Config(
            launch_type=LaunchType.REMOTE,
            api=api_config,
            db=db_config,
            logging=logging_config
        )
