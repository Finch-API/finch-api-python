# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._utils import parse_date
from finch.pagination import SyncResponsesPage, AsyncResponsesPage
from finch.types.hris.company import PayStatementItemListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayStatementItem:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Finch) -> None:
        pay_statement_item = client.hris.company.pay_statement_item.list()
        assert_matches_type(SyncResponsesPage[PayStatementItemListResponse], pay_statement_item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Finch) -> None:
        pay_statement_item = client.hris.company.pay_statement_item.list(
            categories=["earnings"],
            end_date=parse_date("2024-07-01"),
            name="name",
            start_date=parse_date("2024-01-01"),
            type="base_compensation",
        )
        assert_matches_type(SyncResponsesPage[PayStatementItemListResponse], pay_statement_item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Finch) -> None:
        response = client.hris.company.pay_statement_item.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_statement_item = response.parse()
        assert_matches_type(SyncResponsesPage[PayStatementItemListResponse], pay_statement_item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Finch) -> None:
        with client.hris.company.pay_statement_item.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_statement_item = response.parse()
            assert_matches_type(SyncResponsesPage[PayStatementItemListResponse], pay_statement_item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayStatementItem:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncFinch) -> None:
        pay_statement_item = await async_client.hris.company.pay_statement_item.list()
        assert_matches_type(AsyncResponsesPage[PayStatementItemListResponse], pay_statement_item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFinch) -> None:
        pay_statement_item = await async_client.hris.company.pay_statement_item.list(
            categories=["earnings"],
            end_date=parse_date("2024-07-01"),
            name="name",
            start_date=parse_date("2024-01-01"),
            type="base_compensation",
        )
        assert_matches_type(AsyncResponsesPage[PayStatementItemListResponse], pay_statement_item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFinch) -> None:
        response = await async_client.hris.company.pay_statement_item.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_statement_item = response.parse()
        assert_matches_type(AsyncResponsesPage[PayStatementItemListResponse], pay_statement_item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFinch) -> None:
        async with async_client.hris.company.pay_statement_item.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_statement_item = await response.parse()
            assert_matches_type(AsyncResponsesPage[PayStatementItemListResponse], pay_statement_item, path=["response"])

        assert cast(Any, response.is_closed) is True
