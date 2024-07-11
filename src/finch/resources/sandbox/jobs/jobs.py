# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .... import _legacy_response
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .configuration import (
    Configuration,
    AsyncConfiguration,
    ConfigurationWithRawResponse,
    AsyncConfigurationWithRawResponse,
    ConfigurationWithStreamingResponse,
    AsyncConfigurationWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.sandbox import job_create_params
from ....types.sandbox.job_create_response import JobCreateResponse

__all__ = ["Jobs", "AsyncJobs"]


class Jobs(SyncAPIResource):
    @cached_property
    def configuration(self) -> Configuration:
        return Configuration(self._client)

    @cached_property
    def with_raw_response(self) -> JobsWithRawResponse:
        return JobsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsWithStreamingResponse:
        return JobsWithStreamingResponse(self)

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
    ) -> JobCreateResponse:
        """Enqueue a new sandbox job

        Args:
          type: The type of job to start.

        Currently the only supported type is `data_sync_all`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sandbox/jobs",
            body=maybe_transform({"type": type}, job_create_params.JobCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobCreateResponse,
        )


class AsyncJobs(AsyncAPIResource):
    @cached_property
    def configuration(self) -> AsyncConfiguration:
        return AsyncConfiguration(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncJobsWithRawResponse:
        return AsyncJobsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsWithStreamingResponse:
        return AsyncJobsWithStreamingResponse(self)

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
    ) -> JobCreateResponse:
        """Enqueue a new sandbox job

        Args:
          type: The type of job to start.

        Currently the only supported type is `data_sync_all`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sandbox/jobs",
            body=await async_maybe_transform({"type": type}, job_create_params.JobCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobCreateResponse,
        )


class JobsWithRawResponse:
    def __init__(self, jobs: Jobs) -> None:
        self._jobs = jobs

        self.create = _legacy_response.to_raw_response_wrapper(
            jobs.create,
        )

    @cached_property
    def configuration(self) -> ConfigurationWithRawResponse:
        return ConfigurationWithRawResponse(self._jobs.configuration)


class AsyncJobsWithRawResponse:
    def __init__(self, jobs: AsyncJobs) -> None:
        self._jobs = jobs

        self.create = _legacy_response.async_to_raw_response_wrapper(
            jobs.create,
        )

    @cached_property
    def configuration(self) -> AsyncConfigurationWithRawResponse:
        return AsyncConfigurationWithRawResponse(self._jobs.configuration)


class JobsWithStreamingResponse:
    def __init__(self, jobs: Jobs) -> None:
        self._jobs = jobs

        self.create = to_streamed_response_wrapper(
            jobs.create,
        )

    @cached_property
    def configuration(self) -> ConfigurationWithStreamingResponse:
        return ConfigurationWithStreamingResponse(self._jobs.configuration)


class AsyncJobsWithStreamingResponse:
    def __init__(self, jobs: AsyncJobs) -> None:
        self._jobs = jobs

        self.create = async_to_streamed_response_wrapper(
            jobs.create,
        )

    @cached_property
    def configuration(self) -> AsyncConfigurationWithStreamingResponse:
        return AsyncConfigurationWithStreamingResponse(self._jobs.configuration)
