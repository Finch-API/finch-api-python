# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .manual import (
    Manual,
    AsyncManual,
    ManualWithRawResponse,
    AsyncManualWithRawResponse,
    ManualWithStreamingResponse,
    AsyncManualWithStreamingResponse,
)
from ..._compat import cached_property
from .automated import (
    Automated,
    AsyncAutomated,
    AutomatedWithRawResponse,
    AsyncAutomatedWithRawResponse,
    AutomatedWithStreamingResponse,
    AsyncAutomatedWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Jobs", "AsyncJobs"]


class Jobs(SyncAPIResource):
    @cached_property
    def automated(self) -> Automated:
        return Automated(self._client)

    @cached_property
    def manual(self) -> Manual:
        return Manual(self._client)

    @cached_property
    def with_raw_response(self) -> JobsWithRawResponse:
        return JobsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsWithStreamingResponse:
        return JobsWithStreamingResponse(self)


class AsyncJobs(AsyncAPIResource):
    @cached_property
    def automated(self) -> AsyncAutomated:
        return AsyncAutomated(self._client)

    @cached_property
    def manual(self) -> AsyncManual:
        return AsyncManual(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncJobsWithRawResponse:
        return AsyncJobsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsWithStreamingResponse:
        return AsyncJobsWithStreamingResponse(self)


class JobsWithRawResponse:
    def __init__(self, jobs: Jobs) -> None:
        self.automated = AutomatedWithRawResponse(jobs.automated)
        self.manual = ManualWithRawResponse(jobs.manual)


class AsyncJobsWithRawResponse:
    def __init__(self, jobs: AsyncJobs) -> None:
        self.automated = AsyncAutomatedWithRawResponse(jobs.automated)
        self.manual = AsyncManualWithRawResponse(jobs.manual)


class JobsWithStreamingResponse:
    def __init__(self, jobs: Jobs) -> None:
        self.automated = AutomatedWithStreamingResponse(jobs.automated)
        self.manual = ManualWithStreamingResponse(jobs.manual)


class AsyncJobsWithStreamingResponse:
    def __init__(self, jobs: AsyncJobs) -> None:
        self.automated = AsyncAutomatedWithStreamingResponse(jobs.automated)
        self.manual = AsyncManualWithStreamingResponse(jobs.manual)
