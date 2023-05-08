# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._utils import parse_date
from finch.pagination import SyncSinglePage, AsyncSinglePage
from finch.types.hris import Payment

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
access_token = os.environ.get("API_KEY", "something1234")


class TestPayments:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Finch) -> None:
        payment = client.hris.payments.list(
            start_date=parse_date("2021-01-01"),
            end_date=parse_date("2021-01-01"),
        )
        assert_matches_type(SyncSinglePage[Payment], payment, path=["response"])


class TestAsyncPayments:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncFinch) -> None:
        payment = await client.hris.payments.list(
            start_date=parse_date("2021-01-01"),
            end_date=parse_date("2021-01-01"),
        )
        assert_matches_type(AsyncSinglePage[Payment], payment, path=["response"])
