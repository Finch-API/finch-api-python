# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import date

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncSinglePage, AsyncSinglePage
from ...types.hris import Payment, payment_list_params
from ..._base_client import AsyncPaginator, make_request_options

__all__ = ["Payments", "AsyncPayments"]


class Payments(SyncAPIResource):
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
