# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...types import LocationParam
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.sandbox import IndividualUpdateResponse, individual_update_params

__all__ = ["Individual", "AsyncIndividual"]


class Individual(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndividualWithRawResponse:
        return IndividualWithRawResponse(self)

    def update(
        self,
        individual_id: str,
        *,
        dob: Optional[str] | NotGiven = NOT_GIVEN,
        emails: Optional[List[individual_update_params.Email]] | NotGiven = NOT_GIVEN,
        encrypted_ssn: Optional[str] | NotGiven = NOT_GIVEN,
        ethnicity: Optional[
            Literal[
                "asian",
                "white",
                "black_or_african_american",
                "native_hawaiian_or_pacific_islander",
                "american_indian_or_alaska_native",
                "hispanic_or_latino",
                "two_or_more_races",
                "decline_to_specify",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        gender: Optional[Literal["female", "male", "other", "decline_to_specify"]] | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        middle_name: Optional[str] | NotGiven = NOT_GIVEN,
        phone_numbers: Optional[List[Optional[individual_update_params.PhoneNumber]]] | NotGiven = NOT_GIVEN,
        preferred_name: Optional[str] | NotGiven = NOT_GIVEN,
        residence: Optional[LocationParam] | NotGiven = NOT_GIVEN,
        ssn: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndividualUpdateResponse:
        """
        Update sandbox individual

        Args:
          encrypted_ssn: Social Security Number of the individual in **encrypted** format. This field is
              only available with the `ssn` scope enabled and the
              `options: { include: ['ssn'] }` param set in the body.

          ethnicity: The EEOC-defined ethnicity of the individual.

          first_name: The legal first name of the individual.

          gender: The gender of the individual.

          last_name: The legal last name of the individual.

          middle_name: The legal middle name of the individual.

          preferred_name: The preferred name of the individual.

          residence

          ssn: Social Security Number of the individual. This field is only available with the
              `ssn` scope enabled and the `options: { include: ['ssn'] }` param set in the
              body.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/sandbox/individual/{individual_id}",
            body=maybe_transform(
                {
                    "dob": dob,
                    "emails": emails,
                    "encrypted_ssn": encrypted_ssn,
                    "ethnicity": ethnicity,
                    "first_name": first_name,
                    "gender": gender,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "phone_numbers": phone_numbers,
                    "preferred_name": preferred_name,
                    "residence": residence,
                    "ssn": ssn,
                },
                individual_update_params.IndividualUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndividualUpdateResponse,
        )


class AsyncIndividual(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndividualWithRawResponse:
        return AsyncIndividualWithRawResponse(self)

    async def update(
        self,
        individual_id: str,
        *,
        dob: Optional[str] | NotGiven = NOT_GIVEN,
        emails: Optional[List[individual_update_params.Email]] | NotGiven = NOT_GIVEN,
        encrypted_ssn: Optional[str] | NotGiven = NOT_GIVEN,
        ethnicity: Optional[
            Literal[
                "asian",
                "white",
                "black_or_african_american",
                "native_hawaiian_or_pacific_islander",
                "american_indian_or_alaska_native",
                "hispanic_or_latino",
                "two_or_more_races",
                "decline_to_specify",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        gender: Optional[Literal["female", "male", "other", "decline_to_specify"]] | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        middle_name: Optional[str] | NotGiven = NOT_GIVEN,
        phone_numbers: Optional[List[Optional[individual_update_params.PhoneNumber]]] | NotGiven = NOT_GIVEN,
        preferred_name: Optional[str] | NotGiven = NOT_GIVEN,
        residence: Optional[LocationParam] | NotGiven = NOT_GIVEN,
        ssn: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndividualUpdateResponse:
        """
        Update sandbox individual

        Args:
          encrypted_ssn: Social Security Number of the individual in **encrypted** format. This field is
              only available with the `ssn` scope enabled and the
              `options: { include: ['ssn'] }` param set in the body.

          ethnicity: The EEOC-defined ethnicity of the individual.

          first_name: The legal first name of the individual.

          gender: The gender of the individual.

          last_name: The legal last name of the individual.

          middle_name: The legal middle name of the individual.

          preferred_name: The preferred name of the individual.

          residence

          ssn: Social Security Number of the individual. This field is only available with the
              `ssn` scope enabled and the `options: { include: ['ssn'] }` param set in the
              body.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/sandbox/individual/{individual_id}",
            body=maybe_transform(
                {
                    "dob": dob,
                    "emails": emails,
                    "encrypted_ssn": encrypted_ssn,
                    "ethnicity": ethnicity,
                    "first_name": first_name,
                    "gender": gender,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "phone_numbers": phone_numbers,
                    "preferred_name": preferred_name,
                    "residence": residence,
                    "ssn": ssn,
                },
                individual_update_params.IndividualUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndividualUpdateResponse,
        )


class IndividualWithRawResponse:
    def __init__(self, individual: Individual) -> None:
        self.update = to_raw_response_wrapper(
            individual.update,
        )


class AsyncIndividualWithRawResponse:
    def __init__(self, individual: AsyncIndividual) -> None:
        self.update = async_to_raw_response_wrapper(
            individual.update,
        )
