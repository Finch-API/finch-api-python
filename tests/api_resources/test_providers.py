# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from finch.types import Provider
from tests.utils import assert_matches_type
from finch.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProviders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncFinch) -> None:
        provider = await async_client.providers.list()
        assert_matches_type(AsyncSinglePage[Provider], provider, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFinch) -> None:
        response = await async_client.providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(AsyncSinglePage[Provider], provider, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFinch) -> None:
        async with async_client.providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(AsyncSinglePage[Provider], provider, path=["response"])

        assert cast(Any, response.is_closed) is True
