# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .jobs import (
    Jobs,
    AsyncJobs,
    JobsWithRawResponse,
    AsyncJobsWithRawResponse,
    JobsWithStreamingResponse,
    AsyncJobsWithStreamingResponse,
)
from .company import (
    Company,
    AsyncCompany,
    CompanyWithRawResponse,
    AsyncCompanyWithRawResponse,
    CompanyWithStreamingResponse,
    AsyncCompanyWithStreamingResponse,
)
from .payment import (
    Payment,
    AsyncPayment,
    PaymentWithRawResponse,
    AsyncPaymentWithRawResponse,
    PaymentWithStreamingResponse,
    AsyncPaymentWithStreamingResponse,
)
from ..._compat import cached_property
from .directory import (
    Directory,
    AsyncDirectory,
    DirectoryWithRawResponse,
    AsyncDirectoryWithRawResponse,
    DirectoryWithStreamingResponse,
    AsyncDirectoryWithStreamingResponse,
)
from .jobs.jobs import Jobs, AsyncJobs
from .employment import (
    Employment,
    AsyncEmployment,
    EmploymentWithRawResponse,
    AsyncEmploymentWithRawResponse,
    EmploymentWithStreamingResponse,
    AsyncEmploymentWithStreamingResponse,
)
from .individual import (
    Individual,
    AsyncIndividual,
    IndividualWithRawResponse,
    AsyncIndividualWithRawResponse,
    IndividualWithStreamingResponse,
    AsyncIndividualWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .connections import (
    Connections,
    AsyncConnections,
    ConnectionsWithRawResponse,
    AsyncConnectionsWithRawResponse,
    ConnectionsWithStreamingResponse,
    AsyncConnectionsWithStreamingResponse,
)
from .connections.connections import Connections, AsyncConnections

__all__ = ["Sandbox", "AsyncSandbox"]


class Sandbox(SyncAPIResource):
    @cached_property
    def connections(self) -> Connections:
        return Connections(self._client)

    @cached_property
    def company(self) -> Company:
        return Company(self._client)

    @cached_property
    def directory(self) -> Directory:
        return Directory(self._client)

    @cached_property
    def individual(self) -> Individual:
        return Individual(self._client)

    @cached_property
    def employment(self) -> Employment:
        return Employment(self._client)

    @cached_property
    def payment(self) -> Payment:
        return Payment(self._client)

    @cached_property
    def jobs(self) -> Jobs:
        return Jobs(self._client)

    @cached_property
    def with_raw_response(self) -> SandboxWithRawResponse:
        return SandboxWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SandboxWithStreamingResponse:
        return SandboxWithStreamingResponse(self)


class AsyncSandbox(AsyncAPIResource):
    @cached_property
    def connections(self) -> AsyncConnections:
        return AsyncConnections(self._client)

    @cached_property
    def company(self) -> AsyncCompany:
        return AsyncCompany(self._client)

    @cached_property
    def directory(self) -> AsyncDirectory:
        return AsyncDirectory(self._client)

    @cached_property
    def individual(self) -> AsyncIndividual:
        return AsyncIndividual(self._client)

    @cached_property
    def employment(self) -> AsyncEmployment:
        return AsyncEmployment(self._client)

    @cached_property
    def payment(self) -> AsyncPayment:
        return AsyncPayment(self._client)

    @cached_property
    def jobs(self) -> AsyncJobs:
        return AsyncJobs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSandboxWithRawResponse:
        return AsyncSandboxWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSandboxWithStreamingResponse:
        return AsyncSandboxWithStreamingResponse(self)


class SandboxWithRawResponse:
    def __init__(self, sandbox: Sandbox) -> None:
        self._sandbox = sandbox

    @cached_property
    def connections(self) -> ConnectionsWithRawResponse:
        return ConnectionsWithRawResponse(self._sandbox.connections)

    @cached_property
    def company(self) -> CompanyWithRawResponse:
        return CompanyWithRawResponse(self._sandbox.company)

    @cached_property
    def directory(self) -> DirectoryWithRawResponse:
        return DirectoryWithRawResponse(self._sandbox.directory)

    @cached_property
    def individual(self) -> IndividualWithRawResponse:
        return IndividualWithRawResponse(self._sandbox.individual)

    @cached_property
    def employment(self) -> EmploymentWithRawResponse:
        return EmploymentWithRawResponse(self._sandbox.employment)

    @cached_property
    def payment(self) -> PaymentWithRawResponse:
        return PaymentWithRawResponse(self._sandbox.payment)

    @cached_property
    def jobs(self) -> JobsWithRawResponse:
        return JobsWithRawResponse(self._sandbox.jobs)


class AsyncSandboxWithRawResponse:
    def __init__(self, sandbox: AsyncSandbox) -> None:
        self._sandbox = sandbox

    @cached_property
    def connections(self) -> AsyncConnectionsWithRawResponse:
        return AsyncConnectionsWithRawResponse(self._sandbox.connections)

    @cached_property
    def company(self) -> AsyncCompanyWithRawResponse:
        return AsyncCompanyWithRawResponse(self._sandbox.company)

    @cached_property
    def directory(self) -> AsyncDirectoryWithRawResponse:
        return AsyncDirectoryWithRawResponse(self._sandbox.directory)

    @cached_property
    def individual(self) -> AsyncIndividualWithRawResponse:
        return AsyncIndividualWithRawResponse(self._sandbox.individual)

    @cached_property
    def employment(self) -> AsyncEmploymentWithRawResponse:
        return AsyncEmploymentWithRawResponse(self._sandbox.employment)

    @cached_property
    def payment(self) -> AsyncPaymentWithRawResponse:
        return AsyncPaymentWithRawResponse(self._sandbox.payment)

    @cached_property
    def jobs(self) -> AsyncJobsWithRawResponse:
        return AsyncJobsWithRawResponse(self._sandbox.jobs)


class SandboxWithStreamingResponse:
    def __init__(self, sandbox: Sandbox) -> None:
        self._sandbox = sandbox

    @cached_property
    def connections(self) -> ConnectionsWithStreamingResponse:
        return ConnectionsWithStreamingResponse(self._sandbox.connections)

    @cached_property
    def company(self) -> CompanyWithStreamingResponse:
        return CompanyWithStreamingResponse(self._sandbox.company)

    @cached_property
    def directory(self) -> DirectoryWithStreamingResponse:
        return DirectoryWithStreamingResponse(self._sandbox.directory)

    @cached_property
    def individual(self) -> IndividualWithStreamingResponse:
        return IndividualWithStreamingResponse(self._sandbox.individual)

    @cached_property
    def employment(self) -> EmploymentWithStreamingResponse:
        return EmploymentWithStreamingResponse(self._sandbox.employment)

    @cached_property
    def payment(self) -> PaymentWithStreamingResponse:
        return PaymentWithStreamingResponse(self._sandbox.payment)

    @cached_property
    def jobs(self) -> JobsWithStreamingResponse:
        return JobsWithStreamingResponse(self._sandbox.jobs)


class AsyncSandboxWithStreamingResponse:
    def __init__(self, sandbox: AsyncSandbox) -> None:
        self._sandbox = sandbox

    @cached_property
    def connections(self) -> AsyncConnectionsWithStreamingResponse:
        return AsyncConnectionsWithStreamingResponse(self._sandbox.connections)

    @cached_property
    def company(self) -> AsyncCompanyWithStreamingResponse:
        return AsyncCompanyWithStreamingResponse(self._sandbox.company)

    @cached_property
    def directory(self) -> AsyncDirectoryWithStreamingResponse:
        return AsyncDirectoryWithStreamingResponse(self._sandbox.directory)

    @cached_property
    def individual(self) -> AsyncIndividualWithStreamingResponse:
        return AsyncIndividualWithStreamingResponse(self._sandbox.individual)

    @cached_property
    def employment(self) -> AsyncEmploymentWithStreamingResponse:
        return AsyncEmploymentWithStreamingResponse(self._sandbox.employment)

    @cached_property
    def payment(self) -> AsyncPaymentWithStreamingResponse:
        return AsyncPaymentWithStreamingResponse(self._sandbox.payment)

    @cached_property
    def jobs(self) -> AsyncJobsWithStreamingResponse:
        return AsyncJobsWithStreamingResponse(self._sandbox.jobs)
