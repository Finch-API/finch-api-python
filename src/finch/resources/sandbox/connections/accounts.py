# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from .... import _legacy_response
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...._base_client import (
    make_request_options,
)
from ....types.shared import ConnectionStatusType
from ....types.sandbox.connections import (
    AccountCreateResponse,
    AccountUpdateResponse,
    account_create_params,
    account_update_params,
)

__all__ = ["Accounts", "AsyncAccounts"]


class Accounts(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountsWithRawResponse:
        return AccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsWithStreamingResponse:
        return AccountsWithStreamingResponse(self)

    def create(
        self,
        *,
        company_id: str,
        provider_id: str,
        authentication_type: Literal["credential", "api_token", "oauth", "assisted"] | NotGiven = NOT_GIVEN,
        products: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountCreateResponse:
        """
        Create a new account for an existing connection (company/provider pair)

        Args:
          products: Optional, defaults to Organization products (`company`, `directory`,
              `employment`, `individual`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sandbox/connections/accounts",
            body=maybe_transform(
                {
                    "company_id": company_id,
                    "provider_id": provider_id,
                    "authentication_type": authentication_type,
                    "products": products,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountCreateResponse,
        )

    def update(
        self,
        *,
        connection_status: ConnectionStatusType | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountUpdateResponse:
        """Update an existing sandbox account.

        Change the connection status to understand
        how the Finch API responds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/sandbox/connections/accounts",
            body=maybe_transform({"connection_status": connection_status}, account_update_params.AccountUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountUpdateResponse,
        )


class AsyncAccounts(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountsWithRawResponse:
        return AsyncAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsWithStreamingResponse:
        return AsyncAccountsWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_id: str,
        provider_id: str,
        authentication_type: Literal["credential", "api_token", "oauth", "assisted"] | NotGiven = NOT_GIVEN,
        products: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountCreateResponse:
        """
        Create a new account for an existing connection (company/provider pair)

        Args:
          products: Optional, defaults to Organization products (`company`, `directory`,
              `employment`, `individual`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sandbox/connections/accounts",
            body=await async_maybe_transform(
                {
                    "company_id": company_id,
                    "provider_id": provider_id,
                    "authentication_type": authentication_type,
                    "products": products,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountCreateResponse,
        )

    async def update(
        self,
        *,
        connection_status: ConnectionStatusType | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountUpdateResponse:
        """Update an existing sandbox account.

        Change the connection status to understand
        how the Finch API responds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/sandbox/connections/accounts",
            body=await async_maybe_transform(
                {"connection_status": connection_status}, account_update_params.AccountUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountUpdateResponse,
        )


class AccountsWithRawResponse:
    def __init__(self, accounts: Accounts) -> None:
        self._accounts = accounts

        self.create = _legacy_response.to_raw_response_wrapper(
            accounts.create,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            accounts.update,
        )


class AsyncAccountsWithRawResponse:
    def __init__(self, accounts: AsyncAccounts) -> None:
        self._accounts = accounts

        self.create = _legacy_response.async_to_raw_response_wrapper(
            accounts.create,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            accounts.update,
        )


class AccountsWithStreamingResponse:
    def __init__(self, accounts: Accounts) -> None:
        self._accounts = accounts

        self.create = to_streamed_response_wrapper(
            accounts.create,
        )
        self.update = to_streamed_response_wrapper(
            accounts.update,
        )


class AsyncAccountsWithStreamingResponse:
    def __init__(self, accounts: AsyncAccounts) -> None:
        self._accounts = accounts

        self.create = async_to_streamed_response_wrapper(
            accounts.create,
        )
        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )
