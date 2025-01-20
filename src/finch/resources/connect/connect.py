# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sessions import (
    Sessions,
    AsyncSessions,
    SessionsWithRawResponse,
    AsyncSessionsWithRawResponse,
    SessionsWithStreamingResponse,
    AsyncSessionsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Connect", "AsyncConnect"]


class Connect(SyncAPIResource):
    @cached_property
    def sessions(self) -> Sessions:
        return Sessions(self._client)

    @cached_property
    def with_raw_response(self) -> ConnectWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return ConnectWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return ConnectWithStreamingResponse(self)


class AsyncConnect(AsyncAPIResource):
    @cached_property
    def sessions(self) -> AsyncSessions:
        return AsyncSessions(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConnectWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AsyncConnectWithStreamingResponse(self)


class ConnectWithRawResponse:
    def __init__(self, connect: Connect) -> None:
        self._connect = connect

    @cached_property
    def sessions(self) -> SessionsWithRawResponse:
        return SessionsWithRawResponse(self._connect.sessions)


class AsyncConnectWithRawResponse:
    def __init__(self, connect: AsyncConnect) -> None:
        self._connect = connect

    @cached_property
    def sessions(self) -> AsyncSessionsWithRawResponse:
        return AsyncSessionsWithRawResponse(self._connect.sessions)


class ConnectWithStreamingResponse:
    def __init__(self, connect: Connect) -> None:
        self._connect = connect

    @cached_property
    def sessions(self) -> SessionsWithStreamingResponse:
        return SessionsWithStreamingResponse(self._connect.sessions)


class AsyncConnectWithStreamingResponse:
    def __init__(self, connect: AsyncConnect) -> None:
        self._connect = connect

    @cached_property
    def sessions(self) -> AsyncSessionsWithStreamingResponse:
        return AsyncSessionsWithStreamingResponse(self._connect.sessions)
