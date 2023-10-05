
class ConfigLoaderError(Exception):

    def __init__(self, msg: str):
        self._msg = msg

    @property
    def msg(self):
        return self._msg
