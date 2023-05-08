# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .company import CompanyResource, AsyncCompanyResource
from .benefits import Benefits, AsyncBenefits
from .payments import Payments, AsyncPayments
from .directory import Directory, AsyncDirectory
from ..._resource import SyncAPIResource, AsyncAPIResource
from .individuals import Individuals, AsyncIndividuals
from .pay_statements import PayStatements, AsyncPayStatements

if TYPE_CHECKING:
    from ..._client import Finch, AsyncFinch

__all__ = ["HRIS", "AsyncHRIS"]


class HRIS(SyncAPIResource):
    company: CompanyResource
    payments: Payments
    pay_statements: PayStatements
    directory: Directory
    individuals: Individuals
    benefits: Benefits

    def __init__(self, client: Finch) -> None:
        super().__init__(client)
        self.company = CompanyResource(client)
        self.payments = Payments(client)
        self.pay_statements = PayStatements(client)
        self.directory = Directory(client)
        self.individuals = Individuals(client)
        self.benefits = Benefits(client)


class AsyncHRIS(AsyncAPIResource):
    company: AsyncCompanyResource
    payments: AsyncPayments
    pay_statements: AsyncPayStatements
    directory: AsyncDirectory
    individuals: AsyncIndividuals
    benefits: AsyncBenefits

    def __init__(self, client: AsyncFinch) -> None:
        super().__init__(client)
        self.company = AsyncCompanyResource(client)
        self.payments = AsyncPayments(client)
        self.pay_statements = AsyncPayStatements(client)
        self.directory = AsyncDirectory(client)
        self.individuals = AsyncIndividuals(client)
        self.benefits = AsyncBenefits(client)
