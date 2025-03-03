# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
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
from .resources import account, webhooks, providers, access_tokens, request_forwarding
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.hris import hris
from .resources.jobs import jobs
from .resources.connect import connect
from .resources.payroll import payroll
from .resources.sandbox import sandbox

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Finch", "AsyncFinch", "Client", "AsyncClient"]


class Finch(SyncAPIClient):
    access_tokens: access_tokens.AccessTokens
    hris: hris.HRIS
    providers: providers.Providers
    account: account.Account
    webhooks: webhooks.Webhooks
    request_forwarding: request_forwarding.RequestForwarding
    jobs: jobs.Jobs
    sandbox: sandbox.Sandbox
    payroll: payroll.Payroll
    connect: connect.Connect
    with_raw_response: FinchWithRawResponse
    with_streaming_response: FinchWithStreamedResponse

    # client options
    access_token: str | None
    client_id: str | None
    client_secret: str | None
    webhook_secret: str | None

    def __init__(
        self,
        *,
        access_token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
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
        - `webhook_secret` from `FINCH_WEBHOOK_SECRET`
        """
        self.access_token = access_token

        if client_id is None:
            client_id = os.environ.get("FINCH_CLIENT_ID")
        self.client_id = client_id

        if client_secret is None:
            client_secret = os.environ.get("FINCH_CLIENT_SECRET")
        self.client_secret = client_secret

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

        self.access_tokens = access_tokens.AccessTokens(self)
        self.hris = hris.HRIS(self)
        self.providers = providers.Providers(self)
        self.account = account.Account(self)
        self.webhooks = webhooks.Webhooks(self)
        self.request_forwarding = request_forwarding.RequestForwarding(self)
        self.jobs = jobs.Jobs(self)
        self.sandbox = sandbox.Sandbox(self)
        self.payroll = payroll.Payroll(self)
        self.connect = connect.Connect(self)
        self.with_raw_response = FinchWithRawResponse(self)
        self.with_streaming_response = FinchWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

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
        if self.client_id is None:
            return {}
        if self.client_secret is None:
            return {}
        credentials = f"{self.client_id}:{self.client_secret}".encode("ascii")
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

        if self.client_id and self.client_secret and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either access_token, client_id or client_secret to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        access_token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
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

    def get_access_token(
        self,
        code: str,
        *,
        redirect_uri: str | None = None,
    ) -> str:
        """DEPRECATED: use client.access_tokens.create instead."""
        if self.client_id is None:
            raise ValueError("Expected client_id to be set in order to call get_access_token")

        if self.client_secret is None:
            raise ValueError("Expected client_secret to be set in order to call get_access_token")

        response = self.post(
            "/auth/token",
            body={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "code": code,
                "redirect_uri": redirect_uri,
            },
            options={"headers": {"Authorization": Omit()}},
            cast_to=httpx.Response,
        )
        data = response.json()
        return str(data["access_token"])

    def get_auth_url(
        self,
        *,
        products: str,
        redirect_uri: str,
        sandbox: bool,
    ) -> str:
        """
        Returns the authorization url which can be visited in order to obtain an
        authorization code from Finch. The authorization code can then be exchanged for
        an access token for the Finch api by calling get_access_token().
        """
        if self.client_id is None:
            raise ValueError("Expected the client_id to be set in order to call get_auth_url")

        return str(
            httpx.URL(
                "https://connect.tryfinch.com/authorize",
                params={
                    "client_id": self.client_id,
                    "products": products,
                    "redirect_uri": redirect_uri,
                    "sandbox": sandbox,
                },
            )
        )

    def with_access_token(
        self,
        access_token: str,
    ) -> Self:
        """
        Returns a copy of the current Finch client with the given access token for
        authentication.
        """
        return self.with_options(access_token=access_token)

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
    access_tokens: access_tokens.AsyncAccessTokens
    hris: hris.AsyncHRIS
    providers: providers.AsyncProviders
    account: account.AsyncAccount
    webhooks: webhooks.AsyncWebhooks
    request_forwarding: request_forwarding.AsyncRequestForwarding
    jobs: jobs.AsyncJobs
    sandbox: sandbox.AsyncSandbox
    payroll: payroll.AsyncPayroll
    connect: connect.AsyncConnect
    with_raw_response: AsyncFinchWithRawResponse
    with_streaming_response: AsyncFinchWithStreamedResponse

    # client options
    access_token: str | None
    client_id: str | None
    client_secret: str | None
    webhook_secret: str | None

    def __init__(
        self,
        *,
        access_token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
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
        """Construct a new async AsyncFinch client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `client_id` from `FINCH_CLIENT_ID`
        - `client_secret` from `FINCH_CLIENT_SECRET`
        - `webhook_secret` from `FINCH_WEBHOOK_SECRET`
        """
        self.access_token = access_token

        if client_id is None:
            client_id = os.environ.get("FINCH_CLIENT_ID")
        self.client_id = client_id

        if client_secret is None:
            client_secret = os.environ.get("FINCH_CLIENT_SECRET")
        self.client_secret = client_secret

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

        self.access_tokens = access_tokens.AsyncAccessTokens(self)
        self.hris = hris.AsyncHRIS(self)
        self.providers = providers.AsyncProviders(self)
        self.account = account.AsyncAccount(self)
        self.webhooks = webhooks.AsyncWebhooks(self)
        self.request_forwarding = request_forwarding.AsyncRequestForwarding(self)
        self.jobs = jobs.AsyncJobs(self)
        self.sandbox = sandbox.AsyncSandbox(self)
        self.payroll = payroll.AsyncPayroll(self)
        self.connect = connect.AsyncConnect(self)
        self.with_raw_response = AsyncFinchWithRawResponse(self)
        self.with_streaming_response = AsyncFinchWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

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
        if self.client_id is None:
            return {}
        if self.client_secret is None:
            return {}
        credentials = f"{self.client_id}:{self.client_secret}".encode("ascii")
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

        if self.client_id and self.client_secret and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either access_token, client_id or client_secret to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        access_token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
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

    async def get_access_token(
        self,
        code: str,
        *,
        redirect_uri: str | None = None,
    ) -> str:
        """DEPRECATED: use client.access_tokens.create instead."""
        if self.client_id is None:
            raise ValueError("Expected client_id to be set in order to call get_access_token")

        if self.client_secret is None:
            raise ValueError("Expected client_secret to be set in order to call get_access_token")

        response = await self.post(
            "/auth/token",
            body={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "code": code,
                "redirect_uri": redirect_uri,
            },
            options={"headers": {"Authorization": Omit()}},
            cast_to=httpx.Response,
        )
        data = response.json()
        return str(data["access_token"])

    def get_auth_url(
        self,
        *,
        products: str,
        redirect_uri: str,
        sandbox: bool,
    ) -> str:
        """
        Returns the authorization url which can be visited in order to obtain an
        authorization code from Finch. The authorization code can then be exchanged for
        an access token for the Finch api by calling get_access_token().
        """
        if self.client_id is None:
            raise ValueError("Expected the client_id to be set in order to call get_auth_url")

        return str(
            httpx.URL(
                "https://connect.tryfinch.com/authorize",
                params={
                    "client_id": self.client_id,
                    "products": products,
                    "redirect_uri": redirect_uri,
                    "sandbox": sandbox,
                },
            )
        )

    def with_access_token(
        self,
        access_token: str,
    ) -> Self:
        """
        Returns a copy of the current Finch client with the given access token for
        authentication.
        """
        return self.with_options(access_token=access_token)

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
        self.access_tokens = access_tokens.AccessTokensWithRawResponse(client.access_tokens)
        self.hris = hris.HRISWithRawResponse(client.hris)
        self.providers = providers.ProvidersWithRawResponse(client.providers)
        self.account = account.AccountWithRawResponse(client.account)
        self.request_forwarding = request_forwarding.RequestForwardingWithRawResponse(client.request_forwarding)
        self.jobs = jobs.JobsWithRawResponse(client.jobs)
        self.sandbox = sandbox.SandboxWithRawResponse(client.sandbox)
        self.payroll = payroll.PayrollWithRawResponse(client.payroll)
        self.connect = connect.ConnectWithRawResponse(client.connect)


class AsyncFinchWithRawResponse:
    def __init__(self, client: AsyncFinch) -> None:
        self.access_tokens = access_tokens.AsyncAccessTokensWithRawResponse(client.access_tokens)
        self.hris = hris.AsyncHRISWithRawResponse(client.hris)
        self.providers = providers.AsyncProvidersWithRawResponse(client.providers)
        self.account = account.AsyncAccountWithRawResponse(client.account)
        self.request_forwarding = request_forwarding.AsyncRequestForwardingWithRawResponse(client.request_forwarding)
        self.jobs = jobs.AsyncJobsWithRawResponse(client.jobs)
        self.sandbox = sandbox.AsyncSandboxWithRawResponse(client.sandbox)
        self.payroll = payroll.AsyncPayrollWithRawResponse(client.payroll)
        self.connect = connect.AsyncConnectWithRawResponse(client.connect)


class FinchWithStreamedResponse:
    def __init__(self, client: Finch) -> None:
        self.access_tokens = access_tokens.AccessTokensWithStreamingResponse(client.access_tokens)
        self.hris = hris.HRISWithStreamingResponse(client.hris)
        self.providers = providers.ProvidersWithStreamingResponse(client.providers)
        self.account = account.AccountWithStreamingResponse(client.account)
        self.request_forwarding = request_forwarding.RequestForwardingWithStreamingResponse(client.request_forwarding)
        self.jobs = jobs.JobsWithStreamingResponse(client.jobs)
        self.sandbox = sandbox.SandboxWithStreamingResponse(client.sandbox)
        self.payroll = payroll.PayrollWithStreamingResponse(client.payroll)
        self.connect = connect.ConnectWithStreamingResponse(client.connect)


class AsyncFinchWithStreamedResponse:
    def __init__(self, client: AsyncFinch) -> None:
        self.access_tokens = access_tokens.AsyncAccessTokensWithStreamingResponse(client.access_tokens)
        self.hris = hris.AsyncHRISWithStreamingResponse(client.hris)
        self.providers = providers.AsyncProvidersWithStreamingResponse(client.providers)
        self.account = account.AsyncAccountWithStreamingResponse(client.account)
        self.request_forwarding = request_forwarding.AsyncRequestForwardingWithStreamingResponse(
            client.request_forwarding
        )
        self.jobs = jobs.AsyncJobsWithStreamingResponse(client.jobs)
        self.sandbox = sandbox.AsyncSandboxWithStreamingResponse(client.sandbox)
        self.payroll = payroll.AsyncPayrollWithStreamingResponse(client.payroll)
        self.connect = connect.AsyncConnectWithStreamingResponse(client.connect)


Client = Finch

AsyncClient = AsyncFinch
