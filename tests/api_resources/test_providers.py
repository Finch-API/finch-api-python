# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from finch.types import Provider
from tests.utils import assert_matches_type
from finch._client import Finch, AsyncFinch
from finch.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestProviders:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Finch) -> None:
        provider = client.providers.list()
        assert_matches_type(SyncSinglePage[Provider], provider, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Finch) -> None:
        response = client.providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(SyncSinglePage[Provider], provider, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Finch) -> None:
        with client.providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(SyncSinglePage[Provider], provider, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProviders:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncFinch) -> None:
        provider = await client.providers.list()
        assert_matches_type(AsyncSinglePage[Provider], provider, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncFinch) -> None:
        response = await client.providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(AsyncSinglePage[Provider], provider, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncFinch) -> None:
        async with client.providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(AsyncSinglePage[Provider], provider, path=["response"])

        assert cast(Any, response.is_closed) is True
