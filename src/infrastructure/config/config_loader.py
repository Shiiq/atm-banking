from dataclasses import dataclass
import os
import tomllib

from .api_config import APIConfig
from .db_config import DBConfig
from .log_config import LoggingConfig

CONFIG_TEMPLATE_PATH = "./src/infrastructure/config/config_template.toml"
IS_LOCAL_CONDITION = "1"


@dataclass(frozen=True, slots=True)
class Config:

    is_local: bool
    api: APIConfig
    db: DBConfig
    logging: LoggingConfig


def load_config():

    is_local = os.environ.get("LOCAL")

    if is_local == IS_LOCAL_CONDITION:
        return Config(
            is_local=True,
            api=APIConfig(),
            db=DBConfig(),
            logging=LoggingConfig()
        )
    else:
        with open(CONFIG_TEMPLATE_PATH, "rb") as f:
            config_data = tomllib.load(f)
        api_config = APIConfig(**config_data["api"])
        db_config = DBConfig(**config_data["database"])
        logging_config = LoggingConfig(**config_data["logging"])
        return Config(
            is_local=False,
            api=api_config,
            db=db_config,
            logging=logging_config
        )
