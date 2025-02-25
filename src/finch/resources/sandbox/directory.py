# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.sandbox import directory_create_params
from ...types.sandbox.directory_create_response import DirectoryCreateResponse

__all__ = ["Directory", "AsyncDirectory"]


class Directory(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DirectoryWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return DirectoryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DirectoryWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return DirectoryWithStreamingResponse(self)

    def create(
        self,
        *,
        body: Iterable[directory_create_params.Body] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DirectoryCreateResponse:
        """
        Add new individuals to a sandbox company

        Args:
          body: Array of individuals to create. Takes all combined fields from `/individual` and
              `/employment` endpoints. All fields are optional.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sandbox/directory",
            body=maybe_transform(body, Iterable[directory_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectoryCreateResponse,
        )


class AsyncDirectory(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDirectoryWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDirectoryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDirectoryWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AsyncDirectoryWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: Iterable[directory_create_params.Body] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DirectoryCreateResponse:
        """
        Add new individuals to a sandbox company

        Args:
          body: Array of individuals to create. Takes all combined fields from `/individual` and
              `/employment` endpoints. All fields are optional.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sandbox/directory",
            body=await async_maybe_transform(body, Iterable[directory_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectoryCreateResponse,
        )


class DirectoryWithRawResponse:
    def __init__(self, directory: Directory) -> None:
        self._directory = directory

        self.create = _legacy_response.to_raw_response_wrapper(
            directory.create,
        )


class AsyncDirectoryWithRawResponse:
    def __init__(self, directory: AsyncDirectory) -> None:
        self._directory = directory

        self.create = _legacy_response.async_to_raw_response_wrapper(
            directory.create,
        )


class DirectoryWithStreamingResponse:
    def __init__(self, directory: Directory) -> None:
        self._directory = directory

        self.create = to_streamed_response_wrapper(
            directory.create,
        )


class AsyncDirectoryWithStreamingResponse:
    def __init__(self, directory: AsyncDirectory) -> None:
        self._directory = directory

        self.create = async_to_streamed_response_wrapper(
            directory.create,
        )
