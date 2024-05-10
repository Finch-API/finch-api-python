# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.jobs.manual_async_job import ManualAsyncJob

__all__ = ["ManualResource", "AsyncManualResource"]


class ManualResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ManualResourceWithRawResponse:
        return ManualResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManualResourceWithStreamingResponse:
        return ManualResourceWithStreamingResponse(self)

    def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManualAsyncJob:
        """Get a manual job by `job_id`.

        Manual jobs are completed by a human and include
        Assisted Benefits jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/jobs/manual/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManualAsyncJob,
        )


class AsyncManualResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncManualResourceWithRawResponse:
        return AsyncManualResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManualResourceWithStreamingResponse:
        return AsyncManualResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManualAsyncJob:
        """Get a manual job by `job_id`.

        Manual jobs are completed by a human and include
        Assisted Benefits jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/jobs/manual/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManualAsyncJob,
        )


class ManualResourceWithRawResponse:
    def __init__(self, manual: ManualResource) -> None:
        self._manual = manual

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            manual.retrieve,
        )


class AsyncManualResourceWithRawResponse:
    def __init__(self, manual: AsyncManualResource) -> None:
        self._manual = manual

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            manual.retrieve,
        )


class ManualResourceWithStreamingResponse:
    def __init__(self, manual: ManualResource) -> None:
        self._manual = manual

        self.retrieve = to_streamed_response_wrapper(
            manual.retrieve,
        )


class AsyncManualResourceWithStreamingResponse:
    def __init__(self, manual: AsyncManualResource) -> None:
        self._manual = manual

        self.retrieve = async_to_streamed_response_wrapper(
            manual.retrieve,
        )
