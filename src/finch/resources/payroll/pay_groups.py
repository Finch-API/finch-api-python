# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.payroll import pay_group_list_params
from ...types.payroll.pay_group_list_response import PayGroupListResponse
from ...types.payroll.pay_group_retrieve_response import PayGroupRetrieveResponse

__all__ = ["PayGroups", "AsyncPayGroups"]


class PayGroups(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PayGroupsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return PayGroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayGroupsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return PayGroupsWithStreamingResponse(self)

    def retrieve(
        self,
        pay_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PayGroupRetrieveResponse:
        """
        Read information from a single pay group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pay_group_id:
            raise ValueError(f"Expected a non-empty value for `pay_group_id` but received {pay_group_id!r}")
        return self._get(
            f"/employer/pay-groups/{pay_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayGroupRetrieveResponse,
        )

    def list(
        self,
        *,
        individual_id: str | NotGiven = NOT_GIVEN,
        pay_frequencies: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[PayGroupListResponse]:
        """
        Read company pay groups and frequencies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/pay-groups",
            page=SyncSinglePage[PayGroupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "individual_id": individual_id,
                        "pay_frequencies": pay_frequencies,
                    },
                    pay_group_list_params.PayGroupListParams,
                ),
            ),
            model=PayGroupListResponse,
        )


class AsyncPayGroups(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPayGroupsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPayGroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayGroupsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AsyncPayGroupsWithStreamingResponse(self)

    async def retrieve(
        self,
        pay_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PayGroupRetrieveResponse:
        """
        Read information from a single pay group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pay_group_id:
            raise ValueError(f"Expected a non-empty value for `pay_group_id` but received {pay_group_id!r}")
        return await self._get(
            f"/employer/pay-groups/{pay_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayGroupRetrieveResponse,
        )

    def list(
        self,
        *,
        individual_id: str | NotGiven = NOT_GIVEN,
        pay_frequencies: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PayGroupListResponse, AsyncSinglePage[PayGroupListResponse]]:
        """
        Read company pay groups and frequencies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/pay-groups",
            page=AsyncSinglePage[PayGroupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "individual_id": individual_id,
                        "pay_frequencies": pay_frequencies,
                    },
                    pay_group_list_params.PayGroupListParams,
                ),
            ),
            model=PayGroupListResponse,
        )


class PayGroupsWithRawResponse:
    def __init__(self, pay_groups: PayGroups) -> None:
        self._pay_groups = pay_groups

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            pay_groups.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            pay_groups.list,
        )


class AsyncPayGroupsWithRawResponse:
    def __init__(self, pay_groups: AsyncPayGroups) -> None:
        self._pay_groups = pay_groups

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            pay_groups.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            pay_groups.list,
        )


class PayGroupsWithStreamingResponse:
    def __init__(self, pay_groups: PayGroups) -> None:
        self._pay_groups = pay_groups

        self.retrieve = to_streamed_response_wrapper(
            pay_groups.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            pay_groups.list,
        )


class AsyncPayGroupsWithStreamingResponse:
    def __init__(self, pay_groups: AsyncPayGroups) -> None:
        self._pay_groups = pay_groups

        self.retrieve = async_to_streamed_response_wrapper(
            pay_groups.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            pay_groups.list,
        )
