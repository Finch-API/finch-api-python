# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .... import _legacy_response
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.hris.benefits import (
    individual_enroll_many_params,
    individual_enrolled_ids_params,
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
        entity_ids: SequenceNotStr[str] | Omit = omit,
        individuals: Iterable[individual_enroll_many_params.Individual] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrolledIndividualBenefitResponse:
        """Enroll an individual into a deduction or contribution.

        This is an overwrite
        operation. If the employee is already enrolled, the enrollment amounts will be
        adjusted. Making the same request multiple times will not create new
        enrollments, but will continue to set the state of the existing enrollment.

        Args:
          entity_ids: The entity IDs to specify which entities' data to access. Provide exactly one
              entity ID per request; a maximum of one is accepted.

          individuals: Array of the individual_id to enroll and a configuration object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return self._post(
            path_template("/employer/benefits/{benefit_id}/individuals", benefit_id=benefit_id),
            body=maybe_transform(individuals, Iterable[individual_enroll_many_params.Individual]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"entity_ids": entity_ids}, individual_enroll_many_params.IndividualEnrollManyParams
                ),
                security={"bearer_auth": True},
            ),
            cast_to=EnrolledIndividualBenefitResponse,
        )

    def enrolled_ids(
        self,
        benefit_id: str,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndividualEnrolledIDsResponse:
        """
        Lists individuals currently enrolled in a given deduction.

        Args:
          entity_ids: The entity IDs to specify which entities' data to access. Provide exactly one
              entity ID per request; a maximum of one is accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return self._get(
            path_template("/employer/benefits/{benefit_id}/enrolled", benefit_id=benefit_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"entity_ids": entity_ids}, individual_enrolled_ids_params.IndividualEnrolledIDsParams
                ),
                security={"bearer_auth": True},
            ),
            cast_to=IndividualEnrolledIDsResponse,
        )

    def retrieve_many_benefits(
        self,
        benefit_id: str,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        individual_ids: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[IndividualBenefit]:
        """
        Get enrollment information for the given individuals.

        Args:
          entity_ids: The entity IDs to specify which entities' data to access. Provide exactly one
              entity ID per request; a maximum of one is accepted.

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
            path_template("/employer/benefits/{benefit_id}/individuals", benefit_id=benefit_id),
            page=SyncSinglePage[IndividualBenefit],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_ids": entity_ids,
                        "individual_ids": individual_ids,
                    },
                    individual_retrieve_many_benefits_params.IndividualRetrieveManyBenefitsParams,
                ),
                security={"bearer_auth": True},
            ),
            model=IndividualBenefit,
        )

    def unenroll_many(
        self,
        benefit_id: str,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        individual_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnenrolledIndividualBenefitResponse:
        """
        Unenroll individuals from a deduction or contribution

        Args:
          entity_ids: The entity IDs to specify which entities' data to access. Provide exactly one
              entity ID per request; a maximum of one is accepted.

          individual_ids: Array of individual_ids to unenroll.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return self._delete(
            path_template("/employer/benefits/{benefit_id}/individuals", benefit_id=benefit_id),
            body=maybe_transform(
                {"individual_ids": individual_ids}, individual_unenroll_many_params.IndividualUnenrollManyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"entity_ids": entity_ids}, individual_unenroll_many_params.IndividualUnenrollManyParams
                ),
                security={"bearer_auth": True},
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
        entity_ids: SequenceNotStr[str] | Omit = omit,
        individuals: Iterable[individual_enroll_many_params.Individual] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrolledIndividualBenefitResponse:
        """Enroll an individual into a deduction or contribution.

        This is an overwrite
        operation. If the employee is already enrolled, the enrollment amounts will be
        adjusted. Making the same request multiple times will not create new
        enrollments, but will continue to set the state of the existing enrollment.

        Args:
          entity_ids: The entity IDs to specify which entities' data to access. Provide exactly one
              entity ID per request; a maximum of one is accepted.

          individuals: Array of the individual_id to enroll and a configuration object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return await self._post(
            path_template("/employer/benefits/{benefit_id}/individuals", benefit_id=benefit_id),
            body=await async_maybe_transform(individuals, Iterable[individual_enroll_many_params.Individual]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"entity_ids": entity_ids}, individual_enroll_many_params.IndividualEnrollManyParams
                ),
                security={"bearer_auth": True},
            ),
            cast_to=EnrolledIndividualBenefitResponse,
        )

    async def enrolled_ids(
        self,
        benefit_id: str,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndividualEnrolledIDsResponse:
        """
        Lists individuals currently enrolled in a given deduction.

        Args:
          entity_ids: The entity IDs to specify which entities' data to access. Provide exactly one
              entity ID per request; a maximum of one is accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return await self._get(
            path_template("/employer/benefits/{benefit_id}/enrolled", benefit_id=benefit_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"entity_ids": entity_ids}, individual_enrolled_ids_params.IndividualEnrolledIDsParams
                ),
                security={"bearer_auth": True},
            ),
            cast_to=IndividualEnrolledIDsResponse,
        )

    def retrieve_many_benefits(
        self,
        benefit_id: str,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        individual_ids: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[IndividualBenefit, AsyncSinglePage[IndividualBenefit]]:
        """
        Get enrollment information for the given individuals.

        Args:
          entity_ids: The entity IDs to specify which entities' data to access. Provide exactly one
              entity ID per request; a maximum of one is accepted.

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
            path_template("/employer/benefits/{benefit_id}/individuals", benefit_id=benefit_id),
            page=AsyncSinglePage[IndividualBenefit],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_ids": entity_ids,
                        "individual_ids": individual_ids,
                    },
                    individual_retrieve_many_benefits_params.IndividualRetrieveManyBenefitsParams,
                ),
                security={"bearer_auth": True},
            ),
            model=IndividualBenefit,
        )

    async def unenroll_many(
        self,
        benefit_id: str,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        individual_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnenrolledIndividualBenefitResponse:
        """
        Unenroll individuals from a deduction or contribution

        Args:
          entity_ids: The entity IDs to specify which entities' data to access. Provide exactly one
              entity ID per request; a maximum of one is accepted.

          individual_ids: Array of individual_ids to unenroll.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not benefit_id:
            raise ValueError(f"Expected a non-empty value for `benefit_id` but received {benefit_id!r}")
        return await self._delete(
            path_template("/employer/benefits/{benefit_id}/individuals", benefit_id=benefit_id),
            body=await async_maybe_transform(
                {"individual_ids": individual_ids}, individual_unenroll_many_params.IndividualUnenrollManyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"entity_ids": entity_ids}, individual_unenroll_many_params.IndividualUnenrollManyParams
                ),
                security={"bearer_auth": True},
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
