# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.sandbox import IndividualUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndividual:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Finch) -> None:
        individual = client.sandbox.individual.update(
            "string",
        )
        assert_matches_type(IndividualUpdateResponse, individual, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Finch) -> None:
        individual = client.sandbox.individual.update(
            "string",
            dob="12/20/1989",
            emails=[
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
            ],
            encrypted_ssn="string",
            ethnicity="asian",
            first_name="string",
            gender="female",
            last_name="string",
            middle_name="string",
            phone_numbers=[
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
            ],
            preferred_name="string",
            residence={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
                "name": "string",
                "source_id": "string",
            },
            ssn="string",
        )
        assert_matches_type(IndividualUpdateResponse, individual, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Finch) -> None:
        response = client.sandbox.individual.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        individual = response.parse()
        assert_matches_type(IndividualUpdateResponse, individual, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Finch) -> None:
        with client.sandbox.individual.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            individual = response.parse()
            assert_matches_type(IndividualUpdateResponse, individual, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Finch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `individual_id` but received ''"):
            client.sandbox.individual.with_raw_response.update(
                "",
            )


class TestAsyncIndividual:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncFinch) -> None:
        individual = await async_client.sandbox.individual.update(
            "string",
        )
        assert_matches_type(IndividualUpdateResponse, individual, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFinch) -> None:
        individual = await async_client.sandbox.individual.update(
            "string",
            dob="12/20/1989",
            emails=[
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
            ],
            encrypted_ssn="string",
            ethnicity="asian",
            first_name="string",
            gender="female",
            last_name="string",
            middle_name="string",
            phone_numbers=[
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
                {
                    "data": "string",
                    "type": "work",
                },
            ],
            preferred_name="string",
            residence={
                "line1": "string",
                "line2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
                "name": "string",
                "source_id": "string",
            },
            ssn="string",
        )
        assert_matches_type(IndividualUpdateResponse, individual, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFinch) -> None:
        response = await async_client.sandbox.individual.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        individual = response.parse()
        assert_matches_type(IndividualUpdateResponse, individual, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFinch) -> None:
        async with async_client.sandbox.individual.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            individual = await response.parse()
            assert_matches_type(IndividualUpdateResponse, individual, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncFinch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `individual_id` but received ''"):
            await async_client.sandbox.individual.with_raw_response.update(
                "",
            )
