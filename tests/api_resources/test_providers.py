# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from finch.types import Provider
from tests.utils import assert_matches_type
from finch.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = os.environ.get("API_KEY", "something1234")


class TestProviders:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Finch) -> None:
        provider = client.providers.list()
        assert_matches_type(SyncSinglePage[Provider], provider, path=["response"])


class TestAsyncProviders:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncFinch) -> None:
        provider = await client.providers.list()
        assert_matches_type(AsyncSinglePage[Provider], provider, path=["response"])
