# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.pagination import SyncResponsesPage, AsyncResponsesPage
from finch.types.hris import IndividualResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
access_token = os.environ.get("API_KEY", "something1234")


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
