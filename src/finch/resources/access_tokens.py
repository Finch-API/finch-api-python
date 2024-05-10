# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import access_token_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import (
    make_request_options,
)
from ..types.create_access_token_response import CreateAccessTokenResponse

__all__ = ["AccessTokensResource", "AsyncAccessTokensResource"]


class AccessTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessTokensResourceWithRawResponse:
        return AccessTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessTokensResourceWithStreamingResponse:
        return AccessTokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        code: str,
        client_id: str | NotGiven = NOT_GIVEN,
        client_secret: str | NotGiven = NOT_GIVEN,
        redirect_uri: str | NotGiven = NOT_GIVEN,
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
                    "code": code,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "redirect_uri": redirect_uri,
                },
                access_token_create_params.AccessTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateAccessTokenResponse,
        )


class AsyncAccessTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessTokensResourceWithRawResponse:
        return AsyncAccessTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessTokensResourceWithStreamingResponse:
        return AsyncAccessTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        code: str,
        client_id: str | NotGiven = NOT_GIVEN,
        client_secret: str | NotGiven = NOT_GIVEN,
        redirect_uri: str | NotGiven = NOT_GIVEN,
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
            body=await async_maybe_transform(
                {
                    "code": code,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "redirect_uri": redirect_uri,
                },
                access_token_create_params.AccessTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateAccessTokenResponse,
        )


class AccessTokensResourceWithRawResponse:
    def __init__(self, access_tokens: AccessTokensResource) -> None:
        self._access_tokens = access_tokens

        self.create = _legacy_response.to_raw_response_wrapper(
            access_tokens.create,
        )


class AsyncAccessTokensResourceWithRawResponse:
    def __init__(self, access_tokens: AsyncAccessTokensResource) -> None:
        self._access_tokens = access_tokens

        self.create = _legacy_response.async_to_raw_response_wrapper(
            access_tokens.create,
        )


class AccessTokensResourceWithStreamingResponse:
    def __init__(self, access_tokens: AccessTokensResource) -> None:
        self._access_tokens = access_tokens

        self.create = to_streamed_response_wrapper(
            access_tokens.create,
        )


class AsyncAccessTokensResourceWithStreamingResponse:
    def __init__(self, access_tokens: AsyncAccessTokensResource) -> None:
        self._access_tokens = access_tokens

        self.create = async_to_streamed_response_wrapper(
            access_tokens.create,
        )
