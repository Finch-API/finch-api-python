from __future__ import annotations

import os
import asyncio
import logging
from typing import TYPE_CHECKING, Iterator, AsyncIterator

import pytest

from finch import Finch, AsyncFinch

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest

pytest.register_assert_rewrite("tests.utils")

logging.getLogger("finch").setLevel(logging.DEBUG)


@pytest.fixture(scope="session")
def event_loop() -> Iterator[asyncio.AbstractEventLoop]:
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

access_token = "My Access Token"
client_id = "4ab15e51-11ad-49f4-acae-f343b7794375"
client_secret = "My Client Secret"


@pytest.fixture(scope="session")
def client(request: FixtureRequest) -> Iterator[Finch]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    with Finch(
        base_url=base_url,
        access_token=access_token,
        client_id=client_id,
        client_secret=client_secret,
        _strict_response_validation=strict,
    ) as client:
        yield client


@pytest.fixture(scope="session")
async def async_client(request: FixtureRequest) -> AsyncIterator[AsyncFinch]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    async with AsyncFinch(
        base_url=base_url,
        access_token=access_token,
        client_id=client_id,
        client_secret=client_secret,
        _strict_response_validation=strict,
    ) as client:
        yield client
