# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._client import Finch, AsyncFinch
from finch.pagination import SyncIndividualsPage, AsyncIndividualsPage
from finch.types.hris import IndividualInDirectory

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestDirectory:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Finch) -> None:
        directory = client.hris.directory.list()
        assert_matches_type(SyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Finch) -> None:
        directory = client.hris.directory.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Finch) -> None:
        response = client.hris.directory.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert_matches_type(SyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Finch) -> None:
        with client.hris.directory.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = response.parse()
            assert_matches_type(SyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_individuals(self, client: Finch) -> None:
        with pytest.warns(DeprecationWarning):
            directory = client.hris.directory.list_individuals()

        assert_matches_type(SyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

    @parametrize
    def test_method_list_individuals_with_all_params(self, client: Finch) -> None:
        with pytest.warns(DeprecationWarning):
            directory = client.hris.directory.list_individuals(
                limit=0,
                offset=0,
            )

        assert_matches_type(SyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

    @parametrize
    def test_raw_response_list_individuals(self, client: Finch) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.hris.directory.with_raw_response.list_individuals()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert_matches_type(SyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

    @parametrize
    def test_streaming_response_list_individuals(self, client: Finch) -> None:
        with pytest.warns(DeprecationWarning):
            with client.hris.directory.with_streaming_response.list_individuals() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                directory = response.parse()
                assert_matches_type(SyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDirectory:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncFinch) -> None:
        directory = await client.hris.directory.list()
        assert_matches_type(AsyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncFinch) -> None:
        directory = await client.hris.directory.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncFinch) -> None:
        response = await client.hris.directory.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert_matches_type(AsyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncFinch) -> None:
        async with client.hris.directory.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = await response.parse()
            assert_matches_type(AsyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_individuals(self, client: AsyncFinch) -> None:
        with pytest.warns(DeprecationWarning):
            directory = await client.hris.directory.list_individuals()

        assert_matches_type(AsyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

    @parametrize
    async def test_method_list_individuals_with_all_params(self, client: AsyncFinch) -> None:
        with pytest.warns(DeprecationWarning):
            directory = await client.hris.directory.list_individuals(
                limit=0,
                offset=0,
            )

        assert_matches_type(AsyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

    @parametrize
    async def test_raw_response_list_individuals(self, client: AsyncFinch) -> None:
        with pytest.warns(DeprecationWarning):
            response = await client.hris.directory.with_raw_response.list_individuals()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert_matches_type(AsyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

    @parametrize
    async def test_streaming_response_list_individuals(self, client: AsyncFinch) -> None:
        with pytest.warns(DeprecationWarning):
            async with client.hris.directory.with_streaming_response.list_individuals() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                directory = await response.parse()
                assert_matches_type(AsyncIndividualsPage[IndividualInDirectory], directory, path=["response"])

        assert cast(Any, response.is_closed) is True
