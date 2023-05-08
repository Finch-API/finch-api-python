# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncIndividualsPage, AsyncIndividualsPage
from ...types.hris import IndividualInDirectory, directory_list_individuals_params
from ..._base_client import AsyncPaginator, make_request_options

__all__ = ["Directory", "AsyncDirectory"]


class Directory(SyncAPIResource):
    def list_individuals(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncIndividualsPage[IndividualInDirectory]:
        """
        Read company directory and organization structure

        Args:
          limit: Number of employees to return (defaults to all)

          offset: Index to start from (defaults to 0)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/directory",
            page=SyncIndividualsPage[IndividualInDirectory],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    directory_list_individuals_params.DirectoryListIndividualsParams,
                ),
            ),
            model=IndividualInDirectory,
        )


class AsyncDirectory(AsyncAPIResource):
    def list_individuals(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[IndividualInDirectory, AsyncIndividualsPage[IndividualInDirectory]]:
        """
        Read company directory and organization structure

        Args:
          limit: Number of employees to return (defaults to all)

          offset: Index to start from (defaults to 0)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/directory",
            page=AsyncIndividualsPage[IndividualInDirectory],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    directory_list_individuals_params.DirectoryListIndividualsParams,
                ),
            ),
            model=IndividualInDirectory,
        )
