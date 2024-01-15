# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._client import Finch, AsyncFinch
from finch.pagination import SyncResponsesPage, AsyncResponsesPage
from finch.types.hris import IndividualResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestIndividuals:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve_many(self, client: Finch) -> None:
        individual = client.hris.individuals.retrieve_many()
        assert_matches_type(SyncResponsesPage[IndividualResponse], individual, path=["response"])

    @parametrize
    def test_method_retrieve_many_with_all_params(self, client: Finch) -> None:
        individual = client.hris.individuals.retrieve_many(
            options={"include": ["string", "string", "string"]},
            requests=[{"individual_id": "string"}, {"individual_id": "string"}, {"individual_id": "string"}],
        )
        assert_matches_type(SyncResponsesPage[IndividualResponse], individual, path=["response"])

    @parametrize
    def test_raw_response_retrieve_many(self, client: Finch) -> None:
        response = client.hris.individuals.with_raw_response.retrieve_many()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        individual = response.parse()
        assert_matches_type(SyncResponsesPage[IndividualResponse], individual, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_many(self, client: Finch) -> None:
        with client.hris.individuals.with_streaming_response.retrieve_many() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            individual = response.parse()
            assert_matches_type(SyncResponsesPage[IndividualResponse], individual, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIndividuals:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve_many(self, client: AsyncFinch) -> None:
        individual = await client.hris.individuals.retrieve_many()
        assert_matches_type(AsyncResponsesPage[IndividualResponse], individual, path=["response"])

    @parametrize
    async def test_method_retrieve_many_with_all_params(self, client: AsyncFinch) -> None:
        individual = await client.hris.individuals.retrieve_many(
            options={"include": ["string", "string", "string"]},
            requests=[{"individual_id": "string"}, {"individual_id": "string"}, {"individual_id": "string"}],
        )
        assert_matches_type(AsyncResponsesPage[IndividualResponse], individual, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_many(self, client: AsyncFinch) -> None:
        response = await client.hris.individuals.with_raw_response.retrieve_many()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        individual = response.parse()
        assert_matches_type(AsyncResponsesPage[IndividualResponse], individual, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_many(self, client: AsyncFinch) -> None:
        async with client.hris.individuals.with_streaming_response.retrieve_many() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            individual = await response.parse()
            assert_matches_type(AsyncResponsesPage[IndividualResponse], individual, path=["response"])

        assert cast(Any, response.is_closed) is True
