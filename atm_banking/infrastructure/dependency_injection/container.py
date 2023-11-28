from enum import StrEnum
from typing import Dict, Generic, Sequence, TypeVar, Optional

from di import Container, ScopeState
from di.api.scopes import Scope
from di.dependent import Dependent
from di.executors import AsyncExecutor

DependencyTypeT = TypeVar("DependencyTypeT")
SolvedDependencyT = TypeVar("SolvedDependencyT")


class DIScope(StrEnum):

    APP = "app"
    REQUEST = "request"


class DIContainer(Generic[DependencyTypeT, SolvedDependencyT]):

    _solved_dependencies: Dict[DependencyTypeT, SolvedDependencyT]

    def __init__(
            self,
            container: Container,
            executor: AsyncExecutor,
            scopes: Sequence[DIScope]
    ):
        self._container = container
        self._executor = executor
        self._scopes = scopes
        self._solved_dependencies = {}

    def enter_scope(
            self,
            scope: Scope,
            state: Optional[ScopeState] = None
    ):
        return self._container.enter_scope(scope=scope, state=state)

    async def execute(
            self,
            required_dependency: DependencyTypeT,
            scope: Scope,
            state: ScopeState
    ) -> SolvedDependencyT:

        solved_dependency = self._solved_dependencies.get(required_dependency)
        if not solved_dependency:
            solved_dependency = self._container.solve(
                Dependent(required_dependency, scope=scope),
                scopes=self._scopes
            )
            self._solved_dependencies[required_dependency] = solved_dependency
        return await solved_dependency.execute_async(
            executor=self._executor,
            state=state
        )
