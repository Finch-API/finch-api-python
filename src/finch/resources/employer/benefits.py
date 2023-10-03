# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.hris import BenefitType, BenefitFrequency
from ..._base_client import make_request_options
from ...types.employer import RegisterCompanyBenefitsResponse, benefit_register_params

__all__ = ["Benefits", "AsyncBenefits"]


class Benefits(SyncAPIResource):
    def register(
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> RegisterCompanyBenefitsResponse:
        """
        **Availability: Assisted Benefits providers only**

        Register existing benefits from the customer on the provider, on Finch's end.
        Please use the `/provider` endpoint to view available types for each provider.

        Args:
          type: Type of benefit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/employer/benefits/register",
            body=maybe_transform(
                {
                    "description": description,
                    "frequency": frequency,
                    "type": type,
                },
                benefit_register_params.BenefitRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegisterCompanyBenefitsResponse,
        )


class AsyncBenefits(AsyncAPIResource):
    async def register(
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> RegisterCompanyBenefitsResponse:
        """
        **Availability: Assisted Benefits providers only**

        Register existing benefits from the customer on the provider, on Finch's end.
        Please use the `/provider` endpoint to view available types for each provider.

        Args:
          type: Type of benefit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/employer/benefits/register",
            body=maybe_transform(
                {
                    "description": description,
                    "frequency": frequency,
                    "type": type,
                },
                benefit_register_params.BenefitRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegisterCompanyBenefitsResponse,
        )
