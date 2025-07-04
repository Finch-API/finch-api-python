# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from .... import _legacy_response
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.hris.benefits import (
    individual_enroll_many_params,
    individual_unenroll_many_params,
    individual_retrieve_many_benefits_params,
)
from ....types.hris.benefits.individual_benefit import IndividualBenefit
from ....types.hris.benefits.individual_enrolled_ids_response import IndividualEnrolledIDsResponse
from ....types.hris.benefits.enrolled_individual_benefit_response import EnrolledIndividualBenefitResponse
from ....types.hris.benefits.unenrolled_individual_benefit_response import UnenrolledIndividualBenefitResponse

__all__ = ["Individuals", "AsyncIndividuals"]


class Individuals(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndividualsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return IndividualsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndividualsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return IndividualsWithStreamingResponse(self)

    def enroll_many(
        self,
        benefit_id: str,
        *,
        individuals: Iterable[individual_enroll_many_params.Individual] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnrolledIndividualBenefitResponse:
        """Enroll an individual into a deduction or contribution.

        This is an overwrite
        operation. If the employee is already enrolled, the enrollment amounts will be
        adjusted. Making the same request multiple times will not create new
        enrollments, but will continue to set the state of the existing enrollment.

        Args:
          individuals: Array of the individual_id to enroll and a configuration object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return self._post(
            f"/employer/benefits/{benefit_id}/individuals",
            body=maybe_transform(individuals, Iterable[individual_enroll_many_params.Individual]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrolledIndividualBenefitResponse,
        )

    def enrolled_ids(
        self,
        benefit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndividualEnrolledIDsResponse:
        """
        Lists individuals currently enrolled in a given deduction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return self._get(
            f"/employer/benefits/{benefit_id}/enrolled",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndividualEnrolledIDsResponse,
        )

    def retrieve_many_benefits(
        self,
        benefit_id: str,
        *,
        individual_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[IndividualBenefit]:
        """
        Get enrollment information for the given individuals.

        Args:
          individual_ids: comma-delimited list of stable Finch uuids for each individual. If empty,
              defaults to all individuals

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return self._get_api_list(
            f"/employer/benefits/{benefit_id}/individuals",
            page=SyncSinglePage[IndividualBenefit],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"individual_ids": individual_ids},
                    individual_retrieve_many_benefits_params.IndividualRetrieveManyBenefitsParams,
                ),
            ),
            model=IndividualBenefit,
        )

    def unenroll_many(
        self,
        benefit_id: str,
        *,
        individual_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnenrolledIndividualBenefitResponse:
        """
        Unenroll individuals from a deduction or contribution

        Args:
          individual_ids: Array of individual_ids to unenroll.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return self._delete(
            f"/employer/benefits/{benefit_id}/individuals",
            body=maybe_transform(
                {"individual_ids": individual_ids}, individual_unenroll_many_params.IndividualUnenrollManyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnenrolledIndividualBenefitResponse,
        )


class AsyncIndividuals(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndividualsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndividualsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndividualsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AsyncIndividualsWithStreamingResponse(self)

    async def enroll_many(
        self,
        benefit_id: str,
        *,
        individuals: Iterable[individual_enroll_many_params.Individual] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnrolledIndividualBenefitResponse:
        """Enroll an individual into a deduction or contribution.

        This is an overwrite
        operation. If the employee is already enrolled, the enrollment amounts will be
        adjusted. Making the same request multiple times will not create new
        enrollments, but will continue to set the state of the existing enrollment.

        Args:
          individuals: Array of the individual_id to enroll and a configuration object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return await self._post(
            f"/employer/benefits/{benefit_id}/individuals",
            body=await async_maybe_transform(individuals, Iterable[individual_enroll_many_params.Individual]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrolledIndividualBenefitResponse,
        )

    async def enrolled_ids(
        self,
        benefit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndividualEnrolledIDsResponse:
        """
        Lists individuals currently enrolled in a given deduction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return await self._get(
            f"/employer/benefits/{benefit_id}/enrolled",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndividualEnrolledIDsResponse,
        )

    def retrieve_many_benefits(
        self,
        benefit_id: str,
        *,
        individual_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[IndividualBenefit, AsyncSinglePage[IndividualBenefit]]:
        """
        Get enrollment information for the given individuals.

        Args:
          individual_ids: comma-delimited list of stable Finch uuids for each individual. If empty,
              defaults to all individuals

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return self._get_api_list(
            f"/employer/benefits/{benefit_id}/individuals",
            page=AsyncSinglePage[IndividualBenefit],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"individual_ids": individual_ids},
                    individual_retrieve_many_benefits_params.IndividualRetrieveManyBenefitsParams,
                ),
            ),
            model=IndividualBenefit,
        )

    async def unenroll_many(
        self,
        benefit_id: str,
        *,
        individual_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UnenrolledIndividualBenefitResponse:
        """
        Unenroll individuals from a deduction or contribution

        Args:
          individual_ids: Array of individual_ids to unenroll.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return await self._delete(
            f"/employer/benefits/{benefit_id}/individuals",
            body=await async_maybe_transform(
                {"individual_ids": individual_ids}, individual_unenroll_many_params.IndividualUnenrollManyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnenrolledIndividualBenefitResponse,
        )


class IndividualsWithRawResponse:
    def __init__(self, individuals: Individuals) -> None:
        self._individuals = individuals

        self.enroll_many = _legacy_response.to_raw_response_wrapper(
            individuals.enroll_many,
        )
        self.enrolled_ids = _legacy_response.to_raw_response_wrapper(
            individuals.enrolled_ids,
        )
        self.retrieve_many_benefits = _legacy_response.to_raw_response_wrapper(
            individuals.retrieve_many_benefits,
        )
        self.unenroll_many = _legacy_response.to_raw_response_wrapper(
            individuals.unenroll_many,
        )


class AsyncIndividualsWithRawResponse:
    def __init__(self, individuals: AsyncIndividuals) -> None:
        self._individuals = individuals

        self.enroll_many = _legacy_response.async_to_raw_response_wrapper(
            individuals.enroll_many,
        )
        self.enrolled_ids = _legacy_response.async_to_raw_response_wrapper(
            individuals.enrolled_ids,
        )
        self.retrieve_many_benefits = _legacy_response.async_to_raw_response_wrapper(
            individuals.retrieve_many_benefits,
        )
        self.unenroll_many = _legacy_response.async_to_raw_response_wrapper(
            individuals.unenroll_many,
        )


class IndividualsWithStreamingResponse:
    def __init__(self, individuals: Individuals) -> None:
        self._individuals = individuals

        self.enroll_many = to_streamed_response_wrapper(
            individuals.enroll_many,
        )
        self.enrolled_ids = to_streamed_response_wrapper(
            individuals.enrolled_ids,
        )
        self.retrieve_many_benefits = to_streamed_response_wrapper(
            individuals.retrieve_many_benefits,
        )
        self.unenroll_many = to_streamed_response_wrapper(
            individuals.unenroll_many,
        )


class AsyncIndividualsWithStreamingResponse:
    def __init__(self, individuals: AsyncIndividuals) -> None:
        self._individuals = individuals

        self.enroll_many = async_to_streamed_response_wrapper(
            individuals.enroll_many,
        )
        self.enrolled_ids = async_to_streamed_response_wrapper(
            individuals.enrolled_ids,
        )
        self.retrieve_many_benefits = async_to_streamed_response_wrapper(
            individuals.retrieve_many_benefits,
        )
        self.unenroll_many = async_to_streamed_response_wrapper(
            individuals.unenroll_many,
        )
