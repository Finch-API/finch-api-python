# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .company import (
    CompanyResource,
    AsyncCompanyResource,
    CompanyResourceWithRawResponse,
    AsyncCompanyResourceWithRawResponse,
)
from .benefits import (
    Benefits,
    AsyncBenefits,
    BenefitsWithRawResponse,
    AsyncBenefitsWithRawResponse,
)
from .payments import (
    Payments,
    AsyncPayments,
    PaymentsWithRawResponse,
    AsyncPaymentsWithRawResponse,
)
from .directory import (
    Directory,
    AsyncDirectory,
    DirectoryWithRawResponse,
    AsyncDirectoryWithRawResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .employments import (
    Employments,
    AsyncEmployments,
    EmploymentsWithRawResponse,
    AsyncEmploymentsWithRawResponse,
)
from .individuals import (
    Individuals,
    AsyncIndividuals,
    IndividualsWithRawResponse,
    AsyncIndividualsWithRawResponse,
)
from .pay_statements import (
    PayStatements,
    AsyncPayStatements,
    PayStatementsWithRawResponse,
    AsyncPayStatementsWithRawResponse,
)

if TYPE_CHECKING:
    from ..._client import Finch, AsyncFinch

__all__ = ["HRIS", "AsyncHRIS"]


class HRIS(SyncAPIResource):
    company: CompanyResource
    directory: Directory
    individuals: Individuals
    employments: Employments
    payments: Payments
    pay_statements: PayStatements
    benefits: Benefits
    with_raw_response: HRISWithRawResponse

    def __init__(self, client: Finch) -> None:
        super().__init__(client)
        self.company = CompanyResource(client)
        self.directory = Directory(client)
        self.individuals = Individuals(client)
        self.employments = Employments(client)
        self.payments = Payments(client)
        self.pay_statements = PayStatements(client)
        self.benefits = Benefits(client)
        self.with_raw_response = HRISWithRawResponse(self)


class AsyncHRIS(AsyncAPIResource):
    company: AsyncCompanyResource
    directory: AsyncDirectory
    individuals: AsyncIndividuals
    employments: AsyncEmployments
    payments: AsyncPayments
    pay_statements: AsyncPayStatements
    benefits: AsyncBenefits
    with_raw_response: AsyncHRISWithRawResponse

    def __init__(self, client: AsyncFinch) -> None:
        super().__init__(client)
        self.company = AsyncCompanyResource(client)
        self.directory = AsyncDirectory(client)
        self.individuals = AsyncIndividuals(client)
        self.employments = AsyncEmployments(client)
        self.payments = AsyncPayments(client)
        self.pay_statements = AsyncPayStatements(client)
        self.benefits = AsyncBenefits(client)
        self.with_raw_response = AsyncHRISWithRawResponse(self)


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
