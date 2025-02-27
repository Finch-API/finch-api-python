# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.connect import (
    SessionNewResponse,
    SessionReauthenticateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_new(self, client: Finch) -> None:
        session = client.connect.sessions.new(
            customer_id="x",
            customer_name="x",
            products=["company"],
        )
        assert_matches_type(SessionNewResponse, session, path=["response"])

    @parametrize
    def test_method_new_with_all_params(self, client: Finch) -> None:
        session = client.connect.sessions.new(
            customer_id="x",
            customer_name="x",
            products=["company"],
            customer_email="dev@stainless.com",
            integration={
                "auth_method": "assisted",
                "provider": "provider",
            },
            manual=True,
            minutes_to_expire=1,
            redirect_uri="redirect_uri",
            sandbox="finch",
        )
        assert_matches_type(SessionNewResponse, session, path=["response"])

    @parametrize
    def test_raw_response_new(self, client: Finch) -> None:
        response = client.connect.sessions.with_raw_response.new(
            customer_id="x",
            customer_name="x",
            products=["company"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionNewResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_new(self, client: Finch) -> None:
        with client.connect.sessions.with_streaming_response.new(
            customer_id="x",
            customer_name="x",
            products=["company"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionNewResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_reauthenticate(self, client: Finch) -> None:
        session = client.connect.sessions.reauthenticate(
            connection_id="connection_id",
        )
        assert_matches_type(SessionReauthenticateResponse, session, path=["response"])

    @parametrize
    def test_method_reauthenticate_with_all_params(self, client: Finch) -> None:
        session = client.connect.sessions.reauthenticate(
            connection_id="connection_id",
            minutes_to_expire=0,
            products=["company"],
            redirect_uri="https://example.com",
        )
        assert_matches_type(SessionReauthenticateResponse, session, path=["response"])

    @parametrize
    def test_raw_response_reauthenticate(self, client: Finch) -> None:
        response = client.connect.sessions.with_raw_response.reauthenticate(
            connection_id="connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionReauthenticateResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_reauthenticate(self, client: Finch) -> None:
        with client.connect.sessions.with_streaming_response.reauthenticate(
            connection_id="connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionReauthenticateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_new(self, async_client: AsyncFinch) -> None:
        session = await async_client.connect.sessions.new(
            customer_id="x",
            customer_name="x",
            products=["company"],
        )
        assert_matches_type(SessionNewResponse, session, path=["response"])

    @parametrize
    async def test_method_new_with_all_params(self, async_client: AsyncFinch) -> None:
        session = await async_client.connect.sessions.new(
            customer_id="x",
            customer_name="x",
            products=["company"],
            customer_email="dev@stainless.com",
            integration={
                "auth_method": "assisted",
                "provider": "provider",
            },
            manual=True,
            minutes_to_expire=1,
            redirect_uri="redirect_uri",
            sandbox="finch",
        )
        assert_matches_type(SessionNewResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_new(self, async_client: AsyncFinch) -> None:
        response = await async_client.connect.sessions.with_raw_response.new(
            customer_id="x",
            customer_name="x",
            products=["company"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionNewResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_new(self, async_client: AsyncFinch) -> None:
        async with async_client.connect.sessions.with_streaming_response.new(
            customer_id="x",
            customer_name="x",
            products=["company"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionNewResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_reauthenticate(self, async_client: AsyncFinch) -> None:
        session = await async_client.connect.sessions.reauthenticate(
            connection_id="connection_id",
        )
        assert_matches_type(SessionReauthenticateResponse, session, path=["response"])

    @parametrize
    async def test_method_reauthenticate_with_all_params(self, async_client: AsyncFinch) -> None:
        session = await async_client.connect.sessions.reauthenticate(
            connection_id="connection_id",
            minutes_to_expire=0,
            products=["company"],
            redirect_uri="https://example.com",
        )
        assert_matches_type(SessionReauthenticateResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_reauthenticate(self, async_client: AsyncFinch) -> None:
        response = await async_client.connect.sessions.with_raw_response.reauthenticate(
            connection_id="connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionReauthenticateResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_reauthenticate(self, async_client: AsyncFinch) -> None:
        async with async_client.connect.sessions.with_streaming_response.reauthenticate(
            connection_id="connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionReauthenticateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True
