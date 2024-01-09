# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .jobs import Jobs, AsyncJobs, JobsWithRawResponse, AsyncJobsWithRawResponse
from .company import Company, AsyncCompany, CompanyWithRawResponse, AsyncCompanyWithRawResponse
from .payment import Payment, AsyncPayment, PaymentWithRawResponse, AsyncPaymentWithRawResponse
from ..._compat import cached_property
from .directory import Directory, AsyncDirectory, DirectoryWithRawResponse, AsyncDirectoryWithRawResponse
from .jobs.jobs import Jobs, AsyncJobs
from .employment import Employment, AsyncEmployment, EmploymentWithRawResponse, AsyncEmploymentWithRawResponse
from .individual import Individual, AsyncIndividual, IndividualWithRawResponse, AsyncIndividualWithRawResponse
from ..._resource import SyncAPIResource, AsyncAPIResource
from .connections import Connections, AsyncConnections, ConnectionsWithRawResponse, AsyncConnectionsWithRawResponse
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


class SandboxWithRawResponse:
    def __init__(self, sandbox: Sandbox) -> None:
        self.connections = ConnectionsWithRawResponse(sandbox.connections)
        self.company = CompanyWithRawResponse(sandbox.company)
        self.directory = DirectoryWithRawResponse(sandbox.directory)
        self.individual = IndividualWithRawResponse(sandbox.individual)
        self.employment = EmploymentWithRawResponse(sandbox.employment)
        self.payment = PaymentWithRawResponse(sandbox.payment)
        self.jobs = JobsWithRawResponse(sandbox.jobs)


class AsyncSandboxWithRawResponse:
    def __init__(self, sandbox: AsyncSandbox) -> None:
        self.connections = AsyncConnectionsWithRawResponse(sandbox.connections)
        self.company = AsyncCompanyWithRawResponse(sandbox.company)
        self.directory = AsyncDirectoryWithRawResponse(sandbox.directory)
        self.individual = AsyncIndividualWithRawResponse(sandbox.individual)
        self.employment = AsyncEmploymentWithRawResponse(sandbox.employment)
        self.payment = AsyncPaymentWithRawResponse(sandbox.payment)
        self.jobs = AsyncJobsWithRawResponse(sandbox.jobs)
