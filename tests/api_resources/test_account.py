# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from finch.types import Introspection, DisconnectResponse
from tests.utils import assert_matches_type
from finch._client import Finch, AsyncFinch

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestAccount:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_disconnect(self, client: Finch) -> None:
        account = client.account.disconnect()
        assert_matches_type(DisconnectResponse, account, path=["response"])

    @parametrize
    def test_raw_response_disconnect(self, client: Finch) -> None:
        response = client.account.with_raw_response.disconnect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(DisconnectResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_disconnect(self, client: Finch) -> None:
        with client.account.with_streaming_response.disconnect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(DisconnectResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_introspect(self, client: Finch) -> None:
        account = client.account.introspect()
        assert_matches_type(Introspection, account, path=["response"])

    @parametrize
    def test_raw_response_introspect(self, client: Finch) -> None:
        response = client.account.with_raw_response.introspect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Introspection, account, path=["response"])

    @parametrize
    def test_streaming_response_introspect(self, client: Finch) -> None:
        with client.account.with_streaming_response.introspect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Introspection, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccount:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_disconnect(self, client: AsyncFinch) -> None:
        account = await client.account.disconnect()
        assert_matches_type(DisconnectResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_disconnect(self, client: AsyncFinch) -> None:
        response = await client.account.with_raw_response.disconnect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(DisconnectResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_disconnect(self, client: AsyncFinch) -> None:
        async with client.account.with_streaming_response.disconnect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(DisconnectResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_introspect(self, client: AsyncFinch) -> None:
        account = await client.account.introspect()
        assert_matches_type(Introspection, account, path=["response"])

    @parametrize
    async def test_raw_response_introspect(self, client: AsyncFinch) -> None:
        response = await client.account.with_raw_response.introspect()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Introspection, account, path=["response"])

    @parametrize
    async def test_streaming_response_introspect(self, client: AsyncFinch) -> None:
        async with client.account.with_streaming_response.introspect() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Introspection, account, path=["response"])

        assert cast(Any, response.is_closed) is True
