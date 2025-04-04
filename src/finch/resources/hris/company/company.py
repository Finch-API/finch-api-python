# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .... import _legacy_response
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...._base_client import make_request_options
from ....types.hris.company.company import Company
from .pay_statement_item.pay_statement_item import (
    PayStatementItem,
    AsyncPayStatementItem,
    PayStatementItemWithRawResponse,
    AsyncPayStatementItemWithRawResponse,
    PayStatementItemWithStreamingResponse,
    AsyncPayStatementItemWithStreamingResponse,
)

__all__ = ["CompanyResource", "AsyncCompanyResource"]


class CompanyResource(SyncAPIResource):
    @cached_property
    def pay_statement_item(self) -> PayStatementItem:
        return PayStatementItem(self._client)

    @cached_property
    def with_raw_response(self) -> CompanyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return CompanyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompanyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return CompanyResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Company:
        """Read basic company data"""
        return self._get(
            "/employer/company",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )


class AsyncCompanyResource(AsyncAPIResource):
    @cached_property
    def pay_statement_item(self) -> AsyncPayStatementItem:
        return AsyncPayStatementItem(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCompanyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompanyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompanyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AsyncCompanyResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Company:
        """Read basic company data"""
        return await self._get(
            "/employer/company",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Company,
        )


class CompanyResourceWithRawResponse:
    def __init__(self, company: CompanyResource) -> None:
        self._company = company

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            company.retrieve,
        )

    @cached_property
    def pay_statement_item(self) -> PayStatementItemWithRawResponse:
        return PayStatementItemWithRawResponse(self._company.pay_statement_item)


class AsyncCompanyResourceWithRawResponse:
    def __init__(self, company: AsyncCompanyResource) -> None:
        self._company = company

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            company.retrieve,
        )

    @cached_property
    def pay_statement_item(self) -> AsyncPayStatementItemWithRawResponse:
        return AsyncPayStatementItemWithRawResponse(self._company.pay_statement_item)


class CompanyResourceWithStreamingResponse:
    def __init__(self, company: CompanyResource) -> None:
        self._company = company

        self.retrieve = to_streamed_response_wrapper(
            company.retrieve,
        )

    @cached_property
    def pay_statement_item(self) -> PayStatementItemWithStreamingResponse:
        return PayStatementItemWithStreamingResponse(self._company.pay_statement_item)


class AsyncCompanyResourceWithStreamingResponse:
    def __init__(self, company: AsyncCompanyResource) -> None:
        self._company = company

        self.retrieve = async_to_streamed_response_wrapper(
            company.retrieve,
        )

    @cached_property
    def pay_statement_item(self) -> AsyncPayStatementItemWithStreamingResponse:
        return AsyncPayStatementItemWithStreamingResponse(self._company.pay_statement_item)
