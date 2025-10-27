# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
        customer_email: Optional[str],
        customer_id: str,
        customer_name: str,
        integration: Optional[session_new_params.Integration],
        manual: Optional[bool],
        minutes_to_expire: Optional[float],
        products: List[
            Literal[
                "benefits",
                "company",
                "deduction",
                "directory",
                "documents",
                "employment",
                "individual",
                "payment",
                "pay_statement",
                "ssn",
            ]
        ],
        redirect_uri: Optional[str],
        sandbox: Optional[Literal["finch", "provider"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionNewResponse:
        """
        Create a new connect session for an employer

        Args:
          customer_email: Email address of the customer

          customer_id: Unique identifier for the customer

          customer_name: Name of the customer

          integration: Integration configuration for the connect session

          manual: Enable manual authentication mode

          minutes_to_expire: The number of minutes until the session expires (defaults to 129,600, which is
              90 days)

          products: The Finch products to request access to

          redirect_uri: The URI to redirect to after the Connect flow is completed

          sandbox: Sandbox mode for testing

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/connect/sessions",
            body=maybe_transform(
                {
                    "customer_email": customer_email,
                    "customer_id": customer_id,
                    "customer_name": customer_name,
                    "integration": integration,
                    "manual": manual,
                    "minutes_to_expire": minutes_to_expire,
                    "products": products,
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
        minutes_to_expire: int,
        products: Optional[
            List[
                Literal[
                    "benefits",
                    "company",
                    "deduction",
                    "directory",
                    "documents",
                    "employment",
                    "individual",
                    "payment",
                    "pay_statement",
                    "ssn",
                ]
            ]
        ],
        redirect_uri: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        customer_email: Optional[str],
        customer_id: str,
        customer_name: str,
        integration: Optional[session_new_params.Integration],
        manual: Optional[bool],
        minutes_to_expire: Optional[float],
        products: List[
            Literal[
                "benefits",
                "company",
                "deduction",
                "directory",
                "documents",
                "employment",
                "individual",
                "payment",
                "pay_statement",
                "ssn",
            ]
        ],
        redirect_uri: Optional[str],
        sandbox: Optional[Literal["finch", "provider"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionNewResponse:
        """
        Create a new connect session for an employer

        Args:
          customer_email: Email address of the customer

          customer_id: Unique identifier for the customer

          customer_name: Name of the customer

          integration: Integration configuration for the connect session

          manual: Enable manual authentication mode

          minutes_to_expire: The number of minutes until the session expires (defaults to 129,600, which is
              90 days)

          products: The Finch products to request access to

          redirect_uri: The URI to redirect to after the Connect flow is completed

          sandbox: Sandbox mode for testing

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/connect/sessions",
            body=await async_maybe_transform(
                {
                    "customer_email": customer_email,
                    "customer_id": customer_id,
                    "customer_name": customer_name,
                    "integration": integration,
                    "manual": manual,
                    "minutes_to_expire": minutes_to_expire,
                    "products": products,
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
        minutes_to_expire: int,
        products: Optional[
            List[
                Literal[
                    "benefits",
                    "company",
                    "deduction",
                    "directory",
                    "documents",
                    "employment",
                    "individual",
                    "payment",
                    "pay_statement",
                    "ssn",
                ]
            ]
        ],
        redirect_uri: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
