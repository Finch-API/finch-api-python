# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....pagination import SyncResponsesPage, AsyncResponsesPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.hris.individuals import (
    EmploymentDataResponse,
    employment_data_retrieve_many_params,
)

__all__ = ["EmploymentData", "AsyncEmploymentData"]


class EmploymentData(SyncAPIResource):
    def retrieve_many(
        self,
        *,
        requests: List[employment_data_retrieve_many_params.Request],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncResponsesPage[EmploymentDataResponse]:
        """
        Read individual employment and income data

        Note: Income information is returned as reported by the provider. This may not
        always be annualized income, but may be in units of bi-weekly, semi-monthly,
        daily, etc, depending on what information the provider returns.

        Args:
          requests: The array of batch requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/employment",
            page=SyncResponsesPage[EmploymentDataResponse],
            body=maybe_transform(
                {"requests": requests}, employment_data_retrieve_many_params.EmploymentDataRetrieveManyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=EmploymentDataResponse,
            method="post",
        )


class AsyncEmploymentData(AsyncAPIResource):
    def retrieve_many(
        self,
        *,
        requests: List[employment_data_retrieve_many_params.Request],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EmploymentDataResponse, AsyncResponsesPage[EmploymentDataResponse]]:
        """
        Read individual employment and income data

        Note: Income information is returned as reported by the provider. This may not
        always be annualized income, but may be in units of bi-weekly, semi-monthly,
        daily, etc, depending on what information the provider returns.

        Args:
          requests: The array of batch requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/employment",
            page=AsyncResponsesPage[EmploymentDataResponse],
            body=maybe_transform(
                {"requests": requests}, employment_data_retrieve_many_params.EmploymentDataRetrieveManyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=EmploymentDataResponse,
            method="post",
        )
