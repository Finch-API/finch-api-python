# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._client import Finch, AsyncFinch
from finch.types.sandbox import PaymentCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestPayment:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Finch) -> None:
        payment = client.sandbox.payment.create()
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Finch) -> None:
        payment = client.sandbox.payment.create(
            end_date="string",
            pay_statements=[
                {
                    "individual_id": "b2338cfb-472f-4f72-9faa-e028c083144a",
                    "type": "regular_payroll",
                    "payment_method": "check",
                    "total_hours": 0,
                    "gross_pay": {
                        "amount": 0,
                        "currency": "string",
                    },
                    "net_pay": {
                        "amount": 0,
                        "currency": "string",
                    },
                    "earnings": [
                        {
                            "type": "salary",
                            "name": "string",
                            "amount": 0,
                            "currency": "string",
                            "hours": 0,
                        },
                        {
                            "type": "salary",
                            "name": "string",
                            "amount": 0,
                            "currency": "string",
                            "hours": 0,
                        },
                        {
                            "type": "salary",
                            "name": "string",
                            "amount": 0,
                            "currency": "string",
                            "hours": 0,
                        },
                    ],
                    "taxes": [
                        {
                            "type": "state",
                            "name": "string",
                            "employer": True,
                            "amount": 0,
                            "currency": "string",
                        },
                        {
                            "type": "state",
                            "name": "string",
                            "employer": True,
                            "amount": 0,
                            "currency": "string",
                        },
                        {
                            "type": "state",
                            "name": "string",
                            "employer": True,
                            "amount": 0,
                            "currency": "string",
                        },
                    ],
                    "employee_deductions": [
                        {
                            "name": "401k test",
                            "amount": 2000,
                            "currency": "usd",
                            "pre_tax": True,
                            "type": "401k",
                        }
                    ],
                    "employer_contributions": [
                        {
                            "name": "string",
                            "amount": 0,
                            "currency": "string",
                            "type": "401k",
                        },
                        {
                            "name": "string",
                            "amount": 0,
                            "currency": "string",
                            "type": "401k",
                        },
                        {
                            "name": "string",
                            "amount": 0,
                            "currency": "string",
                            "type": "401k",
                        },
                    ],
                }
            ],
            start_date="string",
        )
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Finch) -> None:
        response = client.sandbox.payment.with_raw_response.create()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])


class TestAsyncPayment:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncFinch) -> None:
        payment = await client.sandbox.payment.create()
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncFinch) -> None:
        payment = await client.sandbox.payment.create(
            end_date="string",
            pay_statements=[
                {
                    "individual_id": "b2338cfb-472f-4f72-9faa-e028c083144a",
                    "type": "regular_payroll",
                    "payment_method": "check",
                    "total_hours": 0,
                    "gross_pay": {
                        "amount": 0,
                        "currency": "string",
                    },
                    "net_pay": {
                        "amount": 0,
                        "currency": "string",
                    },
                    "earnings": [
                        {
                            "type": "salary",
                            "name": "string",
                            "amount": 0,
                            "currency": "string",
                            "hours": 0,
                        },
                        {
                            "type": "salary",
                            "name": "string",
                            "amount": 0,
                            "currency": "string",
                            "hours": 0,
                        },
                        {
                            "type": "salary",
                            "name": "string",
                            "amount": 0,
                            "currency": "string",
                            "hours": 0,
                        },
                    ],
                    "taxes": [
                        {
                            "type": "state",
                            "name": "string",
                            "employer": True,
                            "amount": 0,
                            "currency": "string",
                        },
                        {
                            "type": "state",
                            "name": "string",
                            "employer": True,
                            "amount": 0,
                            "currency": "string",
                        },
                        {
                            "type": "state",
                            "name": "string",
                            "employer": True,
                            "amount": 0,
                            "currency": "string",
                        },
                    ],
                    "employee_deductions": [
                        {
                            "name": "401k test",
                            "amount": 2000,
                            "currency": "usd",
                            "pre_tax": True,
                            "type": "401k",
                        }
                    ],
                    "employer_contributions": [
                        {
                            "name": "string",
                            "amount": 0,
                            "currency": "string",
                            "type": "401k",
                        },
                        {
                            "name": "string",
                            "amount": 0,
                            "currency": "string",
                            "type": "401k",
                        },
                        {
                            "name": "string",
                            "amount": 0,
                            "currency": "string",
                            "type": "401k",
                        },
                    ],
                }
            ],
            start_date="string",
        )
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncFinch) -> None:
        response = await client.sandbox.payment.with_raw_response.create()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])
