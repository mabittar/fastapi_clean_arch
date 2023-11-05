from typing import AsyncIterator

import asyncio
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession

from src.main import app as application
from src.infra.database.pg_adapter import async_engine, AsyncSessionLocal, async_get_db


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    """Reference: https://github.com/pytest-dev/pytest-asyncio/issues/38#issuecomment-264418154"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture()
async def client() -> AsyncIterator[AsyncClient]:
    async with AsyncClient(app=application, base_url='http://testserver') as async_client:
        yield async_client


@pytest.fixture()
async def connection():
    async with async_engine.begin() as conn:
        yield conn
        await conn.rollback()


@pytest.fixture()
async def session(connection: AsyncConnection):
    async with AsyncSessionLocal(connection, expire_on_commit=False) as _session:
        yield _session
        yield _session


@pytest.fixture(autouse=True)
async def override_dependency(session: AsyncSession):
    application.dependency_overrides[async_get_db] = lambda: session
