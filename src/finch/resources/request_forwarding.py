# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .. import _legacy_response
from ..types import request_forwarding_forward_params
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
from ..types.request_forwarding_forward_response import RequestForwardingForwardResponse

__all__ = ["RequestForwardingResource", "AsyncRequestForwardingResource"]


class RequestForwardingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RequestForwardingResourceWithRawResponse:
        return RequestForwardingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestForwardingResourceWithStreamingResponse:
        return RequestForwardingResourceWithStreamingResponse(self)

    def forward(
        self,
        *,
        method: str,
        route: str,
        data: Optional[str] | NotGiven = NOT_GIVEN,
        headers: Optional[object] | NotGiven = NOT_GIVEN,
        params: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequestForwardingForwardResponse:
        """The Forward API allows you to make direct requests to an employment system.

        If
        Finch’s unified API doesn’t have a data model that cleanly fits your needs, then
        Forward allows you to push or pull data models directly against an integration’s
        API.

        Args:
          method: The HTTP method for the forwarded request. Valid values include: `GET` , `POST`
              , `PUT` , `DELETE` , and `PATCH`.

          route: The URL route path for the forwarded request. This value must begin with a
              forward-slash ( / ) and may only contain alphanumeric characters, hyphens, and
              underscores.

          data: The body for the forwarded request. This value must be specified as either a
              string or a valid JSON object.

          headers: The HTTP headers to include on the forwarded request. This value must be
              specified as an object of key-value pairs. Example:
              `{"Content-Type": "application/xml", "X-API-Version": "v1" }`

          params: The query parameters for the forwarded request. This value must be specified as
              a valid JSON object rather than a query string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/forward",
            body=maybe_transform(
                {
                    "method": method,
                    "route": route,
                    "data": data,
                    "headers": headers,
                    "params": params,
                },
                request_forwarding_forward_params.RequestForwardingForwardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestForwardingForwardResponse,
        )


class AsyncRequestForwardingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRequestForwardingResourceWithRawResponse:
        return AsyncRequestForwardingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestForwardingResourceWithStreamingResponse:
        return AsyncRequestForwardingResourceWithStreamingResponse(self)

    async def forward(
        self,
        *,
        method: str,
        route: str,
        data: Optional[str] | NotGiven = NOT_GIVEN,
        headers: Optional[object] | NotGiven = NOT_GIVEN,
        params: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequestForwardingForwardResponse:
        """The Forward API allows you to make direct requests to an employment system.

        If
        Finch’s unified API doesn’t have a data model that cleanly fits your needs, then
        Forward allows you to push or pull data models directly against an integration’s
        API.

        Args:
          method: The HTTP method for the forwarded request. Valid values include: `GET` , `POST`
              , `PUT` , `DELETE` , and `PATCH`.

          route: The URL route path for the forwarded request. This value must begin with a
              forward-slash ( / ) and may only contain alphanumeric characters, hyphens, and
              underscores.

          data: The body for the forwarded request. This value must be specified as either a
              string or a valid JSON object.

          headers: The HTTP headers to include on the forwarded request. This value must be
              specified as an object of key-value pairs. Example:
              `{"Content-Type": "application/xml", "X-API-Version": "v1" }`

          params: The query parameters for the forwarded request. This value must be specified as
              a valid JSON object rather than a query string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/forward",
            body=await async_maybe_transform(
                {
                    "method": method,
                    "route": route,
                    "data": data,
                    "headers": headers,
                    "params": params,
                },
                request_forwarding_forward_params.RequestForwardingForwardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestForwardingForwardResponse,
        )


class RequestForwardingResourceWithRawResponse:
    def __init__(self, request_forwarding: RequestForwardingResource) -> None:
        self._request_forwarding = request_forwarding

        self.forward = _legacy_response.to_raw_response_wrapper(
            request_forwarding.forward,
        )


class AsyncRequestForwardingResourceWithRawResponse:
    def __init__(self, request_forwarding: AsyncRequestForwardingResource) -> None:
        self._request_forwarding = request_forwarding

        self.forward = _legacy_response.async_to_raw_response_wrapper(
            request_forwarding.forward,
        )


class RequestForwardingResourceWithStreamingResponse:
    def __init__(self, request_forwarding: RequestForwardingResource) -> None:
        self._request_forwarding = request_forwarding

        self.forward = to_streamed_response_wrapper(
            request_forwarding.forward,
        )


class AsyncRequestForwardingResourceWithStreamingResponse:
    def __init__(self, request_forwarding: AsyncRequestForwardingResource) -> None:
        self._request_forwarding = request_forwarding

        self.forward = async_to_streamed_response_wrapper(
            request_forwarding.forward,
        )
