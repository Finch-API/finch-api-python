# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._utils import parse_date
from finch.pagination import SyncSinglePage, AsyncSinglePage
from finch.types.hris import Payment

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Finch) -> None:
        payment = client.hris.payments.list(
            end_date=parse_date("2021-01-01"),
            start_date=parse_date("2021-01-01"),
        )
        assert_matches_type(SyncSinglePage[Payment], payment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Finch) -> None:
        response = client.hris.payments.with_raw_response.list(
            end_date=parse_date("2021-01-01"),
            start_date=parse_date("2021-01-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(SyncSinglePage[Payment], payment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Finch) -> None:
        with client.hris.payments.with_streaming_response.list(
            end_date=parse_date("2021-01-01"),
            start_date=parse_date("2021-01-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(SyncSinglePage[Payment], payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncFinch) -> None:
        payment = await async_client.hris.payments.list(
            end_date=parse_date("2021-01-01"),
            start_date=parse_date("2021-01-01"),
        )
        assert_matches_type(AsyncSinglePage[Payment], payment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFinch) -> None:
        response = await async_client.hris.payments.with_raw_response.list(
            end_date=parse_date("2021-01-01"),
            start_date=parse_date("2021-01-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(AsyncSinglePage[Payment], payment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFinch) -> None:
        async with async_client.hris.payments.with_streaming_response.list(
            end_date=parse_date("2021-01-01"),
            start_date=parse_date("2021-01-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(AsyncSinglePage[Payment], payment, path=["response"])

        assert cast(Any, response.is_closed) is True
