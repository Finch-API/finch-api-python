# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._utils import parse_date
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
            end_date=parse_date("2019-12-27"),
            pay_statements=[
                {
                    "individual_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "earnings": [
                        {
                            "amount": 0,
                            "hours": 0,
                            "name": "x",
                            "type": "bonus",
                        }
                    ],
                    "employee_deductions": [
                        {
                            "amount": 0,
                            "name": "x",
                            "pre_tax": True,
                            "type": "457",
                        }
                    ],
                    "employer_contributions": [
                        {
                            "amount": 0,
                            "name": "x",
                            "type": "457",
                        }
                    ],
                    "gross_pay": 1,
                    "net_pay": 9007199254740991,
                    "payment_method": "check",
                    "taxes": [
                        {
                            "amount": 0,
                            "employer": True,
                            "name": "x",
                            "type": "federal",
                        }
                    ],
                    "total_hours": 1,
                    "type": "off_cycle_payroll",
                }
            ],
            start_date=parse_date("2019-12-27"),
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
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncFinch) -> None:
        payment = await async_client.sandbox.payment.create()
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFinch) -> None:
        payment = await async_client.sandbox.payment.create(
            end_date=parse_date("2019-12-27"),
            pay_statements=[
                {
                    "individual_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "earnings": [
                        {
                            "amount": 0,
                            "hours": 0,
                            "name": "x",
                            "type": "bonus",
                        }
                    ],
                    "employee_deductions": [
                        {
                            "amount": 0,
                            "name": "x",
                            "pre_tax": True,
                            "type": "457",
                        }
                    ],
                    "employer_contributions": [
                        {
                            "amount": 0,
                            "name": "x",
                            "type": "457",
                        }
                    ],
                    "gross_pay": 1,
                    "net_pay": 9007199254740991,
                    "payment_method": "check",
                    "taxes": [
                        {
                            "amount": 0,
                            "employer": True,
                            "name": "x",
                            "type": "federal",
                        }
                    ],
                    "total_hours": 1,
                    "type": "off_cycle_payroll",
                }
            ],
            start_date=parse_date("2019-12-27"),
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
