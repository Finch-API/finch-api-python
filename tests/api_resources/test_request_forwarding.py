# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from finch.types import RequestForwardingForwardResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRequestForwarding:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_forward(self, client: Finch) -> None:
        request_forwarding = client.request_forwarding.forward(
            method="POST",
            route="/people/search",
        )
        assert_matches_type(RequestForwardingForwardResponse, request_forwarding, path=["response"])

    @parametrize
    def test_method_forward_with_all_params(self, client: Finch) -> None:
        request_forwarding = client.request_forwarding.forward(
            method="POST",
            route="/people/search",
            data=None,
            headers={"content-type": "application/json"},
            params={
                "showInactive": True,
                "humanReadable": True,
            },
        )
        assert_matches_type(RequestForwardingForwardResponse, request_forwarding, path=["response"])

    @parametrize
    def test_raw_response_forward(self, client: Finch) -> None:
        response = client.request_forwarding.with_raw_response.forward(
            method="POST",
            route="/people/search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request_forwarding = response.parse()
        assert_matches_type(RequestForwardingForwardResponse, request_forwarding, path=["response"])

    @parametrize
    def test_streaming_response_forward(self, client: Finch) -> None:
        with client.request_forwarding.with_streaming_response.forward(
            method="POST",
            route="/people/search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request_forwarding = response.parse()
            assert_matches_type(RequestForwardingForwardResponse, request_forwarding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRequestForwarding:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_forward(self, async_client: AsyncFinch) -> None:
        request_forwarding = await async_client.request_forwarding.forward(
            method="POST",
            route="/people/search",
        )
        assert_matches_type(RequestForwardingForwardResponse, request_forwarding, path=["response"])

    @parametrize
    async def test_method_forward_with_all_params(self, async_client: AsyncFinch) -> None:
        request_forwarding = await async_client.request_forwarding.forward(
            method="POST",
            route="/people/search",
            data=None,
            headers={"content-type": "application/json"},
            params={
                "showInactive": True,
                "humanReadable": True,
            },
        )
        assert_matches_type(RequestForwardingForwardResponse, request_forwarding, path=["response"])

    @parametrize
    async def test_raw_response_forward(self, async_client: AsyncFinch) -> None:
        response = await async_client.request_forwarding.with_raw_response.forward(
            method="POST",
            route="/people/search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request_forwarding = response.parse()
        assert_matches_type(RequestForwardingForwardResponse, request_forwarding, path=["response"])

    @parametrize
    async def test_streaming_response_forward(self, async_client: AsyncFinch) -> None:
        async with async_client.request_forwarding.with_streaming_response.forward(
            method="POST",
            route="/people/search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request_forwarding = await response.parse()
            assert_matches_type(RequestForwardingForwardResponse, request_forwarding, path=["response"])

        assert cast(Any, response.is_closed) is True
