import enum
from typing import Sequence, Optional, Any
from di.executors import AsyncExecutor
from di.api.scopes import Scope
from di import Container, ScopeState
from di.dependent import Dependent
from di.api.providers import DependencyProvider, DependencyProviderType


class DIScope(enum.StrEnum):
    APP = "app"
    REQUEST = "request"


class DIContainer:

    def __init__(self, container: Container, scopes: Sequence[Scope]):
        self._container = container
        self._executor = AsyncExecutor()
        self._scopes = scopes

