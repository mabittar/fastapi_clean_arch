from typing import AsyncGenerator

import pytest
from httpx import AsyncClient

from src import application


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture
async def ac() -> AsyncGenerator:
    async with AsyncClient(app=application, base_url="https://test") as c:
        yield c
        