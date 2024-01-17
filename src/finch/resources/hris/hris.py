# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .company import (
    CompanyResource,
    AsyncCompanyResource,
    CompanyResourceWithRawResponse,
    AsyncCompanyResourceWithRawResponse,
    CompanyResourceWithStreamingResponse,
    AsyncCompanyResourceWithStreamingResponse,
)
from .benefits import (
    Benefits,
    AsyncBenefits,
    BenefitsWithRawResponse,
    AsyncBenefitsWithRawResponse,
    BenefitsWithStreamingResponse,
    AsyncBenefitsWithStreamingResponse,
)
from .payments import (
    Payments,
    AsyncPayments,
    PaymentsWithRawResponse,
    AsyncPaymentsWithRawResponse,
    PaymentsWithStreamingResponse,
    AsyncPaymentsWithStreamingResponse,
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
from ..._resource import SyncAPIResource, AsyncAPIResource
from .employments import (
    Employments,
    AsyncEmployments,
    EmploymentsWithRawResponse,
    AsyncEmploymentsWithRawResponse,
    EmploymentsWithStreamingResponse,
    AsyncEmploymentsWithStreamingResponse,
)
from .individuals import (
    Individuals,
    AsyncIndividuals,
    IndividualsWithRawResponse,
    AsyncIndividualsWithRawResponse,
    IndividualsWithStreamingResponse,
    AsyncIndividualsWithStreamingResponse,
)
from .pay_statements import (
    PayStatements,
    AsyncPayStatements,
    PayStatementsWithRawResponse,
    AsyncPayStatementsWithRawResponse,
    PayStatementsWithStreamingResponse,
    AsyncPayStatementsWithStreamingResponse,
)
from .benefits.benefits import Benefits, AsyncBenefits

__all__ = ["HRIS", "AsyncHRIS"]


class HRIS(SyncAPIResource):
    @cached_property
    def company(self) -> CompanyResource:
        return CompanyResource(self._client)

    @cached_property
    def directory(self) -> Directory:
        return Directory(self._client)

    @cached_property
    def individuals(self) -> Individuals:
        return Individuals(self._client)

    @cached_property
    def employments(self) -> Employments:
        return Employments(self._client)

    @cached_property
    def payments(self) -> Payments:
        return Payments(self._client)

    @cached_property
    def pay_statements(self) -> PayStatements:
        return PayStatements(self._client)

    @cached_property
    def benefits(self) -> Benefits:
        return Benefits(self._client)

    @cached_property
    def with_raw_response(self) -> HRISWithRawResponse:
        return HRISWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HRISWithStreamingResponse:
        return HRISWithStreamingResponse(self)


class AsyncHRIS(AsyncAPIResource):
    @cached_property
    def company(self) -> AsyncCompanyResource:
        return AsyncCompanyResource(self._client)

    @cached_property
    def directory(self) -> AsyncDirectory:
        return AsyncDirectory(self._client)

    @cached_property
    def individuals(self) -> AsyncIndividuals:
        return AsyncIndividuals(self._client)

    @cached_property
    def employments(self) -> AsyncEmployments:
        return AsyncEmployments(self._client)

    @cached_property
    def payments(self) -> AsyncPayments:
        return AsyncPayments(self._client)

    @cached_property
    def pay_statements(self) -> AsyncPayStatements:
        return AsyncPayStatements(self._client)

    @cached_property
    def benefits(self) -> AsyncBenefits:
        return AsyncBenefits(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHRISWithRawResponse:
        return AsyncHRISWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHRISWithStreamingResponse:
        return AsyncHRISWithStreamingResponse(self)


class HRISWithRawResponse:
    def __init__(self, hris: HRIS) -> None:
        self._hris = hris

    @cached_property
    def company(self) -> CompanyResourceWithRawResponse:
        return CompanyResourceWithRawResponse(self._hris.company)

    @cached_property
    def directory(self) -> DirectoryWithRawResponse:
        return DirectoryWithRawResponse(self._hris.directory)

    @cached_property
    def individuals(self) -> IndividualsWithRawResponse:
        return IndividualsWithRawResponse(self._hris.individuals)

    @cached_property
    def employments(self) -> EmploymentsWithRawResponse:
        return EmploymentsWithRawResponse(self._hris.employments)

    @cached_property
    def payments(self) -> PaymentsWithRawResponse:
        return PaymentsWithRawResponse(self._hris.payments)

    @cached_property
    def pay_statements(self) -> PayStatementsWithRawResponse:
        return PayStatementsWithRawResponse(self._hris.pay_statements)

    @cached_property
    def benefits(self) -> BenefitsWithRawResponse:
        return BenefitsWithRawResponse(self._hris.benefits)


class AsyncHRISWithRawResponse:
    def __init__(self, hris: AsyncHRIS) -> None:
        self._hris = hris

    @cached_property
    def company(self) -> AsyncCompanyResourceWithRawResponse:
        return AsyncCompanyResourceWithRawResponse(self._hris.company)

    @cached_property
    def directory(self) -> AsyncDirectoryWithRawResponse:
        return AsyncDirectoryWithRawResponse(self._hris.directory)

    @cached_property
    def individuals(self) -> AsyncIndividualsWithRawResponse:
        return AsyncIndividualsWithRawResponse(self._hris.individuals)

    @cached_property
    def employments(self) -> AsyncEmploymentsWithRawResponse:
        return AsyncEmploymentsWithRawResponse(self._hris.employments)

    @cached_property
    def payments(self) -> AsyncPaymentsWithRawResponse:
        return AsyncPaymentsWithRawResponse(self._hris.payments)

    @cached_property
    def pay_statements(self) -> AsyncPayStatementsWithRawResponse:
        return AsyncPayStatementsWithRawResponse(self._hris.pay_statements)

    @cached_property
    def benefits(self) -> AsyncBenefitsWithRawResponse:
        return AsyncBenefitsWithRawResponse(self._hris.benefits)


class HRISWithStreamingResponse:
    def __init__(self, hris: HRIS) -> None:
        self._hris = hris

    @cached_property
    def company(self) -> CompanyResourceWithStreamingResponse:
        return CompanyResourceWithStreamingResponse(self._hris.company)

    @cached_property
    def directory(self) -> DirectoryWithStreamingResponse:
        return DirectoryWithStreamingResponse(self._hris.directory)

    @cached_property
    def individuals(self) -> IndividualsWithStreamingResponse:
        return IndividualsWithStreamingResponse(self._hris.individuals)

    @cached_property
    def employments(self) -> EmploymentsWithStreamingResponse:
        return EmploymentsWithStreamingResponse(self._hris.employments)

    @cached_property
    def payments(self) -> PaymentsWithStreamingResponse:
        return PaymentsWithStreamingResponse(self._hris.payments)

    @cached_property
    def pay_statements(self) -> PayStatementsWithStreamingResponse:
        return PayStatementsWithStreamingResponse(self._hris.pay_statements)

    @cached_property
    def benefits(self) -> BenefitsWithStreamingResponse:
        return BenefitsWithStreamingResponse(self._hris.benefits)


class AsyncHRISWithStreamingResponse:
    def __init__(self, hris: AsyncHRIS) -> None:
        self._hris = hris

    @cached_property
    def company(self) -> AsyncCompanyResourceWithStreamingResponse:
        return AsyncCompanyResourceWithStreamingResponse(self._hris.company)

    @cached_property
    def directory(self) -> AsyncDirectoryWithStreamingResponse:
        return AsyncDirectoryWithStreamingResponse(self._hris.directory)

    @cached_property
    def individuals(self) -> AsyncIndividualsWithStreamingResponse:
        return AsyncIndividualsWithStreamingResponse(self._hris.individuals)

    @cached_property
    def employments(self) -> AsyncEmploymentsWithStreamingResponse:
        return AsyncEmploymentsWithStreamingResponse(self._hris.employments)

    @cached_property
    def payments(self) -> AsyncPaymentsWithStreamingResponse:
        return AsyncPaymentsWithStreamingResponse(self._hris.payments)

    @cached_property
    def pay_statements(self) -> AsyncPayStatementsWithStreamingResponse:
        return AsyncPayStatementsWithStreamingResponse(self._hris.pay_statements)

    @cached_property
    def benefits(self) -> AsyncBenefitsWithStreamingResponse:
        return AsyncBenefitsWithStreamingResponse(self._hris.benefits)
