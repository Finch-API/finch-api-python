# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import TYPE_CHECKING, Any, Union, Mapping
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
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        hris,
        jobs,
        account,
        connect,
        payroll,
        sandbox,
        webhooks,
        providers,
        access_tokens,
        request_forwarding,
    )
    from .resources.account import Account, AsyncAccount
    from .resources.hris.hris import HRIS, AsyncHRIS
    from .resources.jobs.jobs import Jobs, AsyncJobs
    from .resources.providers import Providers, AsyncProviders
    from .resources.access_tokens import AccessTokens, AsyncAccessTokens
    from .resources.connect.connect import Connect, AsyncConnect
    from .resources.payroll.payroll import Payroll, AsyncPayroll
    from .resources.sandbox.sandbox import Sandbox, AsyncSandbox
    from .resources.request_forwarding import RequestForwarding, AsyncRequestForwarding

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Finch", "AsyncFinch", "Client", "AsyncClient"]


class Finch(SyncAPIClient):
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

    @cached_property
    def access_tokens(self) -> AccessTokens:
        from .resources.access_tokens import AccessTokens

        return AccessTokens(self)

    @cached_property
    def hris(self) -> HRIS:
        from .resources.hris import HRIS

        return HRIS(self)

    @cached_property
    def providers(self) -> Providers:
        from .resources.providers import Providers

        return Providers(self)

    @cached_property
    def account(self) -> Account:
        from .resources.account import Account

        return Account(self)

    @cached_property
    def request_forwarding(self) -> RequestForwarding:
        from .resources.request_forwarding import RequestForwarding

        return RequestForwarding(self)

    @cached_property
    def jobs(self) -> Jobs:
        from .resources.jobs import Jobs

        return Jobs(self)

    @cached_property
    def sandbox(self) -> Sandbox:
        from .resources.sandbox import Sandbox

        return Sandbox(self)

    @cached_property
    def payroll(self) -> Payroll:
        from .resources.payroll import Payroll

        return Payroll(self)

    @cached_property
    def connect(self) -> Connect:
        from .resources.connect import Connect

        return Connect(self)

    @cached_property
    def webhooks(self) -> webhooks.Webhooks:
        from .resources.webhooks import Webhooks

        return Webhooks(self)

    @cached_property
    def with_raw_response(self) -> FinchWithRawResponse:
        return FinchWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FinchWithStreamedResponse:
        return FinchWithStreamedResponse(self)

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

    @cached_property
    def access_tokens(self) -> AsyncAccessTokens:
        from .resources.access_tokens import AsyncAccessTokens

        return AsyncAccessTokens(self)

    @cached_property
    def hris(self) -> AsyncHRIS:
        from .resources.hris import AsyncHRIS

        return AsyncHRIS(self)

    @cached_property
    def providers(self) -> AsyncProviders:
        from .resources.providers import AsyncProviders

        return AsyncProviders(self)

    @cached_property
    def account(self) -> AsyncAccount:
        from .resources.account import AsyncAccount

        return AsyncAccount(self)

    @cached_property
    def request_forwarding(self) -> AsyncRequestForwarding:
        from .resources.request_forwarding import AsyncRequestForwarding

        return AsyncRequestForwarding(self)

    @cached_property
    def jobs(self) -> AsyncJobs:
        from .resources.jobs import AsyncJobs

        return AsyncJobs(self)

    @cached_property
    def sandbox(self) -> AsyncSandbox:
        from .resources.sandbox import AsyncSandbox

        return AsyncSandbox(self)

    @cached_property
    def payroll(self) -> AsyncPayroll:
        from .resources.payroll import AsyncPayroll

        return AsyncPayroll(self)

    @cached_property
    def connect(self) -> AsyncConnect:
        from .resources.connect import AsyncConnect

        return AsyncConnect(self)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooks:
        from .resources.webhooks import AsyncWebhooks

        return AsyncWebhooks(self)

    @cached_property
    def with_raw_response(self) -> AsyncFinchWithRawResponse:
        return AsyncFinchWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFinchWithStreamedResponse:
        return AsyncFinchWithStreamedResponse(self)

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
    _client: Finch

    def __init__(self, client: Finch) -> None:
        self._client = client

    @cached_property
    def access_tokens(self) -> access_tokens.AccessTokensWithRawResponse:
        from .resources.access_tokens import AccessTokensWithRawResponse

        return AccessTokensWithRawResponse(self._client.access_tokens)

    @cached_property
    def hris(self) -> hris.HRISWithRawResponse:
        from .resources.hris import HRISWithRawResponse

        return HRISWithRawResponse(self._client.hris)

    @cached_property
    def providers(self) -> providers.ProvidersWithRawResponse:
        from .resources.providers import ProvidersWithRawResponse

        return ProvidersWithRawResponse(self._client.providers)

    @cached_property
    def account(self) -> account.AccountWithRawResponse:
        from .resources.account import AccountWithRawResponse

        return AccountWithRawResponse(self._client.account)

    @cached_property
    def request_forwarding(self) -> request_forwarding.RequestForwardingWithRawResponse:
        from .resources.request_forwarding import RequestForwardingWithRawResponse

        return RequestForwardingWithRawResponse(self._client.request_forwarding)

    @cached_property
    def jobs(self) -> jobs.JobsWithRawResponse:
        from .resources.jobs import JobsWithRawResponse

        return JobsWithRawResponse(self._client.jobs)

    @cached_property
    def sandbox(self) -> sandbox.SandboxWithRawResponse:
        from .resources.sandbox import SandboxWithRawResponse

        return SandboxWithRawResponse(self._client.sandbox)

    @cached_property
    def payroll(self) -> payroll.PayrollWithRawResponse:
        from .resources.payroll import PayrollWithRawResponse

        return PayrollWithRawResponse(self._client.payroll)

    @cached_property
    def connect(self) -> connect.ConnectWithRawResponse:
        from .resources.connect import ConnectWithRawResponse

        return ConnectWithRawResponse(self._client.connect)


class AsyncFinchWithRawResponse:
    _client: AsyncFinch

    def __init__(self, client: AsyncFinch) -> None:
        self._client = client

    @cached_property
    def access_tokens(self) -> access_tokens.AsyncAccessTokensWithRawResponse:
        from .resources.access_tokens import AsyncAccessTokensWithRawResponse

        return AsyncAccessTokensWithRawResponse(self._client.access_tokens)

    @cached_property
    def hris(self) -> hris.AsyncHRISWithRawResponse:
        from .resources.hris import AsyncHRISWithRawResponse

        return AsyncHRISWithRawResponse(self._client.hris)

    @cached_property
    def providers(self) -> providers.AsyncProvidersWithRawResponse:
        from .resources.providers import AsyncProvidersWithRawResponse

        return AsyncProvidersWithRawResponse(self._client.providers)

    @cached_property
    def account(self) -> account.AsyncAccountWithRawResponse:
        from .resources.account import AsyncAccountWithRawResponse

        return AsyncAccountWithRawResponse(self._client.account)

    @cached_property
    def request_forwarding(self) -> request_forwarding.AsyncRequestForwardingWithRawResponse:
        from .resources.request_forwarding import AsyncRequestForwardingWithRawResponse

        return AsyncRequestForwardingWithRawResponse(self._client.request_forwarding)

    @cached_property
    def jobs(self) -> jobs.AsyncJobsWithRawResponse:
        from .resources.jobs import AsyncJobsWithRawResponse

        return AsyncJobsWithRawResponse(self._client.jobs)

    @cached_property
    def sandbox(self) -> sandbox.AsyncSandboxWithRawResponse:
        from .resources.sandbox import AsyncSandboxWithRawResponse

        return AsyncSandboxWithRawResponse(self._client.sandbox)

    @cached_property
    def payroll(self) -> payroll.AsyncPayrollWithRawResponse:
        from .resources.payroll import AsyncPayrollWithRawResponse

        return AsyncPayrollWithRawResponse(self._client.payroll)

    @cached_property
    def connect(self) -> connect.AsyncConnectWithRawResponse:
        from .resources.connect import AsyncConnectWithRawResponse

        return AsyncConnectWithRawResponse(self._client.connect)


class FinchWithStreamedResponse:
    _client: Finch

    def __init__(self, client: Finch) -> None:
        self._client = client

    @cached_property
    def access_tokens(self) -> access_tokens.AccessTokensWithStreamingResponse:
        from .resources.access_tokens import AccessTokensWithStreamingResponse

        return AccessTokensWithStreamingResponse(self._client.access_tokens)

    @cached_property
    def hris(self) -> hris.HRISWithStreamingResponse:
        from .resources.hris import HRISWithStreamingResponse

        return HRISWithStreamingResponse(self._client.hris)

    @cached_property
    def providers(self) -> providers.ProvidersWithStreamingResponse:
        from .resources.providers import ProvidersWithStreamingResponse

        return ProvidersWithStreamingResponse(self._client.providers)

    @cached_property
    def account(self) -> account.AccountWithStreamingResponse:
        from .resources.account import AccountWithStreamingResponse

        return AccountWithStreamingResponse(self._client.account)

    @cached_property
    def request_forwarding(self) -> request_forwarding.RequestForwardingWithStreamingResponse:
        from .resources.request_forwarding import RequestForwardingWithStreamingResponse

        return RequestForwardingWithStreamingResponse(self._client.request_forwarding)

    @cached_property
    def jobs(self) -> jobs.JobsWithStreamingResponse:
        from .resources.jobs import JobsWithStreamingResponse

        return JobsWithStreamingResponse(self._client.jobs)

    @cached_property
    def sandbox(self) -> sandbox.SandboxWithStreamingResponse:
        from .resources.sandbox import SandboxWithStreamingResponse

        return SandboxWithStreamingResponse(self._client.sandbox)

    @cached_property
    def payroll(self) -> payroll.PayrollWithStreamingResponse:
        from .resources.payroll import PayrollWithStreamingResponse

        return PayrollWithStreamingResponse(self._client.payroll)

    @cached_property
    def connect(self) -> connect.ConnectWithStreamingResponse:
        from .resources.connect import ConnectWithStreamingResponse

        return ConnectWithStreamingResponse(self._client.connect)


class AsyncFinchWithStreamedResponse:
    _client: AsyncFinch

    def __init__(self, client: AsyncFinch) -> None:
        self._client = client

    @cached_property
    def access_tokens(self) -> access_tokens.AsyncAccessTokensWithStreamingResponse:
        from .resources.access_tokens import AsyncAccessTokensWithStreamingResponse

        return AsyncAccessTokensWithStreamingResponse(self._client.access_tokens)

    @cached_property
    def hris(self) -> hris.AsyncHRISWithStreamingResponse:
        from .resources.hris import AsyncHRISWithStreamingResponse

        return AsyncHRISWithStreamingResponse(self._client.hris)

    @cached_property
    def providers(self) -> providers.AsyncProvidersWithStreamingResponse:
        from .resources.providers import AsyncProvidersWithStreamingResponse

        return AsyncProvidersWithStreamingResponse(self._client.providers)

    @cached_property
    def account(self) -> account.AsyncAccountWithStreamingResponse:
        from .resources.account import AsyncAccountWithStreamingResponse

        return AsyncAccountWithStreamingResponse(self._client.account)

    @cached_property
    def request_forwarding(self) -> request_forwarding.AsyncRequestForwardingWithStreamingResponse:
        from .resources.request_forwarding import AsyncRequestForwardingWithStreamingResponse

        return AsyncRequestForwardingWithStreamingResponse(self._client.request_forwarding)

    @cached_property
    def jobs(self) -> jobs.AsyncJobsWithStreamingResponse:
        from .resources.jobs import AsyncJobsWithStreamingResponse

        return AsyncJobsWithStreamingResponse(self._client.jobs)

    @cached_property
    def sandbox(self) -> sandbox.AsyncSandboxWithStreamingResponse:
        from .resources.sandbox import AsyncSandboxWithStreamingResponse

        return AsyncSandboxWithStreamingResponse(self._client.sandbox)

    @cached_property
    def payroll(self) -> payroll.AsyncPayrollWithStreamingResponse:
        from .resources.payroll import AsyncPayrollWithStreamingResponse

        return AsyncPayrollWithStreamingResponse(self._client.payroll)

    @cached_property
    def connect(self) -> connect.AsyncConnectWithStreamingResponse:
        from .resources.connect import AsyncConnectWithStreamingResponse

        return AsyncConnectWithStreamingResponse(self._client.connect)


Client = Finch

AsyncClient = AsyncFinch
