# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._client import Finch, AsyncFinch
from finch.types.jobs import ManualAsyncJob

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestManual:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Finch) -> None:
        manual = client.jobs.manual.retrieve(
            "string",
        )
        assert_matches_type(ManualAsyncJob, manual, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Finch) -> None:
        response = client.jobs.manual.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manual = response.parse()
        assert_matches_type(ManualAsyncJob, manual, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Finch) -> None:
        with client.jobs.manual.with_streaming_response.retrieve(
            "string",
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
                "",
            )


class TestAsyncManual:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncFinch) -> None:
        manual = await client.jobs.manual.retrieve(
            "string",
        )
        assert_matches_type(ManualAsyncJob, manual, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncFinch) -> None:
        response = await client.jobs.manual.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        manual = response.parse()
        assert_matches_type(ManualAsyncJob, manual, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncFinch) -> None:
        async with client.jobs.manual.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            manual = await response.parse()
            assert_matches_type(ManualAsyncJob, manual, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, client: AsyncFinch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await client.jobs.manual.with_raw_response.retrieve(
                "",
            )
