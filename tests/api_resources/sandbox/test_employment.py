# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._client import Finch, AsyncFinch
from finch.types.sandbox import EmploymentUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestEmployment:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_update(self, client: Finch) -> None:
        employment = client.sandbox.employment.update(
            "string",
        )
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Finch) -> None:
        employment = client.sandbox.employment.update(
            "string",
            class_code="string",
            custom_fields=[
                {
                    "name": "string",
                    "value": {},
                },
                {
                    "name": "string",
                    "value": {},
                },
                {
                    "name": "string",
                    "value": {},
                },
            ],
            department={"name": "string"},
            employment={
                "type": "employee",
                "subtype": "full_time",
            },
            end_date="string",
            first_name="string",
            income={
                "unit": "yearly",
                "amount": 0,
                "currency": "string",
                "effective_date": "string",
            },
            income_history=[
                {
                    "unit": "yearly",
                    "amount": 0,
                    "currency": "string",
                    "effective_date": "string",
                },
                {
                    "unit": "yearly",
                    "amount": 0,
                    "currency": "string",
                    "effective_date": "string",
                },
                {
                    "unit": "yearly",
                    "amount": 0,
                    "currency": "string",
                    "effective_date": "string",
                },
            ],
            is_active=True,
            last_name="string",
            location={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
                "name": "string",
                "source_id": "string",
            },
            manager={"id": "string"},
            middle_name="string",
            source_id="string",
            start_date="string",
            title="string",
        )
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Finch) -> None:
        response = client.sandbox.employment.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = response.parse()
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])


class TestAsyncEmployment:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_update(self, client: AsyncFinch) -> None:
        employment = await client.sandbox.employment.update(
            "string",
        )
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncFinch) -> None:
        employment = await client.sandbox.employment.update(
            "string",
            class_code="string",
            custom_fields=[
                {
                    "name": "string",
                    "value": {},
                },
                {
                    "name": "string",
                    "value": {},
                },
                {
                    "name": "string",
                    "value": {},
                },
            ],
            department={"name": "string"},
            employment={
                "type": "employee",
                "subtype": "full_time",
            },
            end_date="string",
            first_name="string",
            income={
                "unit": "yearly",
                "amount": 0,
                "currency": "string",
                "effective_date": "string",
            },
            income_history=[
                {
                    "unit": "yearly",
                    "amount": 0,
                    "currency": "string",
                    "effective_date": "string",
                },
                {
                    "unit": "yearly",
                    "amount": 0,
                    "currency": "string",
                    "effective_date": "string",
                },
                {
                    "unit": "yearly",
                    "amount": 0,
                    "currency": "string",
                    "effective_date": "string",
                },
            ],
            is_active=True,
            last_name="string",
            location={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
                "name": "string",
                "source_id": "string",
            },
            manager={"id": "string"},
            middle_name="string",
            source_id="string",
            start_date="string",
            title="string",
        )
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncFinch) -> None:
        response = await client.sandbox.employment.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = response.parse()
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])
