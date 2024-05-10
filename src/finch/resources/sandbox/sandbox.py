# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from .company import (
    CompanyResource,
    AsyncCompanyResource,
    CompanyResourceWithRawResponse,
    AsyncCompanyResourceWithRawResponse,
    CompanyResourceWithStreamingResponse,
    AsyncCompanyResourceWithStreamingResponse,
)
from .payment import (
    PaymentResource,
    AsyncPaymentResource,
    PaymentResourceWithRawResponse,
    AsyncPaymentResourceWithRawResponse,
    PaymentResourceWithStreamingResponse,
    AsyncPaymentResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .directory import (
    DirectoryResource,
    AsyncDirectoryResource,
    DirectoryResourceWithRawResponse,
    AsyncDirectoryResourceWithRawResponse,
    DirectoryResourceWithStreamingResponse,
    AsyncDirectoryResourceWithStreamingResponse,
)
from .jobs.jobs import JobsResource, AsyncJobsResource
from .employment import (
    EmploymentResource,
    AsyncEmploymentResource,
    EmploymentResourceWithRawResponse,
    AsyncEmploymentResourceWithRawResponse,
    EmploymentResourceWithStreamingResponse,
    AsyncEmploymentResourceWithStreamingResponse,
)
from .individual import (
    IndividualResource,
    AsyncIndividualResource,
    IndividualResourceWithRawResponse,
    AsyncIndividualResourceWithRawResponse,
    IndividualResourceWithStreamingResponse,
    AsyncIndividualResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .connections import (
    ConnectionsResource,
    AsyncConnectionsResource,
    ConnectionsResourceWithRawResponse,
    AsyncConnectionsResourceWithRawResponse,
    ConnectionsResourceWithStreamingResponse,
    AsyncConnectionsResourceWithStreamingResponse,
)
from .connections.connections import ConnectionsResource, AsyncConnectionsResource

__all__ = ["SandboxResource", "AsyncSandboxResource"]


class SandboxResource(SyncAPIResource):
    @cached_property
    def connections(self) -> ConnectionsResource:
        return ConnectionsResource(self._client)

    @cached_property
    def company(self) -> CompanyResource:
        return CompanyResource(self._client)

    @cached_property
    def directory(self) -> DirectoryResource:
        return DirectoryResource(self._client)

    @cached_property
    def individual(self) -> IndividualResource:
        return IndividualResource(self._client)

    @cached_property
    def employment(self) -> EmploymentResource:
        return EmploymentResource(self._client)

    @cached_property
    def payment(self) -> PaymentResource:
        return PaymentResource(self._client)

    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SandboxResourceWithRawResponse:
        return SandboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SandboxResourceWithStreamingResponse:
        return SandboxResourceWithStreamingResponse(self)


class AsyncSandboxResource(AsyncAPIResource):
    @cached_property
    def connections(self) -> AsyncConnectionsResource:
        return AsyncConnectionsResource(self._client)

    @cached_property
    def company(self) -> AsyncCompanyResource:
        return AsyncCompanyResource(self._client)

    @cached_property
    def directory(self) -> AsyncDirectoryResource:
        return AsyncDirectoryResource(self._client)

    @cached_property
    def individual(self) -> AsyncIndividualResource:
        return AsyncIndividualResource(self._client)

    @cached_property
    def employment(self) -> AsyncEmploymentResource:
        return AsyncEmploymentResource(self._client)

    @cached_property
    def payment(self) -> AsyncPaymentResource:
        return AsyncPaymentResource(self._client)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSandboxResourceWithRawResponse:
        return AsyncSandboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSandboxResourceWithStreamingResponse:
        return AsyncSandboxResourceWithStreamingResponse(self)


class SandboxResourceWithRawResponse:
    def __init__(self, sandbox: SandboxResource) -> None:
        self._sandbox = sandbox

    @cached_property
    def connections(self) -> ConnectionsResourceWithRawResponse:
        return ConnectionsResourceWithRawResponse(self._sandbox.connections)

    @cached_property
    def company(self) -> CompanyResourceWithRawResponse:
        return CompanyResourceWithRawResponse(self._sandbox.company)

    @cached_property
    def directory(self) -> DirectoryResourceWithRawResponse:
        return DirectoryResourceWithRawResponse(self._sandbox.directory)

    @cached_property
    def individual(self) -> IndividualResourceWithRawResponse:
        return IndividualResourceWithRawResponse(self._sandbox.individual)

    @cached_property
    def employment(self) -> EmploymentResourceWithRawResponse:
        return EmploymentResourceWithRawResponse(self._sandbox.employment)

    @cached_property
    def payment(self) -> PaymentResourceWithRawResponse:
        return PaymentResourceWithRawResponse(self._sandbox.payment)

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._sandbox.jobs)


class AsyncSandboxResourceWithRawResponse:
    def __init__(self, sandbox: AsyncSandboxResource) -> None:
        self._sandbox = sandbox

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithRawResponse:
        return AsyncConnectionsResourceWithRawResponse(self._sandbox.connections)

    @cached_property
    def company(self) -> AsyncCompanyResourceWithRawResponse:
        return AsyncCompanyResourceWithRawResponse(self._sandbox.company)

    @cached_property
    def directory(self) -> AsyncDirectoryResourceWithRawResponse:
        return AsyncDirectoryResourceWithRawResponse(self._sandbox.directory)

    @cached_property
    def individual(self) -> AsyncIndividualResourceWithRawResponse:
        return AsyncIndividualResourceWithRawResponse(self._sandbox.individual)

    @cached_property
    def employment(self) -> AsyncEmploymentResourceWithRawResponse:
        return AsyncEmploymentResourceWithRawResponse(self._sandbox.employment)

    @cached_property
    def payment(self) -> AsyncPaymentResourceWithRawResponse:
        return AsyncPaymentResourceWithRawResponse(self._sandbox.payment)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._sandbox.jobs)


class SandboxResourceWithStreamingResponse:
    def __init__(self, sandbox: SandboxResource) -> None:
        self._sandbox = sandbox

    @cached_property
    def connections(self) -> ConnectionsResourceWithStreamingResponse:
        return ConnectionsResourceWithStreamingResponse(self._sandbox.connections)

    @cached_property
    def company(self) -> CompanyResourceWithStreamingResponse:
        return CompanyResourceWithStreamingResponse(self._sandbox.company)

    @cached_property
    def directory(self) -> DirectoryResourceWithStreamingResponse:
        return DirectoryResourceWithStreamingResponse(self._sandbox.directory)

    @cached_property
    def individual(self) -> IndividualResourceWithStreamingResponse:
        return IndividualResourceWithStreamingResponse(self._sandbox.individual)

    @cached_property
    def employment(self) -> EmploymentResourceWithStreamingResponse:
        return EmploymentResourceWithStreamingResponse(self._sandbox.employment)

    @cached_property
    def payment(self) -> PaymentResourceWithStreamingResponse:
        return PaymentResourceWithStreamingResponse(self._sandbox.payment)

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._sandbox.jobs)


class AsyncSandboxResourceWithStreamingResponse:
    def __init__(self, sandbox: AsyncSandboxResource) -> None:
        self._sandbox = sandbox

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithStreamingResponse:
        return AsyncConnectionsResourceWithStreamingResponse(self._sandbox.connections)

    @cached_property
    def company(self) -> AsyncCompanyResourceWithStreamingResponse:
        return AsyncCompanyResourceWithStreamingResponse(self._sandbox.company)

    @cached_property
    def directory(self) -> AsyncDirectoryResourceWithStreamingResponse:
        return AsyncDirectoryResourceWithStreamingResponse(self._sandbox.directory)

    @cached_property
    def individual(self) -> AsyncIndividualResourceWithStreamingResponse:
        return AsyncIndividualResourceWithStreamingResponse(self._sandbox.individual)

    @cached_property
    def employment(self) -> AsyncEmploymentResourceWithStreamingResponse:
        return AsyncEmploymentResourceWithStreamingResponse(self._sandbox.employment)

    @cached_property
    def payment(self) -> AsyncPaymentResourceWithStreamingResponse:
        return AsyncPaymentResourceWithStreamingResponse(self._sandbox.payment)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._sandbox.jobs)
