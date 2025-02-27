# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .pay_groups import (
    PayGroups,
    AsyncPayGroups,
    PayGroupsWithRawResponse,
    AsyncPayGroupsWithRawResponse,
    PayGroupsWithStreamingResponse,
    AsyncPayGroupsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Payroll", "AsyncPayroll"]


class Payroll(SyncAPIResource):
    @cached_property
    def pay_groups(self) -> PayGroups:
        return PayGroups(self._client)

    @cached_property
    def with_raw_response(self) -> PayrollWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return PayrollWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayrollWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return PayrollWithStreamingResponse(self)


class AsyncPayroll(AsyncAPIResource):
    @cached_property
    def pay_groups(self) -> AsyncPayGroups:
        return AsyncPayGroups(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPayrollWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPayrollWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayrollWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AsyncPayrollWithStreamingResponse(self)


class PayrollWithRawResponse:
    def __init__(self, payroll: Payroll) -> None:
        self._payroll = payroll

    @cached_property
    def pay_groups(self) -> PayGroupsWithRawResponse:
        return PayGroupsWithRawResponse(self._payroll.pay_groups)


class AsyncPayrollWithRawResponse:
    def __init__(self, payroll: AsyncPayroll) -> None:
        self._payroll = payroll

    @cached_property
    def pay_groups(self) -> AsyncPayGroupsWithRawResponse:
        return AsyncPayGroupsWithRawResponse(self._payroll.pay_groups)


class PayrollWithStreamingResponse:
    def __init__(self, payroll: Payroll) -> None:
        self._payroll = payroll

    @cached_property
    def pay_groups(self) -> PayGroupsWithStreamingResponse:
        return PayGroupsWithStreamingResponse(self._payroll.pay_groups)


class AsyncPayrollWithStreamingResponse:
    def __init__(self, payroll: AsyncPayroll) -> None:
        self._payroll = payroll

    @cached_property
    def pay_groups(self) -> AsyncPayGroupsWithStreamingResponse:
        return AsyncPayGroupsWithStreamingResponse(self._payroll.pay_groups)
