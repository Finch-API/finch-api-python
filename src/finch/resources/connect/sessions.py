# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.connect import session_new_params, session_reauthenticate_params
from ...types.connect.session_new_response import SessionNewResponse
from ...types.connect.session_reauthenticate_response import SessionReauthenticateResponse

__all__ = ["Sessions", "AsyncSessions"]


class Sessions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SessionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return SessionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return SessionsWithStreamingResponse(self)

    def new(
        self,
        *,
        customer_id: str,
        customer_name: str,
        products: List[
            Literal["company", "directory", "individual", "employment", "payment", "pay_statement", "benefits", "ssn"]
        ],
        customer_email: Optional[str] | NotGiven = NOT_GIVEN,
        integration: Optional[session_new_params.Integration] | NotGiven = NOT_GIVEN,
        manual: Optional[bool] | NotGiven = NOT_GIVEN,
        minutes_to_expire: Optional[float] | NotGiven = NOT_GIVEN,
        redirect_uri: Optional[str] | NotGiven = NOT_GIVEN,
        sandbox: Optional[Literal["finch", "provider"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionNewResponse:
        """
        Create a new connect session for an employer

        Args:
          minutes_to_expire: The number of minutes until the session expires (defaults to 43,200, which is 30
              days)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/connect/sessions",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "customer_name": customer_name,
                    "products": products,
                    "customer_email": customer_email,
                    "integration": integration,
                    "manual": manual,
                    "minutes_to_expire": minutes_to_expire,
                    "redirect_uri": redirect_uri,
                    "sandbox": sandbox,
                },
                session_new_params.SessionNewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionNewResponse,
        )

    def reauthenticate(
        self,
        *,
        connection_id: str,
        minutes_to_expire: Optional[int] | NotGiven = NOT_GIVEN,
        products: Optional[
            List[
                Literal[
                    "company", "directory", "individual", "employment", "payment", "pay_statement", "benefits", "ssn"
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        redirect_uri: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionReauthenticateResponse:
        """
        Create a new Connect session for reauthenticating an existing connection

        Args:
          connection_id: The ID of the existing connection to reauthenticate

          minutes_to_expire: The number of minutes until the session expires (defaults to 43,200, which is 30
              days)

          products: The products to request access to (optional for reauthentication)

          redirect_uri: The URI to redirect to after the Connect flow is completed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/connect/sessions/reauthenticate",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "minutes_to_expire": minutes_to_expire,
                    "products": products,
                    "redirect_uri": redirect_uri,
                },
                session_reauthenticate_params.SessionReauthenticateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionReauthenticateResponse,
        )


class AsyncSessions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSessionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AsyncSessionsWithStreamingResponse(self)

    async def new(
        self,
        *,
        customer_id: str,
        customer_name: str,
        products: List[
            Literal["company", "directory", "individual", "employment", "payment", "pay_statement", "benefits", "ssn"]
        ],
        customer_email: Optional[str] | NotGiven = NOT_GIVEN,
        integration: Optional[session_new_params.Integration] | NotGiven = NOT_GIVEN,
        manual: Optional[bool] | NotGiven = NOT_GIVEN,
        minutes_to_expire: Optional[float] | NotGiven = NOT_GIVEN,
        redirect_uri: Optional[str] | NotGiven = NOT_GIVEN,
        sandbox: Optional[Literal["finch", "provider"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionNewResponse:
        """
        Create a new connect session for an employer

        Args:
          minutes_to_expire: The number of minutes until the session expires (defaults to 43,200, which is 30
              days)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/connect/sessions",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "customer_name": customer_name,
                    "products": products,
                    "customer_email": customer_email,
                    "integration": integration,
                    "manual": manual,
                    "minutes_to_expire": minutes_to_expire,
                    "redirect_uri": redirect_uri,
                    "sandbox": sandbox,
                },
                session_new_params.SessionNewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionNewResponse,
        )

    async def reauthenticate(
        self,
        *,
        connection_id: str,
        minutes_to_expire: Optional[int] | NotGiven = NOT_GIVEN,
        products: Optional[
            List[
                Literal[
                    "company", "directory", "individual", "employment", "payment", "pay_statement", "benefits", "ssn"
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        redirect_uri: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionReauthenticateResponse:
        """
        Create a new Connect session for reauthenticating an existing connection

        Args:
          connection_id: The ID of the existing connection to reauthenticate

          minutes_to_expire: The number of minutes until the session expires (defaults to 43,200, which is 30
              days)

          products: The products to request access to (optional for reauthentication)

          redirect_uri: The URI to redirect to after the Connect flow is completed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/connect/sessions/reauthenticate",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "minutes_to_expire": minutes_to_expire,
                    "products": products,
                    "redirect_uri": redirect_uri,
                },
                session_reauthenticate_params.SessionReauthenticateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionReauthenticateResponse,
        )


class SessionsWithRawResponse:
    def __init__(self, sessions: Sessions) -> None:
        self._sessions = sessions

        self.new = _legacy_response.to_raw_response_wrapper(
            sessions.new,
        )
        self.reauthenticate = _legacy_response.to_raw_response_wrapper(
            sessions.reauthenticate,
        )


class AsyncSessionsWithRawResponse:
    def __init__(self, sessions: AsyncSessions) -> None:
        self._sessions = sessions

        self.new = _legacy_response.async_to_raw_response_wrapper(
            sessions.new,
        )
        self.reauthenticate = _legacy_response.async_to_raw_response_wrapper(
            sessions.reauthenticate,
        )


class SessionsWithStreamingResponse:
    def __init__(self, sessions: Sessions) -> None:
        self._sessions = sessions

        self.new = to_streamed_response_wrapper(
            sessions.new,
        )
        self.reauthenticate = to_streamed_response_wrapper(
            sessions.reauthenticate,
        )


class AsyncSessionsWithStreamingResponse:
    def __init__(self, sessions: AsyncSessions) -> None:
        self._sessions = sessions

        self.new = async_to_streamed_response_wrapper(
            sessions.new,
        )
        self.reauthenticate = async_to_streamed_response_wrapper(
            sessions.reauthenticate,
        )
