# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .company import (
    CompanyResource,
    AsyncCompanyResource,
    CompanyResourceWithRawResponse,
    AsyncCompanyResourceWithRawResponse,
)
from .benefits import Benefits, AsyncBenefits, BenefitsWithRawResponse, AsyncBenefitsWithRawResponse
from .payments import Payments, AsyncPayments, PaymentsWithRawResponse, AsyncPaymentsWithRawResponse
from ..._compat import cached_property
from .directory import Directory, AsyncDirectory, DirectoryWithRawResponse, AsyncDirectoryWithRawResponse
from ..._resource import SyncAPIResource, AsyncAPIResource
from .employments import Employments, AsyncEmployments, EmploymentsWithRawResponse, AsyncEmploymentsWithRawResponse
from .individuals import Individuals, AsyncIndividuals, IndividualsWithRawResponse, AsyncIndividualsWithRawResponse
from .pay_statements import (
    PayStatements,
    AsyncPayStatements,
    PayStatementsWithRawResponse,
    AsyncPayStatementsWithRawResponse,
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


class HRISWithRawResponse:
    def __init__(self, hris: HRIS) -> None:
        self.company = CompanyResourceWithRawResponse(hris.company)
        self.directory = DirectoryWithRawResponse(hris.directory)
        self.individuals = IndividualsWithRawResponse(hris.individuals)
        self.employments = EmploymentsWithRawResponse(hris.employments)
        self.payments = PaymentsWithRawResponse(hris.payments)
        self.pay_statements = PayStatementsWithRawResponse(hris.pay_statements)
        self.benefits = BenefitsWithRawResponse(hris.benefits)


class AsyncHRISWithRawResponse:
    def __init__(self, hris: AsyncHRIS) -> None:
        self.company = AsyncCompanyResourceWithRawResponse(hris.company)
        self.directory = AsyncDirectoryWithRawResponse(hris.directory)
        self.individuals = AsyncIndividualsWithRawResponse(hris.individuals)
        self.employments = AsyncEmploymentsWithRawResponse(hris.employments)
        self.payments = AsyncPaymentsWithRawResponse(hris.payments)
        self.pay_statements = AsyncPayStatementsWithRawResponse(hris.pay_statements)
        self.benefits = AsyncBenefitsWithRawResponse(hris.benefits)
