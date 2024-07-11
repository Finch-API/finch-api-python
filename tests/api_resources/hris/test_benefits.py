# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.pagination import SyncSinglePage, AsyncSinglePage
from finch.types.hris import (
    CompanyBenefit,
    SupportedBenefit,
    UpdateCompanyBenefitResponse,
    CreateCompanyBenefitsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBenefits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Finch) -> None:
        benefit = client.hris.benefits.create()
        assert_matches_type(CreateCompanyBenefitsResponse, benefit, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Finch) -> None:
        benefit = client.hris.benefits.create(
            description="description",
            frequency="one_time",
            type="401k",
        )
        assert_matches_type(CreateCompanyBenefitsResponse, benefit, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Finch) -> None:
        response = client.hris.benefits.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit = response.parse()
        assert_matches_type(CreateCompanyBenefitsResponse, benefit, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Finch) -> None:
        with client.hris.benefits.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit = response.parse()
            assert_matches_type(CreateCompanyBenefitsResponse, benefit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Finch) -> None:
        benefit = client.hris.benefits.retrieve(
            "benefit_id",
        )
        assert_matches_type(CompanyBenefit, benefit, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Finch) -> None:
        response = client.hris.benefits.with_raw_response.retrieve(
            "benefit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit = response.parse()
        assert_matches_type(CompanyBenefit, benefit, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Finch) -> None:
        with client.hris.benefits.with_streaming_response.retrieve(
            "benefit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit = response.parse()
            assert_matches_type(CompanyBenefit, benefit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Finch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benefit_id` but received ''"):
            client.hris.benefits.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Finch) -> None:
        benefit = client.hris.benefits.update(
            benefit_id="benefit_id",
        )
        assert_matches_type(UpdateCompanyBenefitResponse, benefit, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Finch) -> None:
        benefit = client.hris.benefits.update(
            benefit_id="benefit_id",
            description="description",
        )
        assert_matches_type(UpdateCompanyBenefitResponse, benefit, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Finch) -> None:
        response = client.hris.benefits.with_raw_response.update(
            benefit_id="benefit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit = response.parse()
        assert_matches_type(UpdateCompanyBenefitResponse, benefit, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Finch) -> None:
        with client.hris.benefits.with_streaming_response.update(
            benefit_id="benefit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit = response.parse()
            assert_matches_type(UpdateCompanyBenefitResponse, benefit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Finch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benefit_id` but received ''"):
            client.hris.benefits.with_raw_response.update(
                benefit_id="",
            )

    @parametrize
    def test_method_list(self, client: Finch) -> None:
        benefit = client.hris.benefits.list()
        assert_matches_type(SyncSinglePage[CompanyBenefit], benefit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Finch) -> None:
        response = client.hris.benefits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit = response.parse()
        assert_matches_type(SyncSinglePage[CompanyBenefit], benefit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Finch) -> None:
        with client.hris.benefits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit = response.parse()
            assert_matches_type(SyncSinglePage[CompanyBenefit], benefit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_supported_benefits(self, client: Finch) -> None:
        benefit = client.hris.benefits.list_supported_benefits()
        assert_matches_type(SyncSinglePage[SupportedBenefit], benefit, path=["response"])

    @parametrize
    def test_raw_response_list_supported_benefits(self, client: Finch) -> None:
        response = client.hris.benefits.with_raw_response.list_supported_benefits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit = response.parse()
        assert_matches_type(SyncSinglePage[SupportedBenefit], benefit, path=["response"])

    @parametrize
    def test_streaming_response_list_supported_benefits(self, client: Finch) -> None:
        with client.hris.benefits.with_streaming_response.list_supported_benefits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit = response.parse()
            assert_matches_type(SyncSinglePage[SupportedBenefit], benefit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBenefits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFinch) -> None:
        benefit = await async_client.hris.benefits.create()
        assert_matches_type(CreateCompanyBenefitsResponse, benefit, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFinch) -> None:
        benefit = await async_client.hris.benefits.create(
            description="description",
            frequency="one_time",
            type="401k",
        )
        assert_matches_type(CreateCompanyBenefitsResponse, benefit, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFinch) -> None:
        response = await async_client.hris.benefits.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit = response.parse()
        assert_matches_type(CreateCompanyBenefitsResponse, benefit, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFinch) -> None:
        async with async_client.hris.benefits.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit = await response.parse()
            assert_matches_type(CreateCompanyBenefitsResponse, benefit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFinch) -> None:
        benefit = await async_client.hris.benefits.retrieve(
            "benefit_id",
        )
        assert_matches_type(CompanyBenefit, benefit, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFinch) -> None:
        response = await async_client.hris.benefits.with_raw_response.retrieve(
            "benefit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit = response.parse()
        assert_matches_type(CompanyBenefit, benefit, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFinch) -> None:
        async with async_client.hris.benefits.with_streaming_response.retrieve(
            "benefit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit = await response.parse()
            assert_matches_type(CompanyBenefit, benefit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFinch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benefit_id` but received ''"):
            await async_client.hris.benefits.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncFinch) -> None:
        benefit = await async_client.hris.benefits.update(
            benefit_id="benefit_id",
        )
        assert_matches_type(UpdateCompanyBenefitResponse, benefit, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFinch) -> None:
        benefit = await async_client.hris.benefits.update(
            benefit_id="benefit_id",
            description="description",
        )
        assert_matches_type(UpdateCompanyBenefitResponse, benefit, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFinch) -> None:
        response = await async_client.hris.benefits.with_raw_response.update(
            benefit_id="benefit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit = response.parse()
        assert_matches_type(UpdateCompanyBenefitResponse, benefit, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFinch) -> None:
        async with async_client.hris.benefits.with_streaming_response.update(
            benefit_id="benefit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit = await response.parse()
            assert_matches_type(UpdateCompanyBenefitResponse, benefit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncFinch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benefit_id` but received ''"):
            await async_client.hris.benefits.with_raw_response.update(
                benefit_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncFinch) -> None:
        benefit = await async_client.hris.benefits.list()
        assert_matches_type(AsyncSinglePage[CompanyBenefit], benefit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFinch) -> None:
        response = await async_client.hris.benefits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit = response.parse()
        assert_matches_type(AsyncSinglePage[CompanyBenefit], benefit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFinch) -> None:
        async with async_client.hris.benefits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit = await response.parse()
            assert_matches_type(AsyncSinglePage[CompanyBenefit], benefit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_supported_benefits(self, async_client: AsyncFinch) -> None:
        benefit = await async_client.hris.benefits.list_supported_benefits()
        assert_matches_type(AsyncSinglePage[SupportedBenefit], benefit, path=["response"])

    @parametrize
    async def test_raw_response_list_supported_benefits(self, async_client: AsyncFinch) -> None:
        response = await async_client.hris.benefits.with_raw_response.list_supported_benefits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit = response.parse()
        assert_matches_type(AsyncSinglePage[SupportedBenefit], benefit, path=["response"])

    @parametrize
    async def test_streaming_response_list_supported_benefits(self, async_client: AsyncFinch) -> None:
        async with async_client.hris.benefits.with_streaming_response.list_supported_benefits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit = await response.parse()
            assert_matches_type(AsyncSinglePage[SupportedBenefit], benefit, path=["response"])

        assert cast(Any, response.is_closed) is True
