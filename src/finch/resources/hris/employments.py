# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncResponsesPage, AsyncResponsesPage
from ...types.hris import EmploymentDataResponse, employment_retrieve_many_params
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["Employments", "AsyncEmployments"]


class Employments(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmploymentsWithRawResponse:
        return EmploymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmploymentsWithStreamingResponse:
        return EmploymentsWithStreamingResponse(self)

    def retrieve_many(
        self,
        *,
        requests: Iterable[employment_retrieve_many_params.Request],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncResponsesPage[EmploymentDataResponse]:
        """
        Read individual employment and income data

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
            body=maybe_transform({"requests": requests}, employment_retrieve_many_params.EmploymentRetrieveManyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=EmploymentDataResponse,
            method="post",
        )


class AsyncEmployments(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmploymentsWithRawResponse:
        return AsyncEmploymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmploymentsWithStreamingResponse:
        return AsyncEmploymentsWithStreamingResponse(self)

    def retrieve_many(
        self,
        *,
        requests: Iterable[employment_retrieve_many_params.Request],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EmploymentDataResponse, AsyncResponsesPage[EmploymentDataResponse]]:
        """
        Read individual employment and income data

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
            body=maybe_transform({"requests": requests}, employment_retrieve_many_params.EmploymentRetrieveManyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=EmploymentDataResponse,
            method="post",
        )


class EmploymentsWithRawResponse:
    def __init__(self, employments: Employments) -> None:
        self._employments = employments

        self.retrieve_many = _legacy_response.to_raw_response_wrapper(
            employments.retrieve_many,
        )


class AsyncEmploymentsWithRawResponse:
    def __init__(self, employments: AsyncEmployments) -> None:
        self._employments = employments

        self.retrieve_many = _legacy_response.async_to_raw_response_wrapper(
            employments.retrieve_many,
        )


class EmploymentsWithStreamingResponse:
    def __init__(self, employments: Employments) -> None:
        self._employments = employments

        self.retrieve_many = to_streamed_response_wrapper(
            employments.retrieve_many,
        )


class AsyncEmploymentsWithStreamingResponse:
    def __init__(self, employments: AsyncEmployments) -> None:
        self._employments = employments

        self.retrieve_many = async_to_streamed_response_wrapper(
            employments.retrieve_many,
        )
