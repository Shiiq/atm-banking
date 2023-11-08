from enum import StrEnum

CONFIG_TEMPLATE_PATH = "./config_template.toml"


class LaunchType(StrEnum):

    LOCAL = "loc"
    REMOTE = "rem"


class ConfigLoaderError(Exception):

    _msg = (
        "Cannot read the LAUNCH environment variable."
        " Please set LAUNCH to 'loc' (e.g. export LAUNCH=loc)"
        " and restart the application. Or if you run the application remotely,"
        " check the environment variables in docker-compose file."
    )

    @property
    def msg(self):
        return self._msg

    def __str__(self):
        return self._msg
