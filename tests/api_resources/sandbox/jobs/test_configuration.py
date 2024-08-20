# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.sandbox.jobs import SandboxJobConfiguration, ConfigurationRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfiguration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Finch) -> None:
        configuration = client.sandbox.jobs.configuration.retrieve()
        assert_matches_type(ConfigurationRetrieveResponse, configuration, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Finch) -> None:
        response = client.sandbox.jobs.configuration.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationRetrieveResponse, configuration, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Finch) -> None:
        with client.sandbox.jobs.configuration.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationRetrieveResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Finch) -> None:
        configuration = client.sandbox.jobs.configuration.update(
            completion_status="complete",
            type="data_sync_all",
        )
        assert_matches_type(SandboxJobConfiguration, configuration, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Finch) -> None:
        response = client.sandbox.jobs.configuration.with_raw_response.update(
            completion_status="complete",
            type="data_sync_all",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(SandboxJobConfiguration, configuration, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Finch) -> None:
        with client.sandbox.jobs.configuration.with_streaming_response.update(
            completion_status="complete",
            type="data_sync_all",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(SandboxJobConfiguration, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfiguration:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFinch) -> None:
        configuration = await async_client.sandbox.jobs.configuration.retrieve()
        assert_matches_type(ConfigurationRetrieveResponse, configuration, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFinch) -> None:
        response = await async_client.sandbox.jobs.configuration.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationRetrieveResponse, configuration, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFinch) -> None:
        async with async_client.sandbox.jobs.configuration.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationRetrieveResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncFinch) -> None:
        configuration = await async_client.sandbox.jobs.configuration.update(
            completion_status="complete",
            type="data_sync_all",
        )
        assert_matches_type(SandboxJobConfiguration, configuration, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFinch) -> None:
        response = await async_client.sandbox.jobs.configuration.with_raw_response.update(
            completion_status="complete",
            type="data_sync_all",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(SandboxJobConfiguration, configuration, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFinch) -> None:
        async with async_client.sandbox.jobs.configuration.with_streaming_response.update(
            completion_status="complete",
            type="data_sync_all",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(SandboxJobConfiguration, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True
