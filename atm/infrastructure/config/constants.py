from enum import StrEnum
from pathlib import Path

_BASE_DIR = Path(__file__).parent.parent.parent.parent
CONFIG_TEMPLATE_PATH = _BASE_DIR.joinpath("./config_template.toml")


class LaunchType(StrEnum):
    """The two types of the application launch."""

    LOCAL = "loc"
    REMOTE = "rem"


class ConfigLoaderError(Exception):

    _msg = (
        "Cannot read the LAUNCH environment variable. "
        "Please set LAUNCH to 'loc' (e.g. export LAUNCH=loc) "
        "and restart the application. Or if you run the application remotely,"
        " check the environment variables in docker-compose files."
    )

    @property
    def msg(self):
        return self._msg

    def __str__(self):
        return self._msg
