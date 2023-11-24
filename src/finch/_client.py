# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
import asyncio
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
    AsyncTransport,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from ._streaming import Stream as Stream
from ._streaming import AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_LIMITS,
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
    hris: resources.HRIS
    providers: resources.Providers
    account: resources.Account
    webhooks: resources.Webhooks
    request_forwarding: resources.RequestForwarding
    with_raw_response: FinchWithRawResponse

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
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Transport | None = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: ProxiesTypes | None = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = None,
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
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.hris = resources.HRIS(self)
        self.providers = resources.Providers(self)
        self.account = resources.Account(self)
        self.webhooks = resources.Webhooks(self)
        self.request_forwarding = resources.RequestForwarding(self)
        self.with_raw_response = FinchWithRawResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        access_token = self.access_token
        if access_token is None:
            return {}
        return {"Authorization": f"Bearer {access_token}"}

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

        raise TypeError(
            '"Could not resolve authentication method. Expected the access_token to be set. Or for the `Authorization` headers to be explicitly omitted"'
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
        connection_pool_limits: httpx.Limits | None = None,
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

        if connection_pool_limits is not None:
            if http_client is not None:
                raise ValueError("The 'http_client' argument is mutually exclusive with 'connection_pool_limits'")

            if self._has_custom_http_client:
                raise ValueError(
                    "A custom HTTP client has been set and is mutually exclusive with the 'connection_pool_limits' argument"
                )

            http_client = None
        else:
            if self._limits is not DEFAULT_LIMITS:
                connection_pool_limits = self._limits
            else:
                connection_pool_limits = None

            http_client = http_client or self._client

        return self.__class__(
            access_token=access_token or self.access_token,
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or str(self.base_url),
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            connection_pool_limits=connection_pool_limits,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def __del__(self) -> None:
        if not hasattr(self, "_has_custom_http_client") or not hasattr(self, "close"):
            # this can happen if the '__init__' method raised an error
            return

        if self._has_custom_http_client:
            return

        self.close()

    def get_access_token(
        self,
        code: str,
        *,
        redirect_uri: str,
    ) -> str:
        """Returns an access token for the Finch API given an authorization code.

        An
        authorization code can be obtained by visiting the url returned by
        get_auth_url().
        """
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
    hris: resources.AsyncHRIS
    providers: resources.AsyncProviders
    account: resources.AsyncAccount
    webhooks: resources.AsyncWebhooks
    request_forwarding: resources.AsyncRequestForwarding
    with_raw_response: AsyncFinchWithRawResponse

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
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: AsyncTransport | None = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: ProxiesTypes | None = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = None,
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
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.hris = resources.AsyncHRIS(self)
        self.providers = resources.AsyncProviders(self)
        self.account = resources.AsyncAccount(self)
        self.webhooks = resources.AsyncWebhooks(self)
        self.request_forwarding = resources.AsyncRequestForwarding(self)
        self.with_raw_response = AsyncFinchWithRawResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        access_token = self.access_token
        if access_token is None:
            return {}
        return {"Authorization": f"Bearer {access_token}"}

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

        raise TypeError(
            '"Could not resolve authentication method. Expected the access_token to be set. Or for the `Authorization` headers to be explicitly omitted"'
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
        connection_pool_limits: httpx.Limits | None = None,
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

        if connection_pool_limits is not None:
            if http_client is not None:
                raise ValueError("The 'http_client' argument is mutually exclusive with 'connection_pool_limits'")

            if self._has_custom_http_client:
                raise ValueError(
                    "A custom HTTP client has been set and is mutually exclusive with the 'connection_pool_limits' argument"
                )

            http_client = None
        else:
            if self._limits is not DEFAULT_LIMITS:
                connection_pool_limits = self._limits
            else:
                connection_pool_limits = None

            http_client = http_client or self._client

        return self.__class__(
            access_token=access_token or self.access_token,
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or str(self.base_url),
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            connection_pool_limits=connection_pool_limits,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def __del__(self) -> None:
        if not hasattr(self, "_has_custom_http_client") or not hasattr(self, "close"):
            # this can happen if the '__init__' method raised an error
            return

        if self._has_custom_http_client:
            return

        try:
            asyncio.get_running_loop().create_task(self.close())
        except Exception:
            pass

    async def get_access_token(
        self,
        code: str,
        *,
        redirect_uri: str,
    ) -> str:
        """Returns an access token for the Finch API given an authorization code.

        An
        authorization code can be obtained by visiting the url returned by
        get_auth_url().
        """
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
        self.hris = resources.HRISWithRawResponse(client.hris)
        self.providers = resources.ProvidersWithRawResponse(client.providers)
        self.account = resources.AccountWithRawResponse(client.account)
        self.request_forwarding = resources.RequestForwardingWithRawResponse(client.request_forwarding)


class AsyncFinchWithRawResponse:
    def __init__(self, client: AsyncFinch) -> None:
        self.hris = resources.AsyncHRISWithRawResponse(client.hris)
        self.providers = resources.AsyncProvidersWithRawResponse(client.providers)
        self.account = resources.AsyncAccountWithRawResponse(client.account)
        self.request_forwarding = resources.AsyncRequestForwardingWithRawResponse(client.request_forwarding)


Client = Finch

AsyncClient = AsyncFinch
