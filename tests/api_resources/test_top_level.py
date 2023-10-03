# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from finch.types import ForwardResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = os.environ.get("API_KEY", "something1234")


class TestTopLevel:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_forward(self, client: Finch) -> None:
        top_level = client.forward(
            method="string",
            route="string",
        )
        assert_matches_type(ForwardResponse, top_level, path=["response"])

    @parametrize
    def test_method_forward_with_all_params(self, client: Finch) -> None:
        top_level = client.forward(
            method="string",
            route="string",
            data="string",
            headers={},
            params={},
        )
        assert_matches_type(ForwardResponse, top_level, path=["response"])


class TestAsyncTopLevel:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_forward(self, client: AsyncFinch) -> None:
        top_level = await client.forward(
            method="string",
            route="string",
        )
        assert_matches_type(ForwardResponse, top_level, path=["response"])

    @parametrize
    async def test_method_forward_with_all_params(self, client: AsyncFinch) -> None:
        top_level = await client.forward(
            method="string",
            route="string",
            data="string",
            headers={},
            params={},
        )
        assert_matches_type(ForwardResponse, top_level, path=["response"])
