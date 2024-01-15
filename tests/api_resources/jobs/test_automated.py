# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._client import Finch, AsyncFinch
from finch.pagination import SyncPage, AsyncPage
from finch.types.jobs import AutomatedAsyncJob, AutomatedCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestAutomated:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Finch) -> None:
        automated = client.jobs.automated.create(
            type="data_sync_all",
        )
        assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Finch) -> None:
        response = client.jobs.automated.with_raw_response.create(
            type="data_sync_all",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automated = response.parse()
        assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Finch) -> None:
        with client.jobs.automated.with_streaming_response.create(
            type="data_sync_all",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automated = response.parse()
            assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Finch) -> None:
        automated = client.jobs.automated.retrieve(
            "string",
        )
        assert_matches_type(AutomatedAsyncJob, automated, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Finch) -> None:
        response = client.jobs.automated.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automated = response.parse()
        assert_matches_type(AutomatedAsyncJob, automated, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Finch) -> None:
        with client.jobs.automated.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automated = response.parse()
            assert_matches_type(AutomatedAsyncJob, automated, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Finch) -> None:
        automated = client.jobs.automated.list()
        assert_matches_type(SyncPage[AutomatedAsyncJob], automated, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Finch) -> None:
        automated = client.jobs.automated.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncPage[AutomatedAsyncJob], automated, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Finch) -> None:
        response = client.jobs.automated.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automated = response.parse()
        assert_matches_type(SyncPage[AutomatedAsyncJob], automated, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Finch) -> None:
        with client.jobs.automated.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automated = response.parse()
            assert_matches_type(SyncPage[AutomatedAsyncJob], automated, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAutomated:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncFinch) -> None:
        automated = await client.jobs.automated.create(
            type="data_sync_all",
        )
        assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncFinch) -> None:
        response = await client.jobs.automated.with_raw_response.create(
            type="data_sync_all",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automated = response.parse()
        assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncFinch) -> None:
        async with client.jobs.automated.with_streaming_response.create(
            type="data_sync_all",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automated = await response.parse()
            assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncFinch) -> None:
        automated = await client.jobs.automated.retrieve(
            "string",
        )
        assert_matches_type(AutomatedAsyncJob, automated, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncFinch) -> None:
        response = await client.jobs.automated.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automated = response.parse()
        assert_matches_type(AutomatedAsyncJob, automated, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncFinch) -> None:
        async with client.jobs.automated.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automated = await response.parse()
            assert_matches_type(AutomatedAsyncJob, automated, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncFinch) -> None:
        automated = await client.jobs.automated.list()
        assert_matches_type(AsyncPage[AutomatedAsyncJob], automated, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncFinch) -> None:
        automated = await client.jobs.automated.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncPage[AutomatedAsyncJob], automated, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncFinch) -> None:
        response = await client.jobs.automated.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automated = response.parse()
        assert_matches_type(AsyncPage[AutomatedAsyncJob], automated, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncFinch) -> None:
        async with client.jobs.automated.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automated = await response.parse()
            assert_matches_type(AsyncPage[AutomatedAsyncJob], automated, path=["response"])

        assert cast(Any, response.is_closed) is True
