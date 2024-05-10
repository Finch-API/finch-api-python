# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Finch",
    "AsyncFinch",
    "Client",
    "AsyncClient",
]


class Finch(SyncAPIClient):
    access_tokens: resources.AccessTokensResource
    hris: resources.HRISResource
    providers: resources.ProvidersResource
    account: resources.AccountResource
    request_forwarding: resources.RequestForwardingResource
    jobs: resources.JobsResource
    sandbox: resources.SandboxResource
    with_raw_response: FinchWithRawResponse
    with_streaming_response: FinchWithStreamedResponse

    # client options
    access_token: str | None
    client_id: str | None
    client_secret: str | None
    sandbox_client_id: str | None
    sandbox_client_secret: str | None
    webhook_secret: str | None

    def __init__(
        self,
        *,
        access_token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        sandbox_client_id: str | None = None,
        sandbox_client_secret: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Finch client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `client_id` from `FINCH_CLIENT_ID`
        - `client_secret` from `FINCH_CLIENT_SECRET`
        - `sandbox_client_id` from `FINCH_SANDBOX_CLIENT_ID`
        - `sandbox_client_secret` from `FINCH_SANDBOX_CLIENT_SECRET`
        - `webhook_secret` from `FINCH_WEBHOOK_SECRET`
        """
        self.access_token = access_token

        if client_id is None:
            client_id = os.environ.get("FINCH_CLIENT_ID")
        self.client_id = client_id

        if client_secret is None:
            client_secret = os.environ.get("FINCH_CLIENT_SECRET")
        self.client_secret = client_secret

        if sandbox_client_id is None:
            sandbox_client_id = os.environ.get("FINCH_SANDBOX_CLIENT_ID")
        self.sandbox_client_id = sandbox_client_id

        if sandbox_client_secret is None:
            sandbox_client_secret = os.environ.get("FINCH_SANDBOX_CLIENT_SECRET")
        self.sandbox_client_secret = sandbox_client_secret

        if webhook_secret is None:
            webhook_secret = os.environ.get("FINCH_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        if base_url is None:
            base_url = os.environ.get("FINCH_BASE_URL")
        if base_url is None:
            base_url = f"https://api.tryfinch.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.access_tokens = resources.AccessTokensResource(self)
        self.hris = resources.HRISResource(self)
        self.providers = resources.ProvidersResource(self)
        self.account = resources.AccountResource(self)
        self.request_forwarding = resources.RequestForwardingResource(self)
        self.jobs = resources.JobsResource(self)
        self.sandbox = resources.SandboxResource(self)
        self.with_raw_response = FinchWithRawResponse(self)
        self.with_streaming_response = FinchWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        if self._bearer_auth:
            return self._bearer_auth
        if self._basic_auth:
            return self._basic_auth
        return {}

    @property
    def _bearer_auth(self) -> dict[str, str]:
        access_token = self.access_token
        if access_token is None:
            return {}
        return {"Authorization": f"Bearer {access_token}"}

    @property
    def _basic_auth(self) -> dict[str, str]:
        if self.sandbox_client_id is None:
            return {}
        if self.sandbox_client_secret is None:
            return {}
        credentials = f"{self.sandbox_client_id}:{self.sandbox_client_secret}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "Finch-API-Version": "2020-09-17",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.access_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        if self.sandbox_client_id and self.sandbox_client_secret and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either access_token, sandbox_client_id or sandbox_client_secret to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        access_token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        sandbox_client_id: str | None = None,
        sandbox_client_secret: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            access_token=access_token or self.access_token,
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            sandbox_client_id=sandbox_client_id or self.sandbox_client_id,
            sandbox_client_secret=sandbox_client_secret or self.sandbox_client_secret,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncFinch(AsyncAPIClient):
    access_tokens: resources.AsyncAccessTokensResource
    hris: resources.AsyncHRISResource
    providers: resources.AsyncProvidersResource
    account: resources.AsyncAccountResource
    request_forwarding: resources.AsyncRequestForwardingResource
    jobs: resources.AsyncJobsResource
    sandbox: resources.AsyncSandboxResource
    with_raw_response: AsyncFinchWithRawResponse
    with_streaming_response: AsyncFinchWithStreamedResponse

    # client options
    access_token: str | None
    client_id: str | None
    client_secret: str | None
    sandbox_client_id: str | None
    sandbox_client_secret: str | None
    webhook_secret: str | None

    def __init__(
        self,
        *,
        access_token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        sandbox_client_id: str | None = None,
        sandbox_client_secret: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async Finch client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `client_id` from `FINCH_CLIENT_ID`
        - `client_secret` from `FINCH_CLIENT_SECRET`
        - `sandbox_client_id` from `FINCH_SANDBOX_CLIENT_ID`
        - `sandbox_client_secret` from `FINCH_SANDBOX_CLIENT_SECRET`
        - `webhook_secret` from `FINCH_WEBHOOK_SECRET`
        """
        self.access_token = access_token

        if client_id is None:
            client_id = os.environ.get("FINCH_CLIENT_ID")
        self.client_id = client_id

        if client_secret is None:
            client_secret = os.environ.get("FINCH_CLIENT_SECRET")
        self.client_secret = client_secret

        if sandbox_client_id is None:
            sandbox_client_id = os.environ.get("FINCH_SANDBOX_CLIENT_ID")
        self.sandbox_client_id = sandbox_client_id

        if sandbox_client_secret is None:
            sandbox_client_secret = os.environ.get("FINCH_SANDBOX_CLIENT_SECRET")
        self.sandbox_client_secret = sandbox_client_secret

        if webhook_secret is None:
            webhook_secret = os.environ.get("FINCH_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        if base_url is None:
            base_url = os.environ.get("FINCH_BASE_URL")
        if base_url is None:
            base_url = f"https://api.tryfinch.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.access_tokens = resources.AsyncAccessTokensResource(self)
        self.hris = resources.AsyncHRISResource(self)
        self.providers = resources.AsyncProvidersResource(self)
        self.account = resources.AsyncAccountResource(self)
        self.request_forwarding = resources.AsyncRequestForwardingResource(self)
        self.jobs = resources.AsyncJobsResource(self)
        self.sandbox = resources.AsyncSandboxResource(self)
        self.with_raw_response = AsyncFinchWithRawResponse(self)
        self.with_streaming_response = AsyncFinchWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        if self._bearer_auth:
            return self._bearer_auth
        if self._basic_auth:
            return self._basic_auth
        return {}

    @property
    def _bearer_auth(self) -> dict[str, str]:
        access_token = self.access_token
        if access_token is None:
            return {}
        return {"Authorization": f"Bearer {access_token}"}

    @property
    def _basic_auth(self) -> dict[str, str]:
        if self.sandbox_client_id is None:
            return {}
        if self.sandbox_client_secret is None:
            return {}
        credentials = f"{self.sandbox_client_id}:{self.sandbox_client_secret}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "Finch-API-Version": "2020-09-17",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.access_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        if self.sandbox_client_id and self.sandbox_client_secret and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either access_token, sandbox_client_id or sandbox_client_secret to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        access_token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        sandbox_client_id: str | None = None,
        sandbox_client_secret: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            access_token=access_token or self.access_token,
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            sandbox_client_id=sandbox_client_id or self.sandbox_client_id,
            sandbox_client_secret=sandbox_client_secret or self.sandbox_client_secret,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class FinchWithRawResponse:
    def __init__(self, client: Finch) -> None:
        self.access_tokens = resources.AccessTokensResourceWithRawResponse(client.access_tokens)
        self.hris = resources.HRISResourceWithRawResponse(client.hris)
        self.providers = resources.ProvidersResourceWithRawResponse(client.providers)
        self.account = resources.AccountResourceWithRawResponse(client.account)
        self.request_forwarding = resources.RequestForwardingResourceWithRawResponse(client.request_forwarding)
        self.jobs = resources.JobsResourceWithRawResponse(client.jobs)
        self.sandbox = resources.SandboxResourceWithRawResponse(client.sandbox)


class AsyncFinchWithRawResponse:
    def __init__(self, client: AsyncFinch) -> None:
        self.access_tokens = resources.AsyncAccessTokensResourceWithRawResponse(client.access_tokens)
        self.hris = resources.AsyncHRISResourceWithRawResponse(client.hris)
        self.providers = resources.AsyncProvidersResourceWithRawResponse(client.providers)
        self.account = resources.AsyncAccountResourceWithRawResponse(client.account)
        self.request_forwarding = resources.AsyncRequestForwardingResourceWithRawResponse(client.request_forwarding)
        self.jobs = resources.AsyncJobsResourceWithRawResponse(client.jobs)
        self.sandbox = resources.AsyncSandboxResourceWithRawResponse(client.sandbox)


class FinchWithStreamedResponse:
    def __init__(self, client: Finch) -> None:
        self.access_tokens = resources.AccessTokensResourceWithStreamingResponse(client.access_tokens)
        self.hris = resources.HRISResourceWithStreamingResponse(client.hris)
        self.providers = resources.ProvidersResourceWithStreamingResponse(client.providers)
        self.account = resources.AccountResourceWithStreamingResponse(client.account)
        self.request_forwarding = resources.RequestForwardingResourceWithStreamingResponse(client.request_forwarding)
        self.jobs = resources.JobsResourceWithStreamingResponse(client.jobs)
        self.sandbox = resources.SandboxResourceWithStreamingResponse(client.sandbox)


class AsyncFinchWithStreamedResponse:
    def __init__(self, client: AsyncFinch) -> None:
        self.access_tokens = resources.AsyncAccessTokensResourceWithStreamingResponse(client.access_tokens)
        self.hris = resources.AsyncHRISResourceWithStreamingResponse(client.hris)
        self.providers = resources.AsyncProvidersResourceWithStreamingResponse(client.providers)
        self.account = resources.AsyncAccountResourceWithStreamingResponse(client.account)
        self.request_forwarding = resources.AsyncRequestForwardingResourceWithStreamingResponse(
            client.request_forwarding
        )
        self.jobs = resources.AsyncJobsResourceWithStreamingResponse(client.jobs)
        self.sandbox = resources.AsyncSandboxResourceWithStreamingResponse(client.sandbox)


Client = Finch

AsyncClient = AsyncFinch
