# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.sandbox import payment_create_params
from ...types.sandbox.payment_create_response import PaymentCreateResponse

__all__ = ["Payment", "AsyncPayment"]


class Payment(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return PaymentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return PaymentWithStreamingResponse(self)

    def create(
        self,
        *,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        pay_statements: Iterable[payment_create_params.PayStatement] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
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
          pay_statements: Array of pay statements to include in the payment.

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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AsyncPaymentWithStreamingResponse(self)

    async def create(
        self,
        *,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        pay_statements: Iterable[payment_create_params.PayStatement] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
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
          pay_statements: Array of pay statements to include in the payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sandbox/payment",
            body=await async_maybe_transform(
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
        self._payment = payment

        self.create = _legacy_response.to_raw_response_wrapper(
            payment.create,
        )


class AsyncPaymentWithRawResponse:
    def __init__(self, payment: AsyncPayment) -> None:
        self._payment = payment

        self.create = _legacy_response.async_to_raw_response_wrapper(
            payment.create,
        )


class PaymentWithStreamingResponse:
    def __init__(self, payment: Payment) -> None:
        self._payment = payment

        self.create = to_streamed_response_wrapper(
            payment.create,
        )


class AsyncPaymentWithStreamingResponse:
    def __init__(self, payment: AsyncPayment) -> None:
        self._payment = payment

        self.create = async_to_streamed_response_wrapper(
            payment.create,
        )
