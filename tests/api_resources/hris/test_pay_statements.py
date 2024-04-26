# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.pagination import SyncResponsesPage, AsyncResponsesPage
from finch.types.hris import PayStatementResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayStatements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_many(self, client: Finch) -> None:
        pay_statement = client.hris.pay_statements.retrieve_many(
            requests=[{"payment_id": "string"}],
        )
        assert_matches_type(SyncResponsesPage[PayStatementResponse], pay_statement, path=["response"])

    @parametrize
    def test_raw_response_retrieve_many(self, client: Finch) -> None:
        response = client.hris.pay_statements.with_raw_response.retrieve_many(
            requests=[{"payment_id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_statement = response.parse()
        assert_matches_type(SyncResponsesPage[PayStatementResponse], pay_statement, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_many(self, client: Finch) -> None:
        with client.hris.pay_statements.with_streaming_response.retrieve_many(
            requests=[{"payment_id": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_statement = response.parse()
            assert_matches_type(SyncResponsesPage[PayStatementResponse], pay_statement, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayStatements:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve_many(self, async_client: AsyncFinch) -> None:
        pay_statement = await async_client.hris.pay_statements.retrieve_many(
            requests=[{"payment_id": "string"}],
        )
        assert_matches_type(AsyncResponsesPage[PayStatementResponse], pay_statement, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_many(self, async_client: AsyncFinch) -> None:
        response = await async_client.hris.pay_statements.with_raw_response.retrieve_many(
            requests=[{"payment_id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_statement = response.parse()
        assert_matches_type(AsyncResponsesPage[PayStatementResponse], pay_statement, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_many(self, async_client: AsyncFinch) -> None:
        async with async_client.hris.pay_statements.with_streaming_response.retrieve_many(
            requests=[{"payment_id": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_statement = await response.parse()
            assert_matches_type(AsyncResponsesPage[PayStatementResponse], pay_statement, path=["response"])

        assert cast(Any, response.is_closed) is True
