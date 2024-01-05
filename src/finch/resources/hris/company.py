# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...types.hris import Company
from ..._base_client import (
    make_request_options,
)

__all__ = ["CompanyResource", "AsyncCompanyResource"]


class CompanyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompanyResourceWithRawResponse:
        return CompanyResourceWithRawResponse(self)

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
    def with_raw_response(self) -> AsyncCompanyResourceWithRawResponse:
        return AsyncCompanyResourceWithRawResponse(self)

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
        self.retrieve = to_raw_response_wrapper(
            company.retrieve,
        )


class AsyncCompanyResourceWithRawResponse:
    def __init__(self, company: AsyncCompanyResource) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            company.retrieve,
        )
