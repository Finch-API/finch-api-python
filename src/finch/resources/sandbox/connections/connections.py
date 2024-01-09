# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from .accounts import Accounts, AsyncAccounts, AccountsWithRawResponse, AsyncAccountsWithRawResponse
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...._base_client import (
    make_request_options,
)
from ....types.sandbox import ConnectionCreateResponse, connection_create_params

__all__ = ["Connections", "AsyncConnections"]


class Connections(SyncAPIResource):
    @cached_property
    def accounts(self) -> Accounts:
        return Accounts(self._client)

    @cached_property
    def with_raw_response(self) -> ConnectionsWithRawResponse:
        return ConnectionsWithRawResponse(self)

    def create(
        self,
        *,
        provider_id: str,
        authentication_type: Literal["credentials", "api_token", "oauth", "assisted"] | NotGiven = NOT_GIVEN,
        employer_size: int | NotGiven = NOT_GIVEN,
        products: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionCreateResponse:
        """
        Create a new connection (new company/provider pair) with a new account

        Args:
          employer_size: Optional: the size of the employer to be created with this connection. Defaults
              to 20

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sandbox/connections",
            body=maybe_transform(
                {
                    "provider_id": provider_id,
                    "authentication_type": authentication_type,
                    "employer_size": employer_size,
                    "products": products,
                },
                connection_create_params.ConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionCreateResponse,
        )


class AsyncConnections(AsyncAPIResource):
    @cached_property
    def accounts(self) -> AsyncAccounts:
        return AsyncAccounts(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConnectionsWithRawResponse:
        return AsyncConnectionsWithRawResponse(self)

    async def create(
        self,
        *,
        provider_id: str,
        authentication_type: Literal["credentials", "api_token", "oauth", "assisted"] | NotGiven = NOT_GIVEN,
        employer_size: int | NotGiven = NOT_GIVEN,
        products: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionCreateResponse:
        """
        Create a new connection (new company/provider pair) with a new account

        Args:
          employer_size: Optional: the size of the employer to be created with this connection. Defaults
              to 20

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sandbox/connections",
            body=maybe_transform(
                {
                    "provider_id": provider_id,
                    "authentication_type": authentication_type,
                    "employer_size": employer_size,
                    "products": products,
                },
                connection_create_params.ConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionCreateResponse,
        )


class ConnectionsWithRawResponse:
    def __init__(self, connections: Connections) -> None:
        self.accounts = AccountsWithRawResponse(connections.accounts)

        self.create = to_raw_response_wrapper(
            connections.create,
        )


class AsyncConnectionsWithRawResponse:
    def __init__(self, connections: AsyncConnections) -> None:
        self.accounts = AsyncAccountsWithRawResponse(connections.accounts)

        self.create = async_to_raw_response_wrapper(
            connections.create,
        )
