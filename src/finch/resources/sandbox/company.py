# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ... import _legacy_response
from ...types import LocationParam
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.sandbox import CompanyUpdateResponse, company_update_params

__all__ = ["Company", "AsyncCompany"]


class Company(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompanyWithRawResponse:
        return CompanyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompanyWithStreamingResponse:
        return CompanyWithStreamingResponse(self)

    def update(
        self,
        *,
        accounts: Optional[Iterable[company_update_params.Account]],
        departments: Optional[Iterable[Optional[company_update_params.Department]]],
        ein: Optional[str],
        entity: Optional[company_update_params.Entity],
        legal_name: Optional[str],
        locations: Optional[Iterable[Optional[LocationParam]]],
        primary_email: Optional[str],
        primary_phone_number: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyUpdateResponse:
        """
        Update a sandbox company's data

        Args:
          accounts: An array of bank account objects associated with the payroll/HRIS system.

          departments: The array of company departments.

          ein: The employer identification number.

          entity: The entity type object.

          legal_name: The legal name of the company.

          primary_email: The email of the main administrator on the account.

          primary_phone_number: The phone number of the main administrator on the account. Format: `XXXXXXXXXX`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/sandbox/company",
            body=maybe_transform(
                {
                    "accounts": accounts,
                    "departments": departments,
                    "ein": ein,
                    "entity": entity,
                    "legal_name": legal_name,
                    "locations": locations,
                    "primary_email": primary_email,
                    "primary_phone_number": primary_phone_number,
                },
                company_update_params.CompanyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyUpdateResponse,
        )


class AsyncCompany(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompanyWithRawResponse:
        return AsyncCompanyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompanyWithStreamingResponse:
        return AsyncCompanyWithStreamingResponse(self)

    async def update(
        self,
        *,
        accounts: Optional[Iterable[company_update_params.Account]],
        departments: Optional[Iterable[Optional[company_update_params.Department]]],
        ein: Optional[str],
        entity: Optional[company_update_params.Entity],
        legal_name: Optional[str],
        locations: Optional[Iterable[Optional[LocationParam]]],
        primary_email: Optional[str],
        primary_phone_number: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyUpdateResponse:
        """
        Update a sandbox company's data

        Args:
          accounts: An array of bank account objects associated with the payroll/HRIS system.

          departments: The array of company departments.

          ein: The employer identification number.

          entity: The entity type object.

          legal_name: The legal name of the company.

          primary_email: The email of the main administrator on the account.

          primary_phone_number: The phone number of the main administrator on the account. Format: `XXXXXXXXXX`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/sandbox/company",
            body=await async_maybe_transform(
                {
                    "accounts": accounts,
                    "departments": departments,
                    "ein": ein,
                    "entity": entity,
                    "legal_name": legal_name,
                    "locations": locations,
                    "primary_email": primary_email,
                    "primary_phone_number": primary_phone_number,
                },
                company_update_params.CompanyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyUpdateResponse,
        )


class CompanyWithRawResponse:
    def __init__(self, company: Company) -> None:
        self._company = company

        self.update = _legacy_response.to_raw_response_wrapper(
            company.update,
        )


class AsyncCompanyWithRawResponse:
    def __init__(self, company: AsyncCompany) -> None:
        self._company = company

        self.update = _legacy_response.async_to_raw_response_wrapper(
            company.update,
        )


class CompanyWithStreamingResponse:
    def __init__(self, company: Company) -> None:
        self._company = company

        self.update = to_streamed_response_wrapper(
            company.update,
        )


class AsyncCompanyWithStreamingResponse:
    def __init__(self, company: AsyncCompany) -> None:
        self._company = company

        self.update = async_to_streamed_response_wrapper(
            company.update,
        )
