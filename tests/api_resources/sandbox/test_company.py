# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.sandbox import CompanyUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompany:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Finch) -> None:
        company = client.sandbox.company.update(
            accounts=[{}, {}, {}],
            departments=[{}, {}, {}],
            ein="ein",
            entity={},
            legal_name="legal_name",
            locations=[{}, {}, {}],
            primary_email="primary_email",
            primary_phone_number="primary_phone_number",
        )
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Finch) -> None:
        company = client.sandbox.company.update(
            accounts=[
                {
                    "routing_number": "routing_number",
                    "account_name": "account_name",
                    "institution_name": "institution_name",
                    "account_type": "checking",
                    "account_number": "account_number",
                },
                {
                    "routing_number": "routing_number",
                    "account_name": "account_name",
                    "institution_name": "institution_name",
                    "account_type": "checking",
                    "account_number": "account_number",
                },
                {
                    "routing_number": "routing_number",
                    "account_name": "account_name",
                    "institution_name": "institution_name",
                    "account_type": "checking",
                    "account_number": "account_number",
                },
            ],
            departments=[
                {
                    "name": "name",
                    "parent": {"name": "name"},
                },
                {
                    "name": "name",
                    "parent": {"name": "name"},
                },
                {
                    "name": "name",
                    "parent": {"name": "name"},
                },
            ],
            ein="ein",
            entity={
                "type": "llc",
                "subtype": "s_corporation",
            },
            legal_name="legal_name",
            locations=[
                {
                    "line1": "line1",
                    "line2": "line2",
                    "city": "city",
                    "state": "state",
                    "postal_code": "postal_code",
                    "country": "country",
                    "name": "name",
                    "source_id": "source_id",
                },
                {
                    "line1": "line1",
                    "line2": "line2",
                    "city": "city",
                    "state": "state",
                    "postal_code": "postal_code",
                    "country": "country",
                    "name": "name",
                    "source_id": "source_id",
                },
                {
                    "line1": "line1",
                    "line2": "line2",
                    "city": "city",
                    "state": "state",
                    "postal_code": "postal_code",
                    "country": "country",
                    "name": "name",
                    "source_id": "source_id",
                },
            ],
            primary_email="primary_email",
            primary_phone_number="primary_phone_number",
        )
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Finch) -> None:
        response = client.sandbox.company.with_raw_response.update(
            accounts=[{}, {}, {}],
            departments=[{}, {}, {}],
            ein="ein",
            entity={},
            legal_name="legal_name",
            locations=[{}, {}, {}],
            primary_email="primary_email",
            primary_phone_number="primary_phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Finch) -> None:
        with client.sandbox.company.with_streaming_response.update(
            accounts=[{}, {}, {}],
            departments=[{}, {}, {}],
            ein="ein",
            entity={},
            legal_name="legal_name",
            locations=[{}, {}, {}],
            primary_email="primary_email",
            primary_phone_number="primary_phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(CompanyUpdateResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompany:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncFinch) -> None:
        company = await async_client.sandbox.company.update(
            accounts=[{}, {}, {}],
            departments=[{}, {}, {}],
            ein="ein",
            entity={},
            legal_name="legal_name",
            locations=[{}, {}, {}],
            primary_email="primary_email",
            primary_phone_number="primary_phone_number",
        )
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFinch) -> None:
        company = await async_client.sandbox.company.update(
            accounts=[
                {
                    "routing_number": "routing_number",
                    "account_name": "account_name",
                    "institution_name": "institution_name",
                    "account_type": "checking",
                    "account_number": "account_number",
                },
                {
                    "routing_number": "routing_number",
                    "account_name": "account_name",
                    "institution_name": "institution_name",
                    "account_type": "checking",
                    "account_number": "account_number",
                },
                {
                    "routing_number": "routing_number",
                    "account_name": "account_name",
                    "institution_name": "institution_name",
                    "account_type": "checking",
                    "account_number": "account_number",
                },
            ],
            departments=[
                {
                    "name": "name",
                    "parent": {"name": "name"},
                },
                {
                    "name": "name",
                    "parent": {"name": "name"},
                },
                {
                    "name": "name",
                    "parent": {"name": "name"},
                },
            ],
            ein="ein",
            entity={
                "type": "llc",
                "subtype": "s_corporation",
            },
            legal_name="legal_name",
            locations=[
                {
                    "line1": "line1",
                    "line2": "line2",
                    "city": "city",
                    "state": "state",
                    "postal_code": "postal_code",
                    "country": "country",
                    "name": "name",
                    "source_id": "source_id",
                },
                {
                    "line1": "line1",
                    "line2": "line2",
                    "city": "city",
                    "state": "state",
                    "postal_code": "postal_code",
                    "country": "country",
                    "name": "name",
                    "source_id": "source_id",
                },
                {
                    "line1": "line1",
                    "line2": "line2",
                    "city": "city",
                    "state": "state",
                    "postal_code": "postal_code",
                    "country": "country",
                    "name": "name",
                    "source_id": "source_id",
                },
            ],
            primary_email="primary_email",
            primary_phone_number="primary_phone_number",
        )
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFinch) -> None:
        response = await async_client.sandbox.company.with_raw_response.update(
            accounts=[{}, {}, {}],
            departments=[{}, {}, {}],
            ein="ein",
            entity={},
            legal_name="legal_name",
            locations=[{}, {}, {}],
            primary_email="primary_email",
            primary_phone_number="primary_phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(CompanyUpdateResponse, company, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFinch) -> None:
        async with async_client.sandbox.company.with_streaming_response.update(
            accounts=[{}, {}, {}],
            departments=[{}, {}, {}],
            ein="ein",
            entity={},
            legal_name="legal_name",
            locations=[{}, {}, {}],
            primary_email="primary_email",
            primary_phone_number="primary_phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(CompanyUpdateResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True
