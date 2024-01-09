# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .configuration import (
    Configuration,
    AsyncConfiguration,
    ConfigurationWithRawResponse,
    AsyncConfigurationWithRawResponse,
)

__all__ = ["Jobs", "AsyncJobs"]


class Jobs(SyncAPIResource):
    @cached_property
    def configuration(self) -> Configuration:
        return Configuration(self._client)

    @cached_property
    def with_raw_response(self) -> JobsWithRawResponse:
        return JobsWithRawResponse(self)


class AsyncJobs(AsyncAPIResource):
    @cached_property
    def configuration(self) -> AsyncConfiguration:
        return AsyncConfiguration(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncJobsWithRawResponse:
        return AsyncJobsWithRawResponse(self)


class JobsWithRawResponse:
    def __init__(self, jobs: Jobs) -> None:
        self.configuration = ConfigurationWithRawResponse(jobs.configuration)


class AsyncJobsWithRawResponse:
    def __init__(self, jobs: AsyncJobs) -> None:
        self.configuration = AsyncConfigurationWithRawResponse(jobs.configuration)
