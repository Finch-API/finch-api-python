# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return JobsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AsyncJobsWithStreamingResponse(self)


class JobsWithRawResponse:
    def __init__(self, jobs: Jobs) -> None:
        self._jobs = jobs

    @cached_property
    def automated(self) -> AutomatedWithRawResponse:
        return AutomatedWithRawResponse(self._jobs.automated)

    @cached_property
    def manual(self) -> ManualWithRawResponse:
        return ManualWithRawResponse(self._jobs.manual)


class AsyncJobsWithRawResponse:
    def __init__(self, jobs: AsyncJobs) -> None:
        self._jobs = jobs

    @cached_property
    def automated(self) -> AsyncAutomatedWithRawResponse:
        return AsyncAutomatedWithRawResponse(self._jobs.automated)

    @cached_property
    def manual(self) -> AsyncManualWithRawResponse:
        return AsyncManualWithRawResponse(self._jobs.manual)


class JobsWithStreamingResponse:
    def __init__(self, jobs: Jobs) -> None:
        self._jobs = jobs

    @cached_property
    def automated(self) -> AutomatedWithStreamingResponse:
        return AutomatedWithStreamingResponse(self._jobs.automated)

    @cached_property
    def manual(self) -> ManualWithStreamingResponse:
        return ManualWithStreamingResponse(self._jobs.manual)


class AsyncJobsWithStreamingResponse:
    def __init__(self, jobs: AsyncJobs) -> None:
        self._jobs = jobs

    @cached_property
    def automated(self) -> AsyncAutomatedWithStreamingResponse:
        return AsyncAutomatedWithStreamingResponse(self._jobs.automated)

    @cached_property
    def manual(self) -> AsyncManualWithStreamingResponse:
        return AsyncManualWithStreamingResponse(self._jobs.manual)
