# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .... import _legacy_response
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...._base_client import (
    make_request_options,
)
from ....types.sandbox.jobs import SandboxJobConfiguration, ConfigurationRetrieveResponse, configuration_update_params

__all__ = ["Configuration", "AsyncConfiguration"]


class Configuration(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigurationWithRawResponse:
        return ConfigurationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationWithStreamingResponse:
        return ConfigurationWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationRetrieveResponse:
        """Get configurations for sandbox jobs"""
        return self._get(
            "/sandbox/jobs/configuration",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationRetrieveResponse,
        )

    def update(
        self,
        *,
        completion_status: Literal["complete", "reauth_error", "permissions_error", "error"],
        type: Literal["data_sync_all"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SandboxJobConfiguration:
        """
        Update configurations for sandbox jobs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/sandbox/jobs/configuration",
            body=maybe_transform(
                {
                    "completion_status": completion_status,
                    "type": type,
                },
                configuration_update_params.ConfigurationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxJobConfiguration,
        )


class AsyncConfiguration(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigurationWithRawResponse:
        return AsyncConfigurationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationWithStreamingResponse:
        return AsyncConfigurationWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationRetrieveResponse:
        """Get configurations for sandbox jobs"""
        return await self._get(
            "/sandbox/jobs/configuration",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationRetrieveResponse,
        )

    async def update(
        self,
        *,
        completion_status: Literal["complete", "reauth_error", "permissions_error", "error"],
        type: Literal["data_sync_all"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SandboxJobConfiguration:
        """
        Update configurations for sandbox jobs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/sandbox/jobs/configuration",
            body=maybe_transform(
                {
                    "completion_status": completion_status,
                    "type": type,
                },
                configuration_update_params.ConfigurationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxJobConfiguration,
        )


class ConfigurationWithRawResponse:
    def __init__(self, configuration: Configuration) -> None:
        self._configuration = configuration

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            configuration.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            configuration.update,
        )


class AsyncConfigurationWithRawResponse:
    def __init__(self, configuration: AsyncConfiguration) -> None:
        self._configuration = configuration

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            configuration.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            configuration.update,
        )


class ConfigurationWithStreamingResponse:
    def __init__(self, configuration: Configuration) -> None:
        self._configuration = configuration

        self.retrieve = to_streamed_response_wrapper(
            configuration.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            configuration.update,
        )


class AsyncConfigurationWithStreamingResponse:
    def __init__(self, configuration: AsyncConfiguration) -> None:
        self._configuration = configuration

        self.retrieve = async_to_streamed_response_wrapper(
            configuration.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            configuration.update,
        )
