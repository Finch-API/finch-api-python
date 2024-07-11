# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.pagination import SyncSinglePage, AsyncSinglePage
from finch.types.payroll import PayGroupListResponse, PayGroupRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Finch) -> None:
        pay_group = client.payroll.pay_groups.retrieve(
            "pay_group_id",
        )
        assert_matches_type(PayGroupRetrieveResponse, pay_group, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Finch) -> None:
        response = client.payroll.pay_groups.with_raw_response.retrieve(
            "pay_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_group = response.parse()
        assert_matches_type(PayGroupRetrieveResponse, pay_group, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Finch) -> None:
        with client.payroll.pay_groups.with_streaming_response.retrieve(
            "pay_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_group = response.parse()
            assert_matches_type(PayGroupRetrieveResponse, pay_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Finch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pay_group_id` but received ''"):
            client.payroll.pay_groups.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Finch) -> None:
        pay_group = client.payroll.pay_groups.list()
        assert_matches_type(SyncSinglePage[PayGroupListResponse], pay_group, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Finch) -> None:
        pay_group = client.payroll.pay_groups.list(
            individual_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pay_frequencies=["string", "string", "string"],
        )
        assert_matches_type(SyncSinglePage[PayGroupListResponse], pay_group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Finch) -> None:
        response = client.payroll.pay_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_group = response.parse()
        assert_matches_type(SyncSinglePage[PayGroupListResponse], pay_group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Finch) -> None:
        with client.payroll.pay_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_group = response.parse()
            assert_matches_type(SyncSinglePage[PayGroupListResponse], pay_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFinch) -> None:
        pay_group = await async_client.payroll.pay_groups.retrieve(
            "pay_group_id",
        )
        assert_matches_type(PayGroupRetrieveResponse, pay_group, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFinch) -> None:
        response = await async_client.payroll.pay_groups.with_raw_response.retrieve(
            "pay_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_group = response.parse()
        assert_matches_type(PayGroupRetrieveResponse, pay_group, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFinch) -> None:
        async with async_client.payroll.pay_groups.with_streaming_response.retrieve(
            "pay_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_group = await response.parse()
            assert_matches_type(PayGroupRetrieveResponse, pay_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFinch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pay_group_id` but received ''"):
            await async_client.payroll.pay_groups.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncFinch) -> None:
        pay_group = await async_client.payroll.pay_groups.list()
        assert_matches_type(AsyncSinglePage[PayGroupListResponse], pay_group, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFinch) -> None:
        pay_group = await async_client.payroll.pay_groups.list(
            individual_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pay_frequencies=["string", "string", "string"],
        )
        assert_matches_type(AsyncSinglePage[PayGroupListResponse], pay_group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFinch) -> None:
        response = await async_client.payroll.pay_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pay_group = response.parse()
        assert_matches_type(AsyncSinglePage[PayGroupListResponse], pay_group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFinch) -> None:
        async with async_client.payroll.pay_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pay_group = await response.parse()
            assert_matches_type(AsyncSinglePage[PayGroupListResponse], pay_group, path=["response"])

        assert cast(Any, response.is_closed) is True
