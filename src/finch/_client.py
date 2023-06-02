# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Union, Mapping, Optional

import httpx

from . import resources
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
from ._version import __version__
from ._streaming import Stream as Stream
from ._streaming import AsyncStream as AsyncStream
from ._base_client import (
    DEFAULT_LIMITS,
    DEFAULT_TIMEOUT,
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
    ats: resources.ATS
    hris: resources.HRIS
    providers: resources.Providers
    account: resources.Account

    # client options
    access_token: str | None
    client_id: str | None
    client_secret: str | None

    def __init__(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        base_url: Optional[str] = None,
        access_token: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = DEFAULT_LIMITS,
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
        """

        if base_url is None:
            base_url = "https://api.tryfinch.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.access_token = access_token

        client_id_envvar = os.environ.get("FINCH_CLIENT_ID", None)
        self.client_id = client_id or client_id_envvar or None

        client_secret_envvar = os.environ.get("FINCH_CLIENT_SECRET", None)
        self.client_secret = client_secret or client_secret_envvar or None

        self.ats = resources.ATS(self)
        self.hris = resources.HRIS(self)
        self.providers = resources.Providers(self)
        self.account = resources.Account(self)

    @property
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    def auth_headers(self) -> dict[str, str]:
        access_token = self.access_token
        if access_token is None:
            return {}
        return {"Authorization": f"Bearer {access_token}"}

    @property
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "Finch-API-Version": "2020-09-17",
            **self._custom_headers,
        }

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
        client_id: str | None = None,
        client_secret: str | None = None,
        access_token: str | None = None,
        base_url: str | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        connection_pool_limits: httpx.Limits | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
    ) -> Finch:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.

        It should be noted that this does not share the underlying httpx client class which may lead
        to performance issues.
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

        # TODO: share the same httpx client between instances
        return self.__class__(
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            base_url=base_url or str(self.base_url),
            access_token=access_token or self.access_token,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            connection_pool_limits=self._limits
            if isinstance(connection_pool_limits, NotGiven)
            else connection_pool_limits,
            max_retries=self.max_retries if isinstance(max_retries, NotGiven) else max_retries,
            default_headers=headers,
            default_query=params,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

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
        authorization code from Finch. The autorization code can then be exchanged for
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


class AsyncFinch(AsyncAPIClient):
    ats: resources.AsyncATS
    hris: resources.AsyncHRIS
    providers: resources.AsyncProviders
    account: resources.AsyncAccount

    # client options
    access_token: str | None
    client_id: str | None
    client_secret: str | None

    def __init__(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        base_url: Optional[str] = None,
        access_token: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = DEFAULT_LIMITS,
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
        """

        if base_url is None:
            base_url = "https://api.tryfinch.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.access_token = access_token

        client_id_envvar = os.environ.get("FINCH_CLIENT_ID", None)
        self.client_id = client_id or client_id_envvar or None

        client_secret_envvar = os.environ.get("FINCH_CLIENT_SECRET", None)
        self.client_secret = client_secret or client_secret_envvar or None

        self.ats = resources.AsyncATS(self)
        self.hris = resources.AsyncHRIS(self)
        self.providers = resources.AsyncProviders(self)
        self.account = resources.AsyncAccount(self)

    @property
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    def auth_headers(self) -> dict[str, str]:
        access_token = self.access_token
        if access_token is None:
            return {}
        return {"Authorization": f"Bearer {access_token}"}

    @property
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "Finch-API-Version": "2020-09-17",
            **self._custom_headers,
        }

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
        client_id: str | None = None,
        client_secret: str | None = None,
        access_token: str | None = None,
        base_url: str | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        connection_pool_limits: httpx.Limits | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
    ) -> AsyncFinch:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.

        It should be noted that this does not share the underlying httpx client class which may lead
        to performance issues.
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

        # TODO: share the same httpx client between instances
        return self.__class__(
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            base_url=base_url or str(self.base_url),
            access_token=access_token or self.access_token,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            connection_pool_limits=self._limits
            if isinstance(connection_pool_limits, NotGiven)
            else connection_pool_limits,
            max_retries=self.max_retries if isinstance(max_retries, NotGiven) else max_retries,
            default_headers=headers,
            default_query=params,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

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
        authorization code from Finch. The autorization code can then be exchanged for
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


Client = Finch

AsyncClient = AsyncFinch
