# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.hris.benefits import (
    IndividualBenefit,
    EnrolledIndividual,
    UnenrolledIndividual,
    IndividualEnrolledIDsResponse,
    individual_unenroll_params,
    individual_enroll_many_params,
    individual_retrieve_many_benefits_params,
)

__all__ = ["Individuals", "AsyncIndividuals"]


class Individuals(SyncAPIResource):
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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

    def unenroll(
        self,
        benefit_id: str,
        *,
        individual_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
                {"individual_ids": individual_ids}, individual_unenroll_params.IndividualUnenrollParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=UnenrolledIndividual,
            method="delete",
        )


class AsyncIndividuals(AsyncAPIResource):
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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

    def unenroll(
        self,
        benefit_id: str,
        *,
        individual_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
                {"individual_ids": individual_ids}, individual_unenroll_params.IndividualUnenrollParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=UnenrolledIndividual,
            method="delete",
        )
