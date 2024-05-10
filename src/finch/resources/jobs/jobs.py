# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .manual import (
    ManualResource,
    AsyncManualResource,
    ManualResourceWithRawResponse,
    AsyncManualResourceWithRawResponse,
    ManualResourceWithStreamingResponse,
    AsyncManualResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .automated import (
    AutomatedResource,
    AsyncAutomatedResource,
    AutomatedResourceWithRawResponse,
    AsyncAutomatedResourceWithRawResponse,
    AutomatedResourceWithStreamingResponse,
    AsyncAutomatedResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def automated(self) -> AutomatedResource:
        return AutomatedResource(self._client)

    @cached_property
    def manual(self) -> ManualResource:
        return ManualResource(self._client)

    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self)


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def automated(self) -> AsyncAutomatedResource:
        return AsyncAutomatedResource(self._client)

    @cached_property
    def manual(self) -> AsyncManualResource:
        return AsyncManualResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self)


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

    @cached_property
    def automated(self) -> AutomatedResourceWithRawResponse:
        return AutomatedResourceWithRawResponse(self._jobs.automated)

    @cached_property
    def manual(self) -> ManualResourceWithRawResponse:
        return ManualResourceWithRawResponse(self._jobs.manual)


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

    @cached_property
    def automated(self) -> AsyncAutomatedResourceWithRawResponse:
        return AsyncAutomatedResourceWithRawResponse(self._jobs.automated)

    @cached_property
    def manual(self) -> AsyncManualResourceWithRawResponse:
        return AsyncManualResourceWithRawResponse(self._jobs.manual)


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

    @cached_property
    def automated(self) -> AutomatedResourceWithStreamingResponse:
        return AutomatedResourceWithStreamingResponse(self._jobs.automated)

    @cached_property
    def manual(self) -> ManualResourceWithStreamingResponse:
        return ManualResourceWithStreamingResponse(self._jobs.manual)


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

    @cached_property
    def automated(self) -> AsyncAutomatedResourceWithStreamingResponse:
        return AsyncAutomatedResourceWithStreamingResponse(self._jobs.automated)

    @cached_property
    def manual(self) -> AsyncManualResourceWithStreamingResponse:
        return AsyncManualResourceWithStreamingResponse(self._jobs.manual)
