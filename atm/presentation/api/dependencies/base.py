from fastapi import FastAPI

from atm.infrastructure.provider import Provider


def get_provider() -> Provider:
    raise NotImplementedError


def setup_dependencies(app: FastAPI, provider: Provider):
    app.dependency_overrides[get_provider] = lambda: provider
