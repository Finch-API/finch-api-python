# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

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
from ...pagination import SyncPage, AsyncPage
from ...types.jobs import AutomatedAsyncJob, AutomatedCreateResponse, automated_list_params, automated_create_params
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["Automated", "AsyncAutomated"]


class Automated(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutomatedWithRawResponse:
        return AutomatedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutomatedWithStreamingResponse:
        return AutomatedWithStreamingResponse(self)

    def create(
        self,
        *,
        type: Literal["data_sync_all"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutomatedCreateResponse:
        """Enqueue an automated job.

        Currently, only the `data_sync_all` job type is
        supported, which will enqueue a job to re-sync all data for a connection.
        `data_sync_all` has a concurrency limit of 1 job at a time per connection. This
        means that if this endpoint is called while a job is already in progress for
        this connection, Finch will return the `job_id` of the job that is currently in
        progress. Finch allows a fixed window rate limit of 1 forced refresh per hour
        per connection.

        This endpoint is available for _Scale_ tier customers as an add-on. To request
        access to this endpoint, please contact your Finch account manager.

        Args:
          type: The type of job to start. Currently the only supported type is `data_sync_all`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/jobs/automated",
            body=maybe_transform({"type": type}, automated_create_params.AutomatedCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomatedCreateResponse,
        )

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
    ) -> AutomatedAsyncJob:
        """
        Get an automated job by `job_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/jobs/automated/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomatedAsyncJob,
        )

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
    ) -> SyncPage[AutomatedAsyncJob]:
        """Get all automated jobs.

        Automated jobs are completed by a machine. By default,
        jobs are sorted in descending order by submission time. For scheduled jobs such
        as data syncs, only the next scheduled job is shown.

        Args:
          limit: Number of items to return

          offset: Index to start from (defaults to 0)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/jobs/automated",
            page=SyncPage[AutomatedAsyncJob],
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
                    automated_list_params.AutomatedListParams,
                ),
            ),
            model=AutomatedAsyncJob,
        )


class AsyncAutomated(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutomatedWithRawResponse:
        return AsyncAutomatedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutomatedWithStreamingResponse:
        return AsyncAutomatedWithStreamingResponse(self)

    async def create(
        self,
        *,
        type: Literal["data_sync_all"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutomatedCreateResponse:
        """Enqueue an automated job.

        Currently, only the `data_sync_all` job type is
        supported, which will enqueue a job to re-sync all data for a connection.
        `data_sync_all` has a concurrency limit of 1 job at a time per connection. This
        means that if this endpoint is called while a job is already in progress for
        this connection, Finch will return the `job_id` of the job that is currently in
        progress. Finch allows a fixed window rate limit of 1 forced refresh per hour
        per connection.

        This endpoint is available for _Scale_ tier customers as an add-on. To request
        access to this endpoint, please contact your Finch account manager.

        Args:
          type: The type of job to start. Currently the only supported type is `data_sync_all`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/jobs/automated",
            body=await async_maybe_transform({"type": type}, automated_create_params.AutomatedCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomatedCreateResponse,
        )

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
    ) -> AutomatedAsyncJob:
        """
        Get an automated job by `job_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/jobs/automated/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomatedAsyncJob,
        )

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
    ) -> AsyncPaginator[AutomatedAsyncJob, AsyncPage[AutomatedAsyncJob]]:
        """Get all automated jobs.

        Automated jobs are completed by a machine. By default,
        jobs are sorted in descending order by submission time. For scheduled jobs such
        as data syncs, only the next scheduled job is shown.

        Args:
          limit: Number of items to return

          offset: Index to start from (defaults to 0)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/jobs/automated",
            page=AsyncPage[AutomatedAsyncJob],
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
                    automated_list_params.AutomatedListParams,
                ),
            ),
            model=AutomatedAsyncJob,
        )


class AutomatedWithRawResponse:
    def __init__(self, automated: Automated) -> None:
        self._automated = automated

        self.create = _legacy_response.to_raw_response_wrapper(
            automated.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            automated.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            automated.list,
        )


class AsyncAutomatedWithRawResponse:
    def __init__(self, automated: AsyncAutomated) -> None:
        self._automated = automated

        self.create = _legacy_response.async_to_raw_response_wrapper(
            automated.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            automated.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            automated.list,
        )


class AutomatedWithStreamingResponse:
    def __init__(self, automated: Automated) -> None:
        self._automated = automated

        self.create = to_streamed_response_wrapper(
            automated.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            automated.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            automated.list,
        )


class AsyncAutomatedWithStreamingResponse:
    def __init__(self, automated: AsyncAutomated) -> None:
        self._automated = automated

        self.create = async_to_streamed_response_wrapper(
            automated.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            automated.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            automated.list,
        )
