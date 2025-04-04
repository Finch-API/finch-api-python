# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.sandbox import DirectoryCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDirectory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Finch) -> None:
        directory = client.sandbox.directory.create()
        assert_matches_type(DirectoryCreateResponse, directory, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Finch) -> None:
        directory = client.sandbox.directory.create(
            body=[
                {
                    "class_code": "class_code",
                    "custom_fields": [
                        {
                            "name": "name",
                            "value": {},
                        }
                    ],
                    "department": {"name": "name"},
                    "dob": "dob",
                    "emails": [
                        {
                            "data": "data",
                            "type": "work",
                        }
                    ],
                    "employment": {
                        "subtype": "full_time",
                        "type": "employee",
                    },
                    "employment_status": "active",
                    "encrypted_ssn": "encrypted_ssn",
                    "end_date": "end_date",
                    "ethnicity": "asian",
                    "first_name": "first_name",
                    "gender": "female",
                    "income": {
                        "amount": 0,
                        "currency": "currency",
                        "effective_date": "effective_date",
                        "unit": "yearly",
                    },
                    "income_history": [
                        {
                            "amount": 0,
                            "currency": "currency",
                            "effective_date": "effective_date",
                            "unit": "yearly",
                        }
                    ],
                    "is_active": True,
                    "last_name": "last_name",
                    "latest_rehire_date": "latest_rehire_date",
                    "location": {
                        "city": "city",
                        "country": "country",
                        "line1": "line1",
                        "line2": "line2",
                        "name": "name",
                        "postal_code": "postal_code",
                        "source_id": "source_id",
                        "state": "state",
                    },
                    "manager": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "middle_name": "middle_name",
                    "phone_numbers": [
                        {
                            "data": "data",
                            "type": "work",
                        }
                    ],
                    "preferred_name": "preferred_name",
                    "residence": {
                        "city": "city",
                        "country": "country",
                        "line1": "line1",
                        "line2": "line2",
                        "name": "name",
                        "postal_code": "postal_code",
                        "source_id": "source_id",
                        "state": "state",
                    },
                    "source_id": "source_id",
                    "ssn": "ssn",
                    "start_date": "start_date",
                    "title": "title",
                }
            ],
        )
        assert_matches_type(DirectoryCreateResponse, directory, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Finch) -> None:
        response = client.sandbox.directory.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert_matches_type(DirectoryCreateResponse, directory, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Finch) -> None:
        with client.sandbox.directory.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = response.parse()
            assert_matches_type(DirectoryCreateResponse, directory, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDirectory:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFinch) -> None:
        directory = await async_client.sandbox.directory.create()
        assert_matches_type(DirectoryCreateResponse, directory, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFinch) -> None:
        directory = await async_client.sandbox.directory.create(
            body=[
                {
                    "class_code": "class_code",
                    "custom_fields": [
                        {
                            "name": "name",
                            "value": {},
                        }
                    ],
                    "department": {"name": "name"},
                    "dob": "dob",
                    "emails": [
                        {
                            "data": "data",
                            "type": "work",
                        }
                    ],
                    "employment": {
                        "subtype": "full_time",
                        "type": "employee",
                    },
                    "employment_status": "active",
                    "encrypted_ssn": "encrypted_ssn",
                    "end_date": "end_date",
                    "ethnicity": "asian",
                    "first_name": "first_name",
                    "gender": "female",
                    "income": {
                        "amount": 0,
                        "currency": "currency",
                        "effective_date": "effective_date",
                        "unit": "yearly",
                    },
                    "income_history": [
                        {
                            "amount": 0,
                            "currency": "currency",
                            "effective_date": "effective_date",
                            "unit": "yearly",
                        }
                    ],
                    "is_active": True,
                    "last_name": "last_name",
                    "latest_rehire_date": "latest_rehire_date",
                    "location": {
                        "city": "city",
                        "country": "country",
                        "line1": "line1",
                        "line2": "line2",
                        "name": "name",
                        "postal_code": "postal_code",
                        "source_id": "source_id",
                        "state": "state",
                    },
                    "manager": {"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    "middle_name": "middle_name",
                    "phone_numbers": [
                        {
                            "data": "data",
                            "type": "work",
                        }
                    ],
                    "preferred_name": "preferred_name",
                    "residence": {
                        "city": "city",
                        "country": "country",
                        "line1": "line1",
                        "line2": "line2",
                        "name": "name",
                        "postal_code": "postal_code",
                        "source_id": "source_id",
                        "state": "state",
                    },
                    "source_id": "source_id",
                    "ssn": "ssn",
                    "start_date": "start_date",
                    "title": "title",
                }
            ],
        )
        assert_matches_type(DirectoryCreateResponse, directory, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFinch) -> None:
        response = await async_client.sandbox.directory.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert_matches_type(DirectoryCreateResponse, directory, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFinch) -> None:
        async with async_client.sandbox.directory.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = await response.parse()
            assert_matches_type(DirectoryCreateResponse, directory, path=["response"])

        assert cast(Any, response.is_closed) is True
