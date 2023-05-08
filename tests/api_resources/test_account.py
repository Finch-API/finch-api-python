# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from finch.types import Introspection, DisconnectResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
access_token = os.environ.get("API_KEY", "something1234")


class TestAccount:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_disconnect(self, client: Finch) -> None:
        account = client.account.disconnect()
        assert_matches_type(DisconnectResponse, account, path=["response"])

    @parametrize
    def test_method_introspect(self, client: Finch) -> None:
        account = client.account.introspect()
        assert_matches_type(Introspection, account, path=["response"])


class TestAsyncAccount:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_disconnect(self, client: AsyncFinch) -> None:
        account = await client.account.disconnect()
        assert_matches_type(DisconnectResponse, account, path=["response"])

    @parametrize
    async def test_method_introspect(self, client: AsyncFinch) -> None:
        account = await client.account.introspect()
        assert_matches_type(Introspection, account, path=["response"])
