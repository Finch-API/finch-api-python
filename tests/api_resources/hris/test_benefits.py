# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

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

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
access_token = os.environ.get("API_KEY", "something1234")


class TestBenefits:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Finch) -> None:
        benefit = client.hris.benefits.create()
        assert_matches_type(CreateCompanyBenefitsResponse, benefit, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Finch) -> None:
        benefit = client.hris.benefits.create(
            type="401k",
            description="string",
            frequency="one_time",
        )
        assert_matches_type(CreateCompanyBenefitsResponse, benefit, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Finch) -> None:
        benefit = client.hris.benefits.retrieve(
            "string",
        )
        assert_matches_type(CompanyBenefit, benefit, path=["response"])

    @parametrize
    def test_method_update(self, client: Finch) -> None:
        benefit = client.hris.benefits.update(
            "string",
        )
        assert_matches_type(UpdateCompanyBenefitResponse, benefit, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Finch) -> None:
        benefit = client.hris.benefits.update(
            "string",
            description="string",
        )
        assert_matches_type(UpdateCompanyBenefitResponse, benefit, path=["response"])

    @parametrize
    def test_method_list(self, client: Finch) -> None:
        benefit = client.hris.benefits.list()
        assert_matches_type(SyncSinglePage[CompanyBenefit], benefit, path=["response"])

    @parametrize
    def test_method_list_supported_benefits(self, client: Finch) -> None:
        benefit = client.hris.benefits.list_supported_benefits()
        assert_matches_type(SyncSinglePage[SupportedBenefit], benefit, path=["response"])


class TestAsyncBenefits:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncFinch) -> None:
        benefit = await client.hris.benefits.create()
        assert_matches_type(CreateCompanyBenefitsResponse, benefit, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncFinch) -> None:
        benefit = await client.hris.benefits.create(
            type="401k",
            description="string",
            frequency="one_time",
        )
        assert_matches_type(CreateCompanyBenefitsResponse, benefit, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncFinch) -> None:
        benefit = await client.hris.benefits.retrieve(
            "string",
        )
        assert_matches_type(CompanyBenefit, benefit, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncFinch) -> None:
        benefit = await client.hris.benefits.update(
            "string",
        )
        assert_matches_type(UpdateCompanyBenefitResponse, benefit, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncFinch) -> None:
        benefit = await client.hris.benefits.update(
            "string",
            description="string",
        )
        assert_matches_type(UpdateCompanyBenefitResponse, benefit, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncFinch) -> None:
        benefit = await client.hris.benefits.list()
        assert_matches_type(AsyncSinglePage[CompanyBenefit], benefit, path=["response"])

    @parametrize
    async def test_method_list_supported_benefits(self, client: AsyncFinch) -> None:
        benefit = await client.hris.benefits.list_supported_benefits()
        assert_matches_type(AsyncSinglePage[SupportedBenefit], benefit, path=["response"])
