# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.sandbox import PaymentCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Finch) -> None:
        payment = client.sandbox.payment.create()
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Finch) -> None:
        payment = client.sandbox.payment.create(
            end_date="end_date",
            pay_statements=[
                {
                    "earnings": [
                        {
                            "amount": 0,
                            "currency": "currency",
                            "hours": 0,
                            "name": "name",
                            "type": "salary",
                        },
                        {
                            "amount": 0,
                            "currency": "currency",
                            "hours": 0,
                            "name": "name",
                            "type": "salary",
                        },
                        {
                            "amount": 0,
                            "currency": "currency",
                            "hours": 0,
                            "name": "name",
                            "type": "salary",
                        },
                    ],
                    "employee_deductions": [
                        {
                            "amount": 2000,
                            "currency": "usd",
                            "name": "401k test",
                            "pre_tax": True,
                            "type": "401k",
                        }
                    ],
                    "employer_contributions": [
                        {
                            "amount": 0,
                            "currency": "currency",
                            "name": "name",
                            "type": "401k",
                        },
                        {
                            "amount": 0,
                            "currency": "currency",
                            "name": "name",
                            "type": "401k",
                        },
                        {
                            "amount": 0,
                            "currency": "currency",
                            "name": "name",
                            "type": "401k",
                        },
                    ],
                    "gross_pay": {
                        "amount": 0,
                        "currency": "currency",
                    },
                    "individual_id": "b2338cfb-472f-4f72-9faa-e028c083144a",
                    "net_pay": {
                        "amount": 0,
                        "currency": "currency",
                    },
                    "payment_method": "check",
                    "taxes": [
                        {
                            "amount": 0,
                            "currency": "currency",
                            "employer": True,
                            "name": "name",
                            "type": "state",
                        },
                        {
                            "amount": 0,
                            "currency": "currency",
                            "employer": True,
                            "name": "name",
                            "type": "state",
                        },
                        {
                            "amount": 0,
                            "currency": "currency",
                            "employer": True,
                            "name": "name",
                            "type": "state",
                        },
                    ],
                    "total_hours": 0,
                    "type": "regular_payroll",
                }
            ],
            start_date="start_date",
        )
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Finch) -> None:
        response = client.sandbox.payment.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Finch) -> None:
        with client.sandbox.payment.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentCreateResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayment:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFinch) -> None:
        payment = await async_client.sandbox.payment.create()
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFinch) -> None:
        payment = await async_client.sandbox.payment.create(
            end_date="end_date",
            pay_statements=[
                {
                    "earnings": [
                        {
                            "amount": 0,
                            "currency": "currency",
                            "hours": 0,
                            "name": "name",
                            "type": "salary",
                        },
                        {
                            "amount": 0,
                            "currency": "currency",
                            "hours": 0,
                            "name": "name",
                            "type": "salary",
                        },
                        {
                            "amount": 0,
                            "currency": "currency",
                            "hours": 0,
                            "name": "name",
                            "type": "salary",
                        },
                    ],
                    "employee_deductions": [
                        {
                            "amount": 2000,
                            "currency": "usd",
                            "name": "401k test",
                            "pre_tax": True,
                            "type": "401k",
                        }
                    ],
                    "employer_contributions": [
                        {
                            "amount": 0,
                            "currency": "currency",
                            "name": "name",
                            "type": "401k",
                        },
                        {
                            "amount": 0,
                            "currency": "currency",
                            "name": "name",
                            "type": "401k",
                        },
                        {
                            "amount": 0,
                            "currency": "currency",
                            "name": "name",
                            "type": "401k",
                        },
                    ],
                    "gross_pay": {
                        "amount": 0,
                        "currency": "currency",
                    },
                    "individual_id": "b2338cfb-472f-4f72-9faa-e028c083144a",
                    "net_pay": {
                        "amount": 0,
                        "currency": "currency",
                    },
                    "payment_method": "check",
                    "taxes": [
                        {
                            "amount": 0,
                            "currency": "currency",
                            "employer": True,
                            "name": "name",
                            "type": "state",
                        },
                        {
                            "amount": 0,
                            "currency": "currency",
                            "employer": True,
                            "name": "name",
                            "type": "state",
                        },
                        {
                            "amount": 0,
                            "currency": "currency",
                            "employer": True,
                            "name": "name",
                            "type": "state",
                        },
                    ],
                    "total_hours": 0,
                    "type": "regular_payroll",
                }
            ],
            start_date="start_date",
        )
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFinch) -> None:
        response = await async_client.sandbox.payment.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFinch) -> None:
        async with async_client.sandbox.payment.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentCreateResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True
