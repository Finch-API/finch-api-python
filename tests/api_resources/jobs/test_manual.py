# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.jobs import ManualAsyncJob

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestManual:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Finch) -> None:
        manual = client.jobs.manual.retrieve(
            job_id="job_id",
        )
        assert_matches_type(ManualAsyncJob, manual, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Finch) -> None:
        manual = client.jobs.manual.retrieve(
            job_id="job_id",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ManualAsyncJob, manual, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Finch) -> None:
        response = client.jobs.manual.with_raw_response.retrieve(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manual = response.parse()
        assert_matches_type(ManualAsyncJob, manual, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Finch) -> None:
        with client.jobs.manual.with_streaming_response.retrieve(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manual = response.parse()
            assert_matches_type(ManualAsyncJob, manual, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Finch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.jobs.manual.with_raw_response.retrieve(
                job_id="",
            )


class TestAsyncManual:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFinch) -> None:
        manual = await async_client.jobs.manual.retrieve(
            job_id="job_id",
        )
        assert_matches_type(ManualAsyncJob, manual, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncFinch) -> None:
        manual = await async_client.jobs.manual.retrieve(
            job_id="job_id",
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ManualAsyncJob, manual, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFinch) -> None:
        response = await async_client.jobs.manual.with_raw_response.retrieve(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manual = response.parse()
        assert_matches_type(ManualAsyncJob, manual, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFinch) -> None:
        async with async_client.jobs.manual.with_streaming_response.retrieve(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manual = await response.parse()
            assert_matches_type(ManualAsyncJob, manual, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFinch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.jobs.manual.with_raw_response.retrieve(
                job_id="",
            )
