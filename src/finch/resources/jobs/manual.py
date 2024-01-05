# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...types.jobs import ManualAsyncJob
from ..._base_client import (
    make_request_options,
)

__all__ = ["Manual", "AsyncManual"]


class Manual(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ManualWithRawResponse:
        return ManualWithRawResponse(self)

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
        return self._get(
            f"/jobs/manual/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManualAsyncJob,
        )


class AsyncManual(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncManualWithRawResponse:
        return AsyncManualWithRawResponse(self)

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
        return await self._get(
            f"/jobs/manual/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManualAsyncJob,
        )


class ManualWithRawResponse:
    def __init__(self, manual: Manual) -> None:
        self.retrieve = to_raw_response_wrapper(
            manual.retrieve,
        )


class AsyncManualWithRawResponse:
    def __init__(self, manual: AsyncManual) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            manual.retrieve,
        )
