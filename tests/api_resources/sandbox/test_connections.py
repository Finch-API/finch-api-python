# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._client import Finch, AsyncFinch
from finch.types.sandbox import ConnectionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestConnections:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Finch) -> None:
        connection = client.sandbox.connections.create(
            provider_id="string",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Finch) -> None:
        connection = client.sandbox.connections.create(
            provider_id="string",
            authentication_type="credentials",
            employer_size=0,
            products=["string", "string", "string"],
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Finch) -> None:
        response = client.sandbox.connections.with_raw_response.create(
            provider_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])


class TestAsyncConnections:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncFinch) -> None:
        connection = await client.sandbox.connections.create(
            provider_id="string",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncFinch) -> None:
        connection = await client.sandbox.connections.create(
            provider_id="string",
            authentication_type="credentials",
            employer_size=0,
            products=["string", "string", "string"],
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncFinch) -> None:
        response = await client.sandbox.connections.with_raw_response.create(
            provider_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])
