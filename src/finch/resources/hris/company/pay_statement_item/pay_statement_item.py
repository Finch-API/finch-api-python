# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal

import httpx

from ..... import _legacy_response
from .rules import (
    Rules,
    AsyncRules,
    RulesWithRawResponse,
    AsyncRulesWithRawResponse,
    RulesWithStreamingResponse,
    AsyncRulesWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .....pagination import SyncResponsesPage, AsyncResponsesPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.hris.company import pay_statement_item_list_params
from .....types.hris.company.pay_statement_item_list_response import PayStatementItemListResponse

__all__ = ["PayStatementItem", "AsyncPayStatementItem"]


class PayStatementItem(SyncAPIResource):
    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def with_raw_response(self) -> PayStatementItemWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return PayStatementItemWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayStatementItemWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return PayStatementItemWithStreamingResponse(self)

    def list(
        self,
        *,
        categories: List[Literal["earnings", "taxes", "employee_deductions", "employer_contributions"]]
        | NotGiven = NOT_GIVEN,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncResponsesPage[PayStatementItemListResponse]:
        """
        **Beta:** this endpoint currently serves employers onboarded after March 4th and
        historical support will be added soon Retrieve a list of detailed pay statement
        items for the access token's connection account.

        Args:
          categories: Comma-delimited list of pay statement item categories to filter on. If empty,
              defaults to all categories.

          end_date: The end date to retrieve pay statement items by via their last seen pay date in
              `YYYY-MM-DD` format.

          name: Case-insensitive partial match search by pay statement item name.

          start_date: The start date to retrieve pay statement items by via their last seen pay date
              (inclusive) in `YYYY-MM-DD` format.

          type: String search by pay statement item type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/pay-statement-item",
            page=SyncResponsesPage[PayStatementItemListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "categories": categories,
                        "end_date": end_date,
                        "name": name,
                        "start_date": start_date,
                        "type": type,
                    },
                    pay_statement_item_list_params.PayStatementItemListParams,
                ),
            ),
            model=PayStatementItemListResponse,
        )


class AsyncPayStatementItem(AsyncAPIResource):
    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPayStatementItemWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPayStatementItemWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayStatementItemWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AsyncPayStatementItemWithStreamingResponse(self)

    def list(
        self,
        *,
        categories: List[Literal["earnings", "taxes", "employee_deductions", "employer_contributions"]]
        | NotGiven = NOT_GIVEN,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PayStatementItemListResponse, AsyncResponsesPage[PayStatementItemListResponse]]:
        """
        **Beta:** this endpoint currently serves employers onboarded after March 4th and
        historical support will be added soon Retrieve a list of detailed pay statement
        items for the access token's connection account.

        Args:
          categories: Comma-delimited list of pay statement item categories to filter on. If empty,
              defaults to all categories.

          end_date: The end date to retrieve pay statement items by via their last seen pay date in
              `YYYY-MM-DD` format.

          name: Case-insensitive partial match search by pay statement item name.

          start_date: The start date to retrieve pay statement items by via their last seen pay date
              (inclusive) in `YYYY-MM-DD` format.

          type: String search by pay statement item type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/pay-statement-item",
            page=AsyncResponsesPage[PayStatementItemListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "categories": categories,
                        "end_date": end_date,
                        "name": name,
                        "start_date": start_date,
                        "type": type,
                    },
                    pay_statement_item_list_params.PayStatementItemListParams,
                ),
            ),
            model=PayStatementItemListResponse,
        )


class PayStatementItemWithRawResponse:
    def __init__(self, pay_statement_item: PayStatementItem) -> None:
        self._pay_statement_item = pay_statement_item

        self.list = _legacy_response.to_raw_response_wrapper(
            pay_statement_item.list,
        )

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._pay_statement_item.rules)


class AsyncPayStatementItemWithRawResponse:
    def __init__(self, pay_statement_item: AsyncPayStatementItem) -> None:
        self._pay_statement_item = pay_statement_item

        self.list = _legacy_response.async_to_raw_response_wrapper(
            pay_statement_item.list,
        )

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._pay_statement_item.rules)


class PayStatementItemWithStreamingResponse:
    def __init__(self, pay_statement_item: PayStatementItem) -> None:
        self._pay_statement_item = pay_statement_item

        self.list = to_streamed_response_wrapper(
            pay_statement_item.list,
        )

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._pay_statement_item.rules)


class AsyncPayStatementItemWithStreamingResponse:
    def __init__(self, pay_statement_item: AsyncPayStatementItem) -> None:
        self._pay_statement_item = pay_statement_item

        self.list = async_to_streamed_response_wrapper(
            pay_statement_item.list,
        )

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._pay_statement_item.rules)
