# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncResponsesPage, AsyncResponsesPage
from ...types.hris import IndividualResponse, individual_retrieve_many_params
from ..._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ..._client import Finch, AsyncFinch

__all__ = ["Individuals", "AsyncIndividuals"]


class Individuals(SyncAPIResource):
    with_raw_response: IndividualsWithRawResponse

    def __init__(self, client: Finch) -> None:
        super().__init__(client)
        self.with_raw_response = IndividualsWithRawResponse(self)

    def retrieve_many(
        self,
        *,
        options: Optional[individual_retrieve_many_params.Options] | NotGiven = NOT_GIVEN,
        requests: List[individual_retrieve_many_params.Request] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncResponsesPage[IndividualResponse]:
        """
        Read individual data, excluding income and employment data

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/individual",
            page=SyncResponsesPage[IndividualResponse],
            body=maybe_transform(
                {
                    "options": options,
                    "requests": requests,
                },
                individual_retrieve_many_params.IndividualRetrieveManyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=IndividualResponse,
            method="post",
        )


class AsyncIndividuals(AsyncAPIResource):
    with_raw_response: AsyncIndividualsWithRawResponse

    def __init__(self, client: AsyncFinch) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncIndividualsWithRawResponse(self)

    def retrieve_many(
        self,
        *,
        options: Optional[individual_retrieve_many_params.Options] | NotGiven = NOT_GIVEN,
        requests: List[individual_retrieve_many_params.Request] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[IndividualResponse, AsyncResponsesPage[IndividualResponse]]:
        """
        Read individual data, excluding income and employment data

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/individual",
            page=AsyncResponsesPage[IndividualResponse],
            body=maybe_transform(
                {
                    "options": options,
                    "requests": requests,
                },
                individual_retrieve_many_params.IndividualRetrieveManyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=IndividualResponse,
            method="post",
        )


class IndividualsWithRawResponse:
    def __init__(self, individuals: Individuals) -> None:
        self.retrieve_many = to_raw_response_wrapper(
            individuals.retrieve_many,
        )


class AsyncIndividualsWithRawResponse:
    def __init__(self, individuals: AsyncIndividuals) -> None:
        self.retrieve_many = async_to_raw_response_wrapper(
            individuals.retrieve_many,
        )
