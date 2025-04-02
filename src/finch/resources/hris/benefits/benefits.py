# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .... import _legacy_response
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from .individuals import (
    Individuals,
    AsyncIndividuals,
    IndividualsWithRawResponse,
    AsyncIndividualsWithRawResponse,
    IndividualsWithStreamingResponse,
    AsyncIndividualsWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ....types.hris import BenefitType, BenefitFrequency, benefit_create_params, benefit_update_params
from ...._base_client import AsyncPaginator, make_request_options
from ....types.hris.benefit_type import BenefitType
from ....types.hris.company_benefit import CompanyBenefit
from ....types.hris.benefit_frequency import BenefitFrequency
from ....types.hris.supported_benefit import SupportedBenefit
from ....types.hris.update_company_benefit_response import UpdateCompanyBenefitResponse
from ....types.hris.create_company_benefits_response import CreateCompanyBenefitsResponse

__all__ = ["Benefits", "AsyncBenefits"]


class Benefits(SyncAPIResource):
    @cached_property
    def individuals(self) -> Individuals:
        return Individuals(self._client)

    @cached_property
    def with_raw_response(self) -> BenefitsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return BenefitsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BenefitsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return BenefitsWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str | NotGiven = NOT_GIVEN,
        frequency: Optional[BenefitFrequency] | NotGiven = NOT_GIVEN,
        type: Optional[BenefitType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateCompanyBenefitsResponse:
        """Creates a new company-wide deduction or contribution.

        Please use the
        `/providers` endpoint to view available types for each provider.

        Args:
          description: Name of the benefit as it appears in the provider and pay statements. Recommend
              limiting this to <30 characters due to limitations in specific providers (e.g.
              Justworks).

          frequency: The frequency of the benefit deduction/contribution.

          type: Type of benefit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/employer/benefits",
            body=maybe_transform(
                {
                    "description": description,
                    "frequency": frequency,
                    "type": type,
                },
                benefit_create_params.BenefitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateCompanyBenefitsResponse,
        )

    def retrieve(
        self,
        benefit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyBenefit:
        """
        Lists deductions and contributions information for a given item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return self._get(
            f"/employer/benefits/{benefit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyBenefit,
        )

    def update(
        self,
        benefit_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpdateCompanyBenefitResponse:
        """
        Updates an existing company-wide deduction or contribution

        Args:
          description: Updated name or description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return self._post(
            f"/employer/benefits/{benefit_id}",
            body=maybe_transform({"description": description}, benefit_update_params.BenefitUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateCompanyBenefitResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[CompanyBenefit]:
        """List all company-wide deductions and contributions."""
        return self._get_api_list(
            "/employer/benefits",
            page=SyncSinglePage[CompanyBenefit],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CompanyBenefit,
        )

    def list_supported_benefits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[SupportedBenefit]:
        """Get deductions metadata"""
        return self._get_api_list(
            "/employer/benefits/meta",
            page=SyncSinglePage[SupportedBenefit],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SupportedBenefit,
        )


class AsyncBenefits(AsyncAPIResource):
    @cached_property
    def individuals(self) -> AsyncIndividuals:
        return AsyncIndividuals(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBenefitsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBenefitsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBenefitsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AsyncBenefitsWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str | NotGiven = NOT_GIVEN,
        frequency: Optional[BenefitFrequency] | NotGiven = NOT_GIVEN,
        type: Optional[BenefitType] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateCompanyBenefitsResponse:
        """Creates a new company-wide deduction or contribution.

        Please use the
        `/providers` endpoint to view available types for each provider.

        Args:
          description: Name of the benefit as it appears in the provider and pay statements. Recommend
              limiting this to <30 characters due to limitations in specific providers (e.g.
              Justworks).

          frequency: The frequency of the benefit deduction/contribution.

          type: Type of benefit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/employer/benefits",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "frequency": frequency,
                    "type": type,
                },
                benefit_create_params.BenefitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateCompanyBenefitsResponse,
        )

    async def retrieve(
        self,
        benefit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyBenefit:
        """
        Lists deductions and contributions information for a given item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return await self._get(
            f"/employer/benefits/{benefit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyBenefit,
        )

    async def update(
        self,
        benefit_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpdateCompanyBenefitResponse:
        """
        Updates an existing company-wide deduction or contribution

        Args:
          description: Updated name or description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return await self._post(
            f"/employer/benefits/{benefit_id}",
            body=await async_maybe_transform({"description": description}, benefit_update_params.BenefitUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateCompanyBenefitResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CompanyBenefit, AsyncSinglePage[CompanyBenefit]]:
        """List all company-wide deductions and contributions."""
        return self._get_api_list(
            "/employer/benefits",
            page=AsyncSinglePage[CompanyBenefit],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CompanyBenefit,
        )

    def list_supported_benefits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SupportedBenefit, AsyncSinglePage[SupportedBenefit]]:
        """Get deductions metadata"""
        return self._get_api_list(
            "/employer/benefits/meta",
            page=AsyncSinglePage[SupportedBenefit],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SupportedBenefit,
        )


class BenefitsWithRawResponse:
    def __init__(self, benefits: Benefits) -> None:
        self._benefits = benefits

        self.create = _legacy_response.to_raw_response_wrapper(
            benefits.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            benefits.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            benefits.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            benefits.list,
        )
        self.list_supported_benefits = _legacy_response.to_raw_response_wrapper(
            benefits.list_supported_benefits,
        )

    @cached_property
    def individuals(self) -> IndividualsWithRawResponse:
        return IndividualsWithRawResponse(self._benefits.individuals)


class AsyncBenefitsWithRawResponse:
    def __init__(self, benefits: AsyncBenefits) -> None:
        self._benefits = benefits

        self.create = _legacy_response.async_to_raw_response_wrapper(
            benefits.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            benefits.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            benefits.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            benefits.list,
        )
        self.list_supported_benefits = _legacy_response.async_to_raw_response_wrapper(
            benefits.list_supported_benefits,
        )

    @cached_property
    def individuals(self) -> AsyncIndividualsWithRawResponse:
        return AsyncIndividualsWithRawResponse(self._benefits.individuals)


class BenefitsWithStreamingResponse:
    def __init__(self, benefits: Benefits) -> None:
        self._benefits = benefits

        self.create = to_streamed_response_wrapper(
            benefits.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            benefits.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            benefits.update,
        )
        self.list = to_streamed_response_wrapper(
            benefits.list,
        )
        self.list_supported_benefits = to_streamed_response_wrapper(
            benefits.list_supported_benefits,
        )

    @cached_property
    def individuals(self) -> IndividualsWithStreamingResponse:
        return IndividualsWithStreamingResponse(self._benefits.individuals)


class AsyncBenefitsWithStreamingResponse:
    def __init__(self, benefits: AsyncBenefits) -> None:
        self._benefits = benefits

        self.create = async_to_streamed_response_wrapper(
            benefits.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            benefits.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            benefits.update,
        )
        self.list = async_to_streamed_response_wrapper(
            benefits.list,
        )
        self.list_supported_benefits = async_to_streamed_response_wrapper(
            benefits.list_supported_benefits,
        )

    @cached_property
    def individuals(self) -> AsyncIndividualsWithStreamingResponse:
        return AsyncIndividualsWithStreamingResponse(self._benefits.individuals)
