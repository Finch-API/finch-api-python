# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.sandbox import ConnectionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    def test_method_create(self, client: Finch) -> None:
        connection = client.sandbox.connections.create(
            provider_id="provider_id",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    def test_method_create_with_all_params(self, client: Finch) -> None:
        connection = client.sandbox.connections.create(
            provider_id="provider_id",
            authentication_type="credential",
            employee_size=0,
            products=["string", "string", "string"],
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    def test_raw_response_create(self, client: Finch) -> None:
        response = client.sandbox.connections.with_raw_response.create(
            provider_id="provider_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    def test_streaming_response_create(self, client: Finch) -> None:
        with client.sandbox.connections.with_streaming_response.create(
            provider_id="provider_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConnections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    async def test_method_create(self, async_client: AsyncFinch) -> None:
        connection = await async_client.sandbox.connections.create(
            provider_id="provider_id",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFinch) -> None:
        connection = await async_client.sandbox.connections.create(
            provider_id="provider_id",
            authentication_type="credential",
            employee_size=0,
            products=["string", "string", "string"],
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFinch) -> None:
        response = await async_client.sandbox.connections.with_raw_response.create(
            provider_id="provider_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFinch) -> None:
        async with async_client.sandbox.connections.with_streaming_response.create(
            provider_id="provider_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True
