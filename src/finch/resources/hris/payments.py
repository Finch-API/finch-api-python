# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ...types.hris import payment_list_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.hris.payment import Payment

__all__ = ["Payments", "AsyncPayments"]


class Payments(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return PaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return PaymentsWithStreamingResponse(self)

    def list(
        self,
        *,
        end_date: Union[str, date],
        start_date: Union[str, date],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Payment]:
        """
        Read payroll and contractor related payments by the company.

        Args:
          end_date: The end date to retrieve payments by a company (inclusive) in `YYYY-MM-DD`
              format.

          start_date: The start date to retrieve payments by a company (inclusive) in `YYYY-MM-DD`
              format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/payment",
            page=SyncSinglePage[Payment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            model=Payment,
        )


class AsyncPayments(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AsyncPaymentsWithStreamingResponse(self)

    def list(
        self,
        *,
        end_date: Union[str, date],
        start_date: Union[str, date],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Payment, AsyncSinglePage[Payment]]:
        """
        Read payroll and contractor related payments by the company.

        Args:
          end_date: The end date to retrieve payments by a company (inclusive) in `YYYY-MM-DD`
              format.

          start_date: The start date to retrieve payments by a company (inclusive) in `YYYY-MM-DD`
              format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/payment",
            page=AsyncSinglePage[Payment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            model=Payment,
        )


class PaymentsWithRawResponse:
    def __init__(self, payments: Payments) -> None:
        self._payments = payments

        self.list = _legacy_response.to_raw_response_wrapper(
            payments.list,
        )


class AsyncPaymentsWithRawResponse:
    def __init__(self, payments: AsyncPayments) -> None:
        self._payments = payments

        self.list = _legacy_response.async_to_raw_response_wrapper(
            payments.list,
        )


class PaymentsWithStreamingResponse:
    def __init__(self, payments: Payments) -> None:
        self._payments = payments

        self.list = to_streamed_response_wrapper(
            payments.list,
        )


class AsyncPaymentsWithStreamingResponse:
    def __init__(self, payments: AsyncPayments) -> None:
        self._payments = payments

        self.list = async_to_streamed_response_wrapper(
            payments.list,
        )
