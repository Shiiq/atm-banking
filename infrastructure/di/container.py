from enum import StrEnum
from typing import Sequence, Optional

from di import Container, ScopeState
from di.api.scopes import Scope
from di.executors import AsyncExecutor
from di.dependent import Dependent


class DIScope(StrEnum):
    APP = "app"
    REQUEST = "request"


class DIContainer:

    def __init__(self, container: Container, executor: AsyncExecutor, scopes: Sequence[Scope]):
        self.container = container
        self.executor = executor
        self.scopes = scopes

    async def enter_scope(self, scope: Scope, state: Optional[ScopeState] = None):
        return self.container.enter_scope(scope=scope, state=state)

    async def execute(self):
        pass