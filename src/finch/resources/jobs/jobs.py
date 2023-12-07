# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .manual import (
    Manual,
    AsyncManual,
    ManualWithRawResponse,
    AsyncManualWithRawResponse,
)
from .automated import (
    Automated,
    AsyncAutomated,
    AutomatedWithRawResponse,
    AsyncAutomatedWithRawResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ..._client import Finch, AsyncFinch

__all__ = ["Jobs", "AsyncJobs"]


class Jobs(SyncAPIResource):
    automated: Automated
    manual: Manual
    with_raw_response: JobsWithRawResponse

    def __init__(self, client: Finch) -> None:
        super().__init__(client)
        self.automated = Automated(client)
        self.manual = Manual(client)
        self.with_raw_response = JobsWithRawResponse(self)


class AsyncJobs(AsyncAPIResource):
    automated: AsyncAutomated
    manual: AsyncManual
    with_raw_response: AsyncJobsWithRawResponse

    def __init__(self, client: AsyncFinch) -> None:
        super().__init__(client)
        self.automated = AsyncAutomated(client)
        self.manual = AsyncManual(client)
        self.with_raw_response = AsyncJobsWithRawResponse(self)


class JobsWithRawResponse:
    def __init__(self, jobs: Jobs) -> None:
        self.automated = AutomatedWithRawResponse(jobs.automated)
        self.manual = ManualWithRawResponse(jobs.manual)


class AsyncJobsWithRawResponse:
    def __init__(self, jobs: AsyncJobs) -> None:
        self.automated = AsyncAutomatedWithRawResponse(jobs.automated)
        self.manual = AsyncManualWithRawResponse(jobs.manual)
