# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .configuration import (
    Configuration,
    AsyncConfiguration,
    ConfigurationWithRawResponse,
    AsyncConfigurationWithRawResponse,
    ConfigurationWithStreamingResponse,
    AsyncConfigurationWithStreamingResponse,
)

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


class JobsWithRawResponse:
    def __init__(self, jobs: Jobs) -> None:
        self._jobs = jobs

    @cached_property
    def configuration(self) -> ConfigurationWithRawResponse:
        return ConfigurationWithRawResponse(self._jobs.configuration)


class AsyncJobsWithRawResponse:
    def __init__(self, jobs: AsyncJobs) -> None:
        self._jobs = jobs

    @cached_property
    def configuration(self) -> AsyncConfigurationWithRawResponse:
        return AsyncConfigurationWithRawResponse(self._jobs.configuration)


class JobsWithStreamingResponse:
    def __init__(self, jobs: Jobs) -> None:
        self._jobs = jobs

    @cached_property
    def configuration(self) -> ConfigurationWithStreamingResponse:
        return ConfigurationWithStreamingResponse(self._jobs.configuration)


class AsyncJobsWithStreamingResponse:
    def __init__(self, jobs: AsyncJobs) -> None:
        self._jobs = jobs

    @cached_property
    def configuration(self) -> AsyncConfigurationWithStreamingResponse:
        return AsyncConfigurationWithStreamingResponse(self._jobs.configuration)
