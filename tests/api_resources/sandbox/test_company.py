# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._client import Finch, AsyncFinch
from finch.types.sandbox import CompanyUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestCompany:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_update(self, client: Finch) -> None:
        company = client.sandbox.company.update(
            accounts=[{}, {}, {}],
            departments=[{}, {}, {}],
            ein="string",
            entity={},
            legal_name="string",
            locations=[{}, {}, {}],
            primary_email="string",
            primary_phone_number="string",
        )
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Finch) -> None:
        company = client.sandbox.company.update(
            accounts=[
                {
                    "routing_number": "string",
                    "account_name": "string",
                    "institution_name": "string",
                    "account_type": "checking",
                    "account_number": "string",
                },
                {
                    "routing_number": "string",
                    "account_name": "string",
                    "institution_name": "string",
                    "account_type": "checking",
                    "account_number": "string",
                },
                {
                    "routing_number": "string",
                    "account_name": "string",
                    "institution_name": "string",
                    "account_type": "checking",
                    "account_number": "string",
                },
            ],
            departments=[
                {
                    "name": "string",
                    "parent": {"name": "string"},
                },
                {
                    "name": "string",
                    "parent": {"name": "string"},
                },
                {
                    "name": "string",
                    "parent": {"name": "string"},
                },
            ],
            ein="string",
            entity={
                "type": "llc",
                "subtype": "s_corporation",
            },
            legal_name="string",
            locations=[
                {
                    "line1": "string",
                    "line2": "string",
                    "city": "string",
                    "state": "string",
                    "postal_code": "string",
                    "country": "string",
                    "name": "string",
                    "source_id": "string",
                },
                {
                    "line1": "string",
                    "line2": "string",
                    "city": "string",
                    "state": "string",
                    "postal_code": "string",
                    "country": "string",
                    "name": "string",
                    "source_id": "string",
                },
                {
                    "line1": "string",
                    "line2": "string",
                    "city": "string",
                    "state": "string",
                    "postal_code": "string",
                    "country": "string",
                    "name": "string",
                    "source_id": "string",
                },
            ],
            primary_email="string",
            primary_phone_number="string",
        )
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Finch) -> None:
        response = client.sandbox.company.with_raw_response.update(
            accounts=[{}, {}, {}],
            departments=[{}, {}, {}],
            ein="string",
            entity={},
            legal_name="string",
            locations=[{}, {}, {}],
            primary_email="string",
            primary_phone_number="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])


class TestAsyncCompany:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_update(self, client: AsyncFinch) -> None:
        company = await client.sandbox.company.update(
            accounts=[{}, {}, {}],
            departments=[{}, {}, {}],
            ein="string",
            entity={},
            legal_name="string",
            locations=[{}, {}, {}],
            primary_email="string",
            primary_phone_number="string",
        )
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncFinch) -> None:
        company = await client.sandbox.company.update(
            accounts=[
                {
                    "routing_number": "string",
                    "account_name": "string",
                    "institution_name": "string",
                    "account_type": "checking",
                    "account_number": "string",
                },
                {
                    "routing_number": "string",
                    "account_name": "string",
                    "institution_name": "string",
                    "account_type": "checking",
                    "account_number": "string",
                },
                {
                    "routing_number": "string",
                    "account_name": "string",
                    "institution_name": "string",
                    "account_type": "checking",
                    "account_number": "string",
                },
            ],
            departments=[
                {
                    "name": "string",
                    "parent": {"name": "string"},
                },
                {
                    "name": "string",
                    "parent": {"name": "string"},
                },
                {
                    "name": "string",
                    "parent": {"name": "string"},
                },
            ],
            ein="string",
            entity={
                "type": "llc",
                "subtype": "s_corporation",
            },
            legal_name="string",
            locations=[
                {
                    "line1": "string",
                    "line2": "string",
                    "city": "string",
                    "state": "string",
                    "postal_code": "string",
                    "country": "string",
                    "name": "string",
                    "source_id": "string",
                },
                {
                    "line1": "string",
                    "line2": "string",
                    "city": "string",
                    "state": "string",
                    "postal_code": "string",
                    "country": "string",
                    "name": "string",
                    "source_id": "string",
                },
                {
                    "line1": "string",
                    "line2": "string",
                    "city": "string",
                    "state": "string",
                    "postal_code": "string",
                    "country": "string",
                    "name": "string",
                    "source_id": "string",
                },
            ],
            primary_email="string",
            primary_phone_number="string",
        )
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncFinch) -> None:
        response = await client.sandbox.company.with_raw_response.update(
            accounts=[{}, {}, {}],
            departments=[{}, {}, {}],
            ein="string",
            entity={},
            legal_name="string",
            locations=[{}, {}, {}],
            primary_email="string",
            primary_phone_number="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])
