# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import Provider
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncSinglePage, AsyncSinglePage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["Providers", "AsyncProviders"]


class Providers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProvidersWithRawResponse:
        return ProvidersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProvidersWithStreamingResponse:
        return ProvidersWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Provider]:
        """Return details on all available payroll and HR systems."""
        return self._get_api_list(
            "/providers",
            page=SyncSinglePage[Provider],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Provider,
        )


class AsyncProviders(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProvidersWithRawResponse:
        return AsyncProvidersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProvidersWithStreamingResponse:
        return AsyncProvidersWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Provider, AsyncSinglePage[Provider]]:
        """Return details on all available payroll and HR systems."""
        return self._get_api_list(
            "/providers",
            page=AsyncSinglePage[Provider],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Provider,
        )


class ProvidersWithRawResponse:
    def __init__(self, providers: Providers) -> None:
        self._providers = providers

        self.list = _legacy_response.to_raw_response_wrapper(
            providers.list,
        )


class AsyncProvidersWithRawResponse:
    def __init__(self, providers: AsyncProviders) -> None:
        self._providers = providers

        self.list = _legacy_response.async_to_raw_response_wrapper(
            providers.list,
        )


class ProvidersWithStreamingResponse:
    def __init__(self, providers: Providers) -> None:
        self._providers = providers

        self.list = to_streamed_response_wrapper(
            providers.list,
        )


class AsyncProvidersWithStreamingResponse:
    def __init__(self, providers: AsyncProviders) -> None:
        self._providers = providers

        self.list = async_to_streamed_response_wrapper(
            providers.list,
        )
