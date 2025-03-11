# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.jobs import (
    AutomatedAsyncJob,
    AutomatedListResponse,
    AutomatedCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutomated:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Finch) -> None:
        automated = client.jobs.automated.create(
            type="data_sync_all",
        )
        assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Finch) -> None:
        response = client.jobs.automated.with_raw_response.create(
            type="data_sync_all",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automated = response.parse()
        assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Finch) -> None:
        with client.jobs.automated.with_streaming_response.create(
            type="data_sync_all",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automated = response.parse()
            assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Finch) -> None:
        automated = client.jobs.automated.create(
            params={"individual_id": "individual_id"},
            type="w4_form_employee_sync",
        )
        assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Finch) -> None:
        response = client.jobs.automated.with_raw_response.create(
            params={"individual_id": "individual_id"},
            type="w4_form_employee_sync",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automated = response.parse()
        assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Finch) -> None:
        with client.jobs.automated.with_streaming_response.create(
            params={"individual_id": "individual_id"},
            type="w4_form_employee_sync",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automated = response.parse()
            assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Finch) -> None:
        automated = client.jobs.automated.retrieve(
            "job_id",
        )
        assert_matches_type(AutomatedAsyncJob, automated, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Finch) -> None:
        response = client.jobs.automated.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automated = response.parse()
        assert_matches_type(AutomatedAsyncJob, automated, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Finch) -> None:
        with client.jobs.automated.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automated = response.parse()
            assert_matches_type(AutomatedAsyncJob, automated, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Finch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.jobs.automated.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Finch) -> None:
        automated = client.jobs.automated.list()
        assert_matches_type(AutomatedListResponse, automated, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Finch) -> None:
        automated = client.jobs.automated.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(AutomatedListResponse, automated, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Finch) -> None:
        response = client.jobs.automated.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automated = response.parse()
        assert_matches_type(AutomatedListResponse, automated, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Finch) -> None:
        with client.jobs.automated.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automated = response.parse()
            assert_matches_type(AutomatedListResponse, automated, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAutomated:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncFinch) -> None:
        automated = await async_client.jobs.automated.create(
            type="data_sync_all",
        )
        assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncFinch) -> None:
        response = await async_client.jobs.automated.with_raw_response.create(
            type="data_sync_all",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automated = response.parse()
        assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncFinch) -> None:
        async with async_client.jobs.automated.with_streaming_response.create(
            type="data_sync_all",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automated = await response.parse()
            assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncFinch) -> None:
        automated = await async_client.jobs.automated.create(
            params={"individual_id": "individual_id"},
            type="w4_form_employee_sync",
        )
        assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncFinch) -> None:
        response = await async_client.jobs.automated.with_raw_response.create(
            params={"individual_id": "individual_id"},
            type="w4_form_employee_sync",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automated = response.parse()
        assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncFinch) -> None:
        async with async_client.jobs.automated.with_streaming_response.create(
            params={"individual_id": "individual_id"},
            type="w4_form_employee_sync",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automated = await response.parse()
            assert_matches_type(AutomatedCreateResponse, automated, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFinch) -> None:
        automated = await async_client.jobs.automated.retrieve(
            "job_id",
        )
        assert_matches_type(AutomatedAsyncJob, automated, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFinch) -> None:
        response = await async_client.jobs.automated.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automated = response.parse()
        assert_matches_type(AutomatedAsyncJob, automated, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFinch) -> None:
        async with async_client.jobs.automated.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automated = await response.parse()
            assert_matches_type(AutomatedAsyncJob, automated, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFinch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.jobs.automated.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncFinch) -> None:
        automated = await async_client.jobs.automated.list()
        assert_matches_type(AutomatedListResponse, automated, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFinch) -> None:
        automated = await async_client.jobs.automated.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(AutomatedListResponse, automated, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFinch) -> None:
        response = await async_client.jobs.automated.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automated = response.parse()
        assert_matches_type(AutomatedListResponse, automated, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFinch) -> None:
        async with async_client.jobs.automated.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automated = await response.parse()
            assert_matches_type(AutomatedListResponse, automated, path=["response"])

        assert cast(Any, response.is_closed) is True
