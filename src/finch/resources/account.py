# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import Introspection, DisconnectResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["Account", "AsyncAccount"]


class Account(SyncAPIResource):
    def disconnect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> DisconnectResponse:
        """
        Disconnect an employer from your application and invalidate all `access_token`s
        associated with the employer. We require applications to implement the
        Disconnect endpoint for billing and security purposes.
        """
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
    async def disconnect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> DisconnectResponse:
        """
        Disconnect an employer from your application and invalidate all `access_token`s
        associated with the employer. We require applications to implement the
        Disconnect endpoint for billing and security purposes.
        """
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Introspection:
        """Read account information associated with an `access_token`"""
        return await self._get(
            "/introspect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Introspection,
        )
