# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.pagination import SyncResponsesPage, AsyncResponsesPage
from finch.types.hris import IndividualResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndividuals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_many(self, client: Finch) -> None:
        individual = client.hris.individuals.retrieve_many()
        assert_matches_type(SyncResponsesPage[IndividualResponse], individual, path=["response"])

    @parametrize
    def test_method_retrieve_many_with_all_params(self, client: Finch) -> None:
        individual = client.hris.individuals.retrieve_many(
            options={"include": ["string", "string", "string"]},
            requests=[
                {"individual_id": "individual_id"},
                {"individual_id": "individual_id"},
                {"individual_id": "individual_id"},
            ],
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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve_many(self, async_client: AsyncFinch) -> None:
        individual = await async_client.hris.individuals.retrieve_many()
        assert_matches_type(AsyncResponsesPage[IndividualResponse], individual, path=["response"])

    @parametrize
    async def test_method_retrieve_many_with_all_params(self, async_client: AsyncFinch) -> None:
        individual = await async_client.hris.individuals.retrieve_many(
            options={"include": ["string", "string", "string"]},
            requests=[
                {"individual_id": "individual_id"},
                {"individual_id": "individual_id"},
                {"individual_id": "individual_id"},
            ],
        )
        assert_matches_type(AsyncResponsesPage[IndividualResponse], individual, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_many(self, async_client: AsyncFinch) -> None:
        response = await async_client.hris.individuals.with_raw_response.retrieve_many()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        individual = response.parse()
        assert_matches_type(AsyncResponsesPage[IndividualResponse], individual, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_many(self, async_client: AsyncFinch) -> None:
        async with async_client.hris.individuals.with_streaming_response.retrieve_many() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            individual = await response.parse()
            assert_matches_type(AsyncResponsesPage[IndividualResponse], individual, path=["response"])

        assert cast(Any, response.is_closed) is True
