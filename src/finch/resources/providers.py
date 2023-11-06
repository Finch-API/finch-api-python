# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..types import Provider
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncSinglePage, AsyncSinglePage
from .._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from .._client import Finch, AsyncFinch

__all__ = ["Providers", "AsyncProviders"]


class Providers(SyncAPIResource):
    with_raw_response: ProvidersWithRawResponse

    def __init__(self, client: Finch) -> None:
        super().__init__(client)
        self.with_raw_response = ProvidersWithRawResponse(self)

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
    with_raw_response: AsyncProvidersWithRawResponse

    def __init__(self, client: AsyncFinch) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncProvidersWithRawResponse(self)

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
        self.list = to_raw_response_wrapper(
            providers.list,
        )


class AsyncProvidersWithRawResponse:
    def __init__(self, providers: AsyncProviders) -> None:
        self.list = async_to_raw_response_wrapper(
            providers.list,
        )
