# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._client import Finch, AsyncFinch
from finch.pagination import SyncResponsesPage, AsyncResponsesPage
from finch.types.hris import EmploymentDataResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestEmployments:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve_many(self, client: Finch) -> None:
        employment = client.hris.employments.retrieve_many(
            requests=[{"individual_id": "string"}, {"individual_id": "string"}, {"individual_id": "string"}],
        )
        assert_matches_type(SyncResponsesPage[EmploymentDataResponse], employment, path=["response"])

    @parametrize
    def test_raw_response_retrieve_many(self, client: Finch) -> None:
        response = client.hris.employments.with_raw_response.retrieve_many(
            requests=[{"individual_id": "string"}, {"individual_id": "string"}, {"individual_id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = response.parse()
        assert_matches_type(SyncResponsesPage[EmploymentDataResponse], employment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_many(self, client: Finch) -> None:
        with client.hris.employments.with_streaming_response.retrieve_many(
            requests=[{"individual_id": "string"}, {"individual_id": "string"}, {"individual_id": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employment = response.parse()
            assert_matches_type(SyncResponsesPage[EmploymentDataResponse], employment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmployments:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve_many(self, client: AsyncFinch) -> None:
        employment = await client.hris.employments.retrieve_many(
            requests=[{"individual_id": "string"}, {"individual_id": "string"}, {"individual_id": "string"}],
        )
        assert_matches_type(AsyncResponsesPage[EmploymentDataResponse], employment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_many(self, client: AsyncFinch) -> None:
        response = await client.hris.employments.with_raw_response.retrieve_many(
            requests=[{"individual_id": "string"}, {"individual_id": "string"}, {"individual_id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = response.parse()
        assert_matches_type(AsyncResponsesPage[EmploymentDataResponse], employment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_many(self, client: AsyncFinch) -> None:
        async with client.hris.employments.with_streaming_response.retrieve_many(
            requests=[{"individual_id": "string"}, {"individual_id": "string"}, {"individual_id": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employment = await response.parse()
            assert_matches_type(AsyncResponsesPage[EmploymentDataResponse], employment, path=["response"])

        assert cast(Any, response.is_closed) is True
