# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.hris.benefits import (
    IndividualBenefit,
    EnrolledIndividual,
    UnenrolledIndividual,
    IndividualEnrolledIDsResponse,
    individual_enroll_many_params,
    individual_unenroll_many_params,
    individual_retrieve_many_benefits_params,
)

if TYPE_CHECKING:
    from ...._client import Finch, AsyncFinch

__all__ = ["Individuals", "AsyncIndividuals"]


class Individuals(SyncAPIResource):
    with_raw_response: IndividualsWithRawResponse

    def __init__(self, client: Finch) -> None:
        super().__init__(client)
        self.with_raw_response = IndividualsWithRawResponse(self)

    def enroll_many(
        self,
        benefit_id: str,
        *,
        individuals: List[individual_enroll_many_params.Individual],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[EnrolledIndividual]:
        """
        **Availability: Automated and Assisted Benefits providers**

        Enroll an individual into a benefit. If the employee is already enrolled, the
        enrollment amounts will be adjusted.

        <!-- theme: warning -->

        > Making changes to an individual's benefits may have tax consequences based on
        > IRS regulations. Please consult a tax expert to ensure all changes being made
        > to the system are compliant with local, state, and federal law.

        Args:
          individuals: Array of the individual_id to enroll and a configuration object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/employer/benefits/{benefit_id}/individuals",
            page=SyncSinglePage[EnrolledIndividual],
            body=maybe_transform(individuals, individual_enroll_many_params.IndividualEnrollManyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=EnrolledIndividual,
            method="post",
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
        **Availability: Automated Benefits providers only**

        Lists individuals currently enrolled in a given benefit.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        **Availability: Automated Benefits providers only**

        Get enrolled benefit information for the given individuals.

        Args:
          individual_ids: comma-delimited list of stable Finch uuids for each individual. If empty,
              defaults to all individuals

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
    ) -> SyncSinglePage[UnenrolledIndividual]:
        """
        **Availability: Automated and Assisted Benefits providers**

        Unenroll individuals from a benefit

        Args:
          individual_ids: Array of individual_ids to unenroll.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/employer/benefits/{benefit_id}/individuals",
            page=SyncSinglePage[UnenrolledIndividual],
            body=maybe_transform(
                {"individual_ids": individual_ids}, individual_unenroll_many_params.IndividualUnenrollManyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=UnenrolledIndividual,
            method="delete",
        )


class AsyncIndividuals(AsyncAPIResource):
    with_raw_response: AsyncIndividualsWithRawResponse

    def __init__(self, client: AsyncFinch) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncIndividualsWithRawResponse(self)

    def enroll_many(
        self,
        benefit_id: str,
        *,
        individuals: List[individual_enroll_many_params.Individual],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EnrolledIndividual, AsyncSinglePage[EnrolledIndividual]]:
        """
        **Availability: Automated and Assisted Benefits providers**

        Enroll an individual into a benefit. If the employee is already enrolled, the
        enrollment amounts will be adjusted.

        <!-- theme: warning -->

        > Making changes to an individual's benefits may have tax consequences based on
        > IRS regulations. Please consult a tax expert to ensure all changes being made
        > to the system are compliant with local, state, and federal law.

        Args:
          individuals: Array of the individual_id to enroll and a configuration object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/employer/benefits/{benefit_id}/individuals",
            page=AsyncSinglePage[EnrolledIndividual],
            body=maybe_transform(individuals, individual_enroll_many_params.IndividualEnrollManyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=EnrolledIndividual,
            method="post",
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
        **Availability: Automated Benefits providers only**

        Lists individuals currently enrolled in a given benefit.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        **Availability: Automated Benefits providers only**

        Get enrolled benefit information for the given individuals.

        Args:
          individual_ids: comma-delimited list of stable Finch uuids for each individual. If empty,
              defaults to all individuals

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
    ) -> AsyncPaginator[UnenrolledIndividual, AsyncSinglePage[UnenrolledIndividual]]:
        """
        **Availability: Automated and Assisted Benefits providers**

        Unenroll individuals from a benefit

        Args:
          individual_ids: Array of individual_ids to unenroll.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/employer/benefits/{benefit_id}/individuals",
            page=AsyncSinglePage[UnenrolledIndividual],
            body=maybe_transform(
                {"individual_ids": individual_ids}, individual_unenroll_many_params.IndividualUnenrollManyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=UnenrolledIndividual,
            method="delete",
        )


class IndividualsWithRawResponse:
    def __init__(self, individuals: Individuals) -> None:
        self.enroll_many = to_raw_response_wrapper(
            individuals.enroll_many,
        )
        self.enrolled_ids = to_raw_response_wrapper(
            individuals.enrolled_ids,
        )
        self.retrieve_many_benefits = to_raw_response_wrapper(
            individuals.retrieve_many_benefits,
        )
        self.unenroll_many = to_raw_response_wrapper(
            individuals.unenroll_many,
        )


class AsyncIndividualsWithRawResponse:
    def __init__(self, individuals: AsyncIndividuals) -> None:
        self.enroll_many = async_to_raw_response_wrapper(
            individuals.enroll_many,
        )
        self.enrolled_ids = async_to_raw_response_wrapper(
            individuals.enrolled_ids,
        )
        self.retrieve_many_benefits = async_to_raw_response_wrapper(
            individuals.retrieve_many_benefits,
        )
        self.unenroll_many = async_to_raw_response_wrapper(
            individuals.unenroll_many,
        )
