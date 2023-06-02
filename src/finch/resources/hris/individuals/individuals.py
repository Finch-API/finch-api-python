# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....pagination import SyncResponsesPage, AsyncResponsesPage
from ....types.hris import IndividualResponse, individual_retrieve_many_params
from ...._base_client import AsyncPaginator, make_request_options
from .employment_data import EmploymentData, AsyncEmploymentData

if TYPE_CHECKING:
    from ...._client import Finch, AsyncFinch

__all__ = ["Individuals", "AsyncIndividuals"]


class Individuals(SyncAPIResource):
    employment_data: EmploymentData

    def __init__(self, client: Finch) -> None:
        super().__init__(client)
        self.employment_data = EmploymentData(client)

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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
    employment_data: AsyncEmploymentData

    def __init__(self, client: AsyncFinch) -> None:
        super().__init__(client)
        self.employment_data = AsyncEmploymentData(client)

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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
