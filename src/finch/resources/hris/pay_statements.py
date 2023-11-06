# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncResponsesPage, AsyncResponsesPage
from ...types.hris import PayStatementResponse, pay_statement_retrieve_many_params
from ..._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ..._client import Finch, AsyncFinch

__all__ = ["PayStatements", "AsyncPayStatements"]


class PayStatements(SyncAPIResource):
    with_raw_response: PayStatementsWithRawResponse

    def __init__(self, client: Finch) -> None:
        super().__init__(client)
        self.with_raw_response = PayStatementsWithRawResponse(self)

    def retrieve_many(
        self,
        *,
        requests: List[pay_statement_retrieve_many_params.Request],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncResponsesPage[PayStatementResponse]:
        """
        Read detailed pay statements for each individual.

        Deduction and contribution types are supported by the payroll systems that
        support Benefits.

        Args:
          requests: The array of batch requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/pay-statement",
            page=SyncResponsesPage[PayStatementResponse],
            body=maybe_transform(
                {"requests": requests}, pay_statement_retrieve_many_params.PayStatementRetrieveManyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayStatementResponse,
            method="post",
        )


class AsyncPayStatements(AsyncAPIResource):
    with_raw_response: AsyncPayStatementsWithRawResponse

    def __init__(self, client: AsyncFinch) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncPayStatementsWithRawResponse(self)

    def retrieve_many(
        self,
        *,
        requests: List[pay_statement_retrieve_many_params.Request],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PayStatementResponse, AsyncResponsesPage[PayStatementResponse]]:
        """
        Read detailed pay statements for each individual.

        Deduction and contribution types are supported by the payroll systems that
        support Benefits.

        Args:
          requests: The array of batch requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/pay-statement",
            page=AsyncResponsesPage[PayStatementResponse],
            body=maybe_transform(
                {"requests": requests}, pay_statement_retrieve_many_params.PayStatementRetrieveManyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayStatementResponse,
            method="post",
        )


class PayStatementsWithRawResponse:
    def __init__(self, pay_statements: PayStatements) -> None:
        self.retrieve_many = to_raw_response_wrapper(
            pay_statements.retrieve_many,
        )


class AsyncPayStatementsWithRawResponse:
    def __init__(self, pay_statements: AsyncPayStatements) -> None:
        self.retrieve_many = async_to_raw_response_wrapper(
            pay_statements.retrieve_many,
        )
