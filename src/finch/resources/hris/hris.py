# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
    BenefitsResource,
    AsyncBenefitsResource,
    BenefitsResourceWithRawResponse,
    AsyncBenefitsResourceWithRawResponse,
    BenefitsResourceWithStreamingResponse,
    AsyncBenefitsResourceWithStreamingResponse,
)
from .payments import (
    PaymentsResource,
    AsyncPaymentsResource,
    PaymentsResourceWithRawResponse,
    AsyncPaymentsResourceWithRawResponse,
    PaymentsResourceWithStreamingResponse,
    AsyncPaymentsResourceWithStreamingResponse,
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
from ..._resource import SyncAPIResource, AsyncAPIResource
from .employments import (
    EmploymentsResource,
    AsyncEmploymentsResource,
    EmploymentsResourceWithRawResponse,
    AsyncEmploymentsResourceWithRawResponse,
    EmploymentsResourceWithStreamingResponse,
    AsyncEmploymentsResourceWithStreamingResponse,
)
from .individuals import (
    IndividualsResource,
    AsyncIndividualsResource,
    IndividualsResourceWithRawResponse,
    AsyncIndividualsResourceWithRawResponse,
    IndividualsResourceWithStreamingResponse,
    AsyncIndividualsResourceWithStreamingResponse,
)
from .pay_statements import (
    PayStatementsResource,
    AsyncPayStatementsResource,
    PayStatementsResourceWithRawResponse,
    AsyncPayStatementsResourceWithRawResponse,
    PayStatementsResourceWithStreamingResponse,
    AsyncPayStatementsResourceWithStreamingResponse,
)
from .benefits.benefits import BenefitsResource, AsyncBenefitsResource

__all__ = ["HRISResource", "AsyncHRISResource"]


class HRISResource(SyncAPIResource):
    @cached_property
    def company(self) -> CompanyResource:
        return CompanyResource(self._client)

    @cached_property
    def directory(self) -> DirectoryResource:
        return DirectoryResource(self._client)

    @cached_property
    def individuals(self) -> IndividualsResource:
        return IndividualsResource(self._client)

    @cached_property
    def employments(self) -> EmploymentsResource:
        return EmploymentsResource(self._client)

    @cached_property
    def payments(self) -> PaymentsResource:
        return PaymentsResource(self._client)

    @cached_property
    def pay_statements(self) -> PayStatementsResource:
        return PayStatementsResource(self._client)

    @cached_property
    def benefits(self) -> BenefitsResource:
        return BenefitsResource(self._client)

    @cached_property
    def with_raw_response(self) -> HRISResourceWithRawResponse:
        return HRISResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HRISResourceWithStreamingResponse:
        return HRISResourceWithStreamingResponse(self)


class AsyncHRISResource(AsyncAPIResource):
    @cached_property
    def company(self) -> AsyncCompanyResource:
        return AsyncCompanyResource(self._client)

    @cached_property
    def directory(self) -> AsyncDirectoryResource:
        return AsyncDirectoryResource(self._client)

    @cached_property
    def individuals(self) -> AsyncIndividualsResource:
        return AsyncIndividualsResource(self._client)

    @cached_property
    def employments(self) -> AsyncEmploymentsResource:
        return AsyncEmploymentsResource(self._client)

    @cached_property
    def payments(self) -> AsyncPaymentsResource:
        return AsyncPaymentsResource(self._client)

    @cached_property
    def pay_statements(self) -> AsyncPayStatementsResource:
        return AsyncPayStatementsResource(self._client)

    @cached_property
    def benefits(self) -> AsyncBenefitsResource:
        return AsyncBenefitsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHRISResourceWithRawResponse:
        return AsyncHRISResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHRISResourceWithStreamingResponse:
        return AsyncHRISResourceWithStreamingResponse(self)


class HRISResourceWithRawResponse:
    def __init__(self, hris: HRISResource) -> None:
        self._hris = hris

    @cached_property
    def company(self) -> CompanyResourceWithRawResponse:
        return CompanyResourceWithRawResponse(self._hris.company)

    @cached_property
    def directory(self) -> DirectoryResourceWithRawResponse:
        return DirectoryResourceWithRawResponse(self._hris.directory)

    @cached_property
    def individuals(self) -> IndividualsResourceWithRawResponse:
        return IndividualsResourceWithRawResponse(self._hris.individuals)

    @cached_property
    def employments(self) -> EmploymentsResourceWithRawResponse:
        return EmploymentsResourceWithRawResponse(self._hris.employments)

    @cached_property
    def payments(self) -> PaymentsResourceWithRawResponse:
        return PaymentsResourceWithRawResponse(self._hris.payments)

    @cached_property
    def pay_statements(self) -> PayStatementsResourceWithRawResponse:
        return PayStatementsResourceWithRawResponse(self._hris.pay_statements)

    @cached_property
    def benefits(self) -> BenefitsResourceWithRawResponse:
        return BenefitsResourceWithRawResponse(self._hris.benefits)


class AsyncHRISResourceWithRawResponse:
    def __init__(self, hris: AsyncHRISResource) -> None:
        self._hris = hris

    @cached_property
    def company(self) -> AsyncCompanyResourceWithRawResponse:
        return AsyncCompanyResourceWithRawResponse(self._hris.company)

    @cached_property
    def directory(self) -> AsyncDirectoryResourceWithRawResponse:
        return AsyncDirectoryResourceWithRawResponse(self._hris.directory)

    @cached_property
    def individuals(self) -> AsyncIndividualsResourceWithRawResponse:
        return AsyncIndividualsResourceWithRawResponse(self._hris.individuals)

    @cached_property
    def employments(self) -> AsyncEmploymentsResourceWithRawResponse:
        return AsyncEmploymentsResourceWithRawResponse(self._hris.employments)

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithRawResponse:
        return AsyncPaymentsResourceWithRawResponse(self._hris.payments)

    @cached_property
    def pay_statements(self) -> AsyncPayStatementsResourceWithRawResponse:
        return AsyncPayStatementsResourceWithRawResponse(self._hris.pay_statements)

    @cached_property
    def benefits(self) -> AsyncBenefitsResourceWithRawResponse:
        return AsyncBenefitsResourceWithRawResponse(self._hris.benefits)


class HRISResourceWithStreamingResponse:
    def __init__(self, hris: HRISResource) -> None:
        self._hris = hris

    @cached_property
    def company(self) -> CompanyResourceWithStreamingResponse:
        return CompanyResourceWithStreamingResponse(self._hris.company)

    @cached_property
    def directory(self) -> DirectoryResourceWithStreamingResponse:
        return DirectoryResourceWithStreamingResponse(self._hris.directory)

    @cached_property
    def individuals(self) -> IndividualsResourceWithStreamingResponse:
        return IndividualsResourceWithStreamingResponse(self._hris.individuals)

    @cached_property
    def employments(self) -> EmploymentsResourceWithStreamingResponse:
        return EmploymentsResourceWithStreamingResponse(self._hris.employments)

    @cached_property
    def payments(self) -> PaymentsResourceWithStreamingResponse:
        return PaymentsResourceWithStreamingResponse(self._hris.payments)

    @cached_property
    def pay_statements(self) -> PayStatementsResourceWithStreamingResponse:
        return PayStatementsResourceWithStreamingResponse(self._hris.pay_statements)

    @cached_property
    def benefits(self) -> BenefitsResourceWithStreamingResponse:
        return BenefitsResourceWithStreamingResponse(self._hris.benefits)


class AsyncHRISResourceWithStreamingResponse:
    def __init__(self, hris: AsyncHRISResource) -> None:
        self._hris = hris

    @cached_property
    def company(self) -> AsyncCompanyResourceWithStreamingResponse:
        return AsyncCompanyResourceWithStreamingResponse(self._hris.company)

    @cached_property
    def directory(self) -> AsyncDirectoryResourceWithStreamingResponse:
        return AsyncDirectoryResourceWithStreamingResponse(self._hris.directory)

    @cached_property
    def individuals(self) -> AsyncIndividualsResourceWithStreamingResponse:
        return AsyncIndividualsResourceWithStreamingResponse(self._hris.individuals)

    @cached_property
    def employments(self) -> AsyncEmploymentsResourceWithStreamingResponse:
        return AsyncEmploymentsResourceWithStreamingResponse(self._hris.employments)

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithStreamingResponse:
        return AsyncPaymentsResourceWithStreamingResponse(self._hris.payments)

    @cached_property
    def pay_statements(self) -> AsyncPayStatementsResourceWithStreamingResponse:
        return AsyncPayStatementsResourceWithStreamingResponse(self._hris.pay_statements)

    @cached_property
    def benefits(self) -> AsyncBenefitsResourceWithStreamingResponse:
        return AsyncBenefitsResourceWithStreamingResponse(self._hris.benefits)
