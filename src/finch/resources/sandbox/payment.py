# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.sandbox import PaymentCreateResponse, payment_create_params

__all__ = ["Payment", "AsyncPayment"]


class Payment(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentWithRawResponse:
        return PaymentWithRawResponse(self)

    def create(
        self,
        *,
        end_date: str | NotGiven = NOT_GIVEN,
        pay_statements: List[payment_create_params.PayStatement] | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreateResponse:
        """
        Add a new sandbox payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sandbox/payment",
            body=maybe_transform(
                {
                    "end_date": end_date,
                    "pay_statements": pay_statements,
                    "start_date": start_date,
                },
                payment_create_params.PaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentCreateResponse,
        )


class AsyncPayment(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentWithRawResponse:
        return AsyncPaymentWithRawResponse(self)

    async def create(
        self,
        *,
        end_date: str | NotGiven = NOT_GIVEN,
        pay_statements: List[payment_create_params.PayStatement] | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreateResponse:
        """
        Add a new sandbox payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sandbox/payment",
            body=maybe_transform(
                {
                    "end_date": end_date,
                    "pay_statements": pay_statements,
                    "start_date": start_date,
                },
                payment_create_params.PaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentCreateResponse,
        )


class PaymentWithRawResponse:
    def __init__(self, payment: Payment) -> None:
        self.create = to_raw_response_wrapper(
            payment.create,
        )


class AsyncPaymentWithRawResponse:
    def __init__(self, payment: AsyncPayment) -> None:
        self.create = async_to_raw_response_wrapper(
            payment.create,
        )
