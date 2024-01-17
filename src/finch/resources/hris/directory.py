# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import typing_extensions

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncIndividualsPage, AsyncIndividualsPage
from ...types.hris import IndividualInDirectory, directory_list_params
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["Directory", "AsyncDirectory"]


class Directory(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DirectoryWithRawResponse:
        return DirectoryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DirectoryWithStreamingResponse:
        return DirectoryWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
                    directory_list_params.DirectoryListParams,
                ),
            ),
            model=IndividualInDirectory,
        )

    @typing_extensions.deprecated("use `list` instead")
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        return self.list(
            limit=limit,
            offset=offset,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )


class AsyncDirectory(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDirectoryWithRawResponse:
        return AsyncDirectoryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDirectoryWithStreamingResponse:
        return AsyncDirectoryWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
                    directory_list_params.DirectoryListParams,
                ),
            ),
            model=IndividualInDirectory,
        )

    @typing_extensions.deprecated("use `list` instead")
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        return self.list(
            limit=limit,
            offset=offset,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )


class DirectoryWithRawResponse:
    def __init__(self, directory: Directory) -> None:
        self._directory = directory

        self.list = _legacy_response.to_raw_response_wrapper(
            directory.list,
        )
        self.list_individuals = (  # pyright: ignore[reportDeprecated]
            _legacy_response.to_raw_response_wrapper(
                directory.list_individuals  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncDirectoryWithRawResponse:
    def __init__(self, directory: AsyncDirectory) -> None:
        self._directory = directory

        self.list = _legacy_response.async_to_raw_response_wrapper(
            directory.list,
        )
        self.list_individuals = (  # pyright: ignore[reportDeprecated]
            _legacy_response.async_to_raw_response_wrapper(
                directory.list_individuals  # pyright: ignore[reportDeprecated],
            )
        )


class DirectoryWithStreamingResponse:
    def __init__(self, directory: Directory) -> None:
        self._directory = directory

        self.list = to_streamed_response_wrapper(
            directory.list,
        )
        self.list_individuals = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                directory.list_individuals  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncDirectoryWithStreamingResponse:
    def __init__(self, directory: AsyncDirectory) -> None:
        self._directory = directory

        self.list = async_to_streamed_response_wrapper(
            directory.list,
        )
        self.list_individuals = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                directory.list_individuals  # pyright: ignore[reportDeprecated],
            )
        )
