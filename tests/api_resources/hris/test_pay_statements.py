# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.pagination import SyncResponsesPage, AsyncResponsesPage
from finch.types.hris import PayStatementResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestPayStatements:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve_many(self, client: Finch) -> None:
        pay_statement = client.hris.pay_statements.retrieve_many(
            requests=[
                {"payment_id": "e8b90071-0c11-471c-86e8-e303ef2f6782"},
                {"payment_id": "e8b90071-0c11-471c-86e8-e303ef2f6782"},
                {"payment_id": "e8b90071-0c11-471c-86e8-e303ef2f6782"},
            ],
        )
        assert_matches_type(SyncResponsesPage[PayStatementResponse], pay_statement, path=["response"])


class TestAsyncPayStatements:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve_many(self, client: AsyncFinch) -> None:
        pay_statement = await client.hris.pay_statements.retrieve_many(
            requests=[
                {"payment_id": "e8b90071-0c11-471c-86e8-e303ef2f6782"},
                {"payment_id": "e8b90071-0c11-471c-86e8-e303ef2f6782"},
                {"payment_id": "e8b90071-0c11-471c-86e8-e303ef2f6782"},
            ],
        )
        assert_matches_type(AsyncResponsesPage[PayStatementResponse], pay_statement, path=["response"])
