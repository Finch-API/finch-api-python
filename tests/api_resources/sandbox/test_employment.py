# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.sandbox import EmploymentUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmployment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
            start_date="3/4/2020",
            title="string",
        )
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Finch) -> None:
        response = client.sandbox.employment.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = response.parse()
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Finch) -> None:
        with client.sandbox.employment.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employment = response.parse()
            assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Finch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `individual_id` but received ''"):
            client.sandbox.employment.with_raw_response.update(
                "",
            )


class TestAsyncEmployment:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncFinch) -> None:
        employment = await async_client.sandbox.employment.update(
            "string",
        )
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFinch) -> None:
        employment = await async_client.sandbox.employment.update(
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
            start_date="3/4/2020",
            title="string",
        )
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFinch) -> None:
        response = await async_client.sandbox.employment.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employment = response.parse()
        assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFinch) -> None:
        async with async_client.sandbox.employment.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employment = await response.parse()
            assert_matches_type(EmploymentUpdateResponse, employment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncFinch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `individual_id` but received ''"):
            await async_client.sandbox.employment.with_raw_response.update(
                "",
            )
