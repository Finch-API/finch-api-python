# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import account_disconnect_entity_params
from .._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import make_request_options
from ..types.introspection import Introspection
from ..types.disconnect_response import DisconnectResponse
from ..types.disconnect_entity_response import DisconnectEntityResponse

__all__ = ["Account", "AsyncAccount"]


class Account(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AccountWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AccountWithStreamingResponse(self)

    def disconnect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DisconnectResponse:
        """Disconnect one or more `access_token`s from your application."""
        return self._post(
            "/disconnect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=DisconnectResponse,
        )

    def disconnect_entity(
        self,
        *,
        entity_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DisconnectEntityResponse:
        """
        Disconnect entity(s) from a connection without affecting other entities
        associated with the same connection.

        Args:
          entity_ids: Array of entity UUIDs to disconnect. At least one entity ID must be provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/disconnect-entity",
            body=maybe_transform(
                {"entity_ids": entity_ids}, account_disconnect_entity_params.AccountDisconnectEntityParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=DisconnectEntityResponse,
        )

    def introspect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Introspection:
        """Read account information associated with an `access_token`"""
        return self._get(
            "/introspect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=Introspection,
        )


class AsyncAccount(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AsyncAccountWithStreamingResponse(self)

    async def disconnect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DisconnectResponse:
        """Disconnect one or more `access_token`s from your application."""
        return await self._post(
            "/disconnect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=DisconnectResponse,
        )

    async def disconnect_entity(
        self,
        *,
        entity_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DisconnectEntityResponse:
        """
        Disconnect entity(s) from a connection without affecting other entities
        associated with the same connection.

        Args:
          entity_ids: Array of entity UUIDs to disconnect. At least one entity ID must be provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/disconnect-entity",
            body=await async_maybe_transform(
                {"entity_ids": entity_ids}, account_disconnect_entity_params.AccountDisconnectEntityParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=DisconnectEntityResponse,
        )

    async def introspect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Introspection:
        """Read account information associated with an `access_token`"""
        return await self._get(
            "/introspect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=Introspection,
        )


class AccountWithRawResponse:
    def __init__(self, account: Account) -> None:
        self._account = account

        self.disconnect = _legacy_response.to_raw_response_wrapper(
            account.disconnect,
        )
        self.disconnect_entity = _legacy_response.to_raw_response_wrapper(
            account.disconnect_entity,
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
        self.disconnect_entity = _legacy_response.async_to_raw_response_wrapper(
            account.disconnect_entity,
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
        self.disconnect_entity = to_streamed_response_wrapper(
            account.disconnect_entity,
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
        self.disconnect_entity = async_to_streamed_response_wrapper(
            account.disconnect_entity,
        )
        self.introspect = async_to_streamed_response_wrapper(
            account.introspect,
        )
