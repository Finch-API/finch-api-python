# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.sandbox import JobCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Finch) -> None:
        job = client.sandbox.jobs.create(
            type="data_sync_all",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Finch) -> None:
        response = client.sandbox.jobs.with_raw_response.create(
            type="data_sync_all",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Finch) -> None:
        with client.sandbox.jobs.with_streaming_response.create(
            type="data_sync_all",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncFinch) -> None:
        job = await async_client.sandbox.jobs.create(
            type="data_sync_all",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFinch) -> None:
        response = await async_client.sandbox.jobs.with_raw_response.create(
            type="data_sync_all",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFinch) -> None:
        async with async_client.sandbox.jobs.with_streaming_response.create(
            type="data_sync_all",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True
