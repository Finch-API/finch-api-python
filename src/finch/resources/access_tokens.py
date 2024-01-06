# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..types import CreateAccessTokenResponse, access_token_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["AccessTokens", "AsyncAccessTokens"]


class AccessTokens(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessTokensWithRawResponse:
        return AccessTokensWithRawResponse(self)

    def create(
        self,
        *,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateAccessTokenResponse:
        """
        Exchange the authorization code for an access token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth/token",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "code": code,
                    "redirect_uri": redirect_uri,
                },
                access_token_create_params.AccessTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateAccessTokenResponse,
        )


class AsyncAccessTokens(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessTokensWithRawResponse:
        return AsyncAccessTokensWithRawResponse(self)

    async def create(
        self,
        *,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateAccessTokenResponse:
        """
        Exchange the authorization code for an access token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth/token",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "code": code,
                    "redirect_uri": redirect_uri,
                },
                access_token_create_params.AccessTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateAccessTokenResponse,
        )


class AccessTokensWithRawResponse:
    def __init__(self, access_tokens: AccessTokens) -> None:
        self.create = to_raw_response_wrapper(
            access_tokens.create,
        )


class AsyncAccessTokensWithRawResponse:
    def __init__(self, access_tokens: AsyncAccessTokens) -> None:
        self.create = async_to_raw_response_wrapper(
            access_tokens.create,
        )
