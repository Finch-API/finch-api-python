# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _legacy_response
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import make_request_options
from ..types.introspection import Introspection
from ..types.disconnect_response import DisconnectResponse

__all__ = ["Account", "AsyncAccount"]


class Account(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountWithRawResponse:
        return AccountWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountWithStreamingResponse:
        return AccountWithStreamingResponse(self)

    def disconnect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DisconnectResponse:
        """Disconnect one or more `access_token`s from your application."""
        return self._post(
            "/disconnect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisconnectResponse,
        )

    def introspect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Introspection:
        """Read account information associated with an `access_token`"""
        return self._get(
            "/introspect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Introspection,
        )


class AsyncAccount(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountWithRawResponse:
        return AsyncAccountWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountWithStreamingResponse:
        return AsyncAccountWithStreamingResponse(self)

    async def disconnect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DisconnectResponse:
        """Disconnect one or more `access_token`s from your application."""
        return await self._post(
            "/disconnect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisconnectResponse,
        )

    async def introspect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Introspection:
        """Read account information associated with an `access_token`"""
        return await self._get(
            "/introspect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Introspection,
        )


class AccountWithRawResponse:
    def __init__(self, account: Account) -> None:
        self._account = account

        self.disconnect = _legacy_response.to_raw_response_wrapper(
            account.disconnect,
        )
        self.introspect = _legacy_response.to_raw_response_wrapper(
            account.introspect,
        )


class AsyncAccountWithRawResponse:
    def __init__(self, account: AsyncAccount) -> None:
        self._account = account

        self.disconnect = _legacy_response.async_to_raw_response_wrapper(
            account.disconnect,
        )
        self.introspect = _legacy_response.async_to_raw_response_wrapper(
            account.introspect,
        )


class AccountWithStreamingResponse:
    def __init__(self, account: Account) -> None:
        self._account = account

        self.disconnect = to_streamed_response_wrapper(
            account.disconnect,
        )
        self.introspect = to_streamed_response_wrapper(
            account.introspect,
        )


class AsyncAccountWithStreamingResponse:
    def __init__(self, account: AsyncAccount) -> None:
        self._account = account

        self.disconnect = async_to_streamed_response_wrapper(
            account.disconnect,
        )
        self.introspect = async_to_streamed_response_wrapper(
            account.introspect,
        )
