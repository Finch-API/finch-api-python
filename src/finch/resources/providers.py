# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import Provider
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncSinglePage, AsyncSinglePage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["Providers", "AsyncProviders"]


class Providers(SyncAPIResource):
    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
