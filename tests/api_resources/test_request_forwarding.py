# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from finch.types import RequestForwardingForwardResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = os.environ.get("API_KEY", "something1234")


class TestRequestForwarding:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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


class TestAsyncRequestForwarding:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_forward(self, client: AsyncFinch) -> None:
        request_forwarding = await client.request_forwarding.forward(
            method="POST",
            route="/people/search",
        )
        assert_matches_type(RequestForwardingForwardResponse, request_forwarding, path=["response"])

    @parametrize
    async def test_method_forward_with_all_params(self, client: AsyncFinch) -> None:
        request_forwarding = await client.request_forwarding.forward(
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
