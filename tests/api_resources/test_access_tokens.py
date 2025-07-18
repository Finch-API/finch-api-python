# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Iterator, AsyncIterator, cast

import pytest

from finch import Finch, AsyncFinch
from finch.types import CreateAccessTokenResponse
from tests.utils import assert_matches_type

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest  # pyright: ignore[reportPrivateImportUsage]

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
client_id = "00000000-0000-0000-0000-000000000000"
client_secret = "TEST"


@pytest.fixture(scope="module")
def client(request: FixtureRequest) -> Iterator[Finch]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    with Finch(
        base_url=base_url, client_id=client_id, client_secret=client_secret, _strict_response_validation=strict
    ) as client:
        yield client


@pytest.fixture(scope="module")
async def async_client(request: FixtureRequest) -> AsyncIterator[AsyncFinch]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    async with AsyncFinch(
        base_url=base_url, client_id=client_id, client_secret=client_secret, _strict_response_validation=strict
    ) as client:
        yield client


class TestAccessTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Finch) -> None:
        access_token = client.access_tokens.create(
            code="<your_authorization_code>",
        )
        assert_matches_type(CreateAccessTokenResponse, access_token, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Finch) -> None:
        access_token = client.access_tokens.create(
            code="<your_authorization_code>",
            client_id="6d28c315-5eaa-4071-8ea5-f030eb45edbc",
            client_secret="<your_client_secret>",
            redirect_uri="https://example.com",
        )
        assert_matches_type(CreateAccessTokenResponse, access_token, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Finch) -> None:
        response = client.access_tokens.with_raw_response.create(
            code="<your_authorization_code>",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = response.parse()
        assert_matches_type(CreateAccessTokenResponse, access_token, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Finch) -> None:
        with client.access_tokens.with_streaming_response.create(
            code="<your_authorization_code>",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_token = response.parse()
            assert_matches_type(CreateAccessTokenResponse, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccessTokens:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFinch) -> None:
        access_token = await async_client.access_tokens.create(
            code="<your_authorization_code>",
        )
        assert_matches_type(CreateAccessTokenResponse, access_token, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFinch) -> None:
        access_token = await async_client.access_tokens.create(
            code="<your_authorization_code>",
            client_id="6d28c315-5eaa-4071-8ea5-f030eb45edbc",
            client_secret="<your_client_secret>",
            redirect_uri="https://example.com",
        )
        assert_matches_type(CreateAccessTokenResponse, access_token, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFinch) -> None:
        response = await async_client.access_tokens.with_raw_response.create(
            code="<your_authorization_code>",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = response.parse()
        assert_matches_type(CreateAccessTokenResponse, access_token, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFinch) -> None:
        async with async_client.access_tokens.with_streaming_response.create(
            code="<your_authorization_code>",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_token = await response.parse()
            assert_matches_type(CreateAccessTokenResponse, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True
