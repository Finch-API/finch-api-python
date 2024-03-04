# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ... import _legacy_response
from ...types import IncomeParam, LocationParam
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
from ...types.sandbox import EmploymentUpdateResponse, employment_update_params

__all__ = ["Employment", "AsyncEmployment"]


class Employment(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmploymentWithRawResponse:
        return EmploymentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmploymentWithStreamingResponse:
        return EmploymentWithStreamingResponse(self)

    def update(
        self,
        individual_id: str,
        *,
        class_code: Optional[str] | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[employment_update_params.CustomField] | NotGiven = NOT_GIVEN,
        department: Optional[employment_update_params.Department] | NotGiven = NOT_GIVEN,
        employment: Optional[employment_update_params.Employment] | NotGiven = NOT_GIVEN,
        end_date: Optional[str] | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        income: Optional[IncomeParam] | NotGiven = NOT_GIVEN,
        income_history: Optional[Iterable[Optional[IncomeParam]]] | NotGiven = NOT_GIVEN,
        is_active: Optional[bool] | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        location: Optional[LocationParam] | NotGiven = NOT_GIVEN,
        manager: Optional[employment_update_params.Manager] | NotGiven = NOT_GIVEN,
        middle_name: Optional[str] | NotGiven = NOT_GIVEN,
        source_id: str | NotGiven = NOT_GIVEN,
        start_date: Optional[str] | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmploymentUpdateResponse:
        """
        Update sandbox employment

        Args:
          class_code: Worker's compensation classification code for this employee

          custom_fields: Custom fields for the individual. These are fields which are defined by the
              employer in the system. Custom fields are not currently supported for assisted
              connections.

          department: The department object.

          employment: The employment object.

          first_name: The legal first name of the individual.

          income: The employee's income as reported by the provider. This may not always be
              annualized income, but may be in units of bi-weekly, semi-monthly, daily, etc,
              depending on what information the provider returns.

          income_history: The array of income history.

          is_active: `true` if the individual an an active employee or contractor at the company.

          last_name: The legal last name of the individual.

          location

          manager: The manager object representing the manager of the individual within the org.

          middle_name: The legal middle name of the individual.

          source_id: The source system's unique employment identifier for this individual

          title: The current title of the individual.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not individual_id:
            raise ValueError(f"Expected a non-empty value for `individual_id` but received {individual_id!r}")
        return self._put(
            f"/sandbox/employment/{individual_id}",
            body=maybe_transform(
                {
                    "class_code": class_code,
                    "custom_fields": custom_fields,
                    "department": department,
                    "employment": employment,
                    "end_date": end_date,
                    "first_name": first_name,
                    "income": income,
                    "income_history": income_history,
                    "is_active": is_active,
                    "last_name": last_name,
                    "location": location,
                    "manager": manager,
                    "middle_name": middle_name,
                    "source_id": source_id,
                    "start_date": start_date,
                    "title": title,
                },
                employment_update_params.EmploymentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmploymentUpdateResponse,
        )


class AsyncEmployment(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmploymentWithRawResponse:
        return AsyncEmploymentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmploymentWithStreamingResponse:
        return AsyncEmploymentWithStreamingResponse(self)

    async def update(
        self,
        individual_id: str,
        *,
        class_code: Optional[str] | NotGiven = NOT_GIVEN,
        custom_fields: Iterable[employment_update_params.CustomField] | NotGiven = NOT_GIVEN,
        department: Optional[employment_update_params.Department] | NotGiven = NOT_GIVEN,
        employment: Optional[employment_update_params.Employment] | NotGiven = NOT_GIVEN,
        end_date: Optional[str] | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        income: Optional[IncomeParam] | NotGiven = NOT_GIVEN,
        income_history: Optional[Iterable[Optional[IncomeParam]]] | NotGiven = NOT_GIVEN,
        is_active: Optional[bool] | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        location: Optional[LocationParam] | NotGiven = NOT_GIVEN,
        manager: Optional[employment_update_params.Manager] | NotGiven = NOT_GIVEN,
        middle_name: Optional[str] | NotGiven = NOT_GIVEN,
        source_id: str | NotGiven = NOT_GIVEN,
        start_date: Optional[str] | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmploymentUpdateResponse:
        """
        Update sandbox employment

        Args:
          class_code: Worker's compensation classification code for this employee

          custom_fields: Custom fields for the individual. These are fields which are defined by the
              employer in the system. Custom fields are not currently supported for assisted
              connections.

          department: The department object.

          employment: The employment object.

          first_name: The legal first name of the individual.

          income: The employee's income as reported by the provider. This may not always be
              annualized income, but may be in units of bi-weekly, semi-monthly, daily, etc,
              depending on what information the provider returns.

          income_history: The array of income history.

          is_active: `true` if the individual an an active employee or contractor at the company.

          last_name: The legal last name of the individual.

          location

          manager: The manager object representing the manager of the individual within the org.

          middle_name: The legal middle name of the individual.

          source_id: The source system's unique employment identifier for this individual

          title: The current title of the individual.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not individual_id:
            raise ValueError(f"Expected a non-empty value for `individual_id` but received {individual_id!r}")
        return await self._put(
            f"/sandbox/employment/{individual_id}",
            body=await async_maybe_transform(
                {
                    "class_code": class_code,
                    "custom_fields": custom_fields,
                    "department": department,
                    "employment": employment,
                    "end_date": end_date,
                    "first_name": first_name,
                    "income": income,
                    "income_history": income_history,
                    "is_active": is_active,
                    "last_name": last_name,
                    "location": location,
                    "manager": manager,
                    "middle_name": middle_name,
                    "source_id": source_id,
                    "start_date": start_date,
                    "title": title,
                },
                employment_update_params.EmploymentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmploymentUpdateResponse,
        )


class EmploymentWithRawResponse:
    def __init__(self, employment: Employment) -> None:
        self._employment = employment

        self.update = _legacy_response.to_raw_response_wrapper(
            employment.update,
        )


class AsyncEmploymentWithRawResponse:
    def __init__(self, employment: AsyncEmployment) -> None:
        self._employment = employment

        self.update = _legacy_response.async_to_raw_response_wrapper(
            employment.update,
        )


class EmploymentWithStreamingResponse:
    def __init__(self, employment: Employment) -> None:
        self._employment = employment

        self.update = to_streamed_response_wrapper(
            employment.update,
        )


class AsyncEmploymentWithStreamingResponse:
    def __init__(self, employment: AsyncEmployment) -> None:
        self._employment = employment

        self.update = async_to_streamed_response_wrapper(
            employment.update,
        )
