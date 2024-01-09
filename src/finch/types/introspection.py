# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .shared import ConnectionStatusType
from .._models import BaseModel

__all__ = ["Introspection", "AuthenticationMethods", "AuthenticationMethodsConnectionStatus"]


class AuthenticationMethodsConnectionStatus(BaseModel):
    message: Optional[str] = None

    status: Optional[ConnectionStatusType] = None


class AuthenticationMethods(BaseModel):
    connection_status: Optional[AuthenticationMethodsConnectionStatus] = None

    type: Optional[str] = None


class Introspection(BaseModel):
    account_id: str
    """The Finch uuid of the account used to connect this company."""

    authentication_methods: AuthenticationMethods

    client_id: str
    """The client id of the application associated with the `access_token`."""

    client_type: Literal["production", "development", "sandbox"]
    """The type of application associated with a token."""

    company_id: str
    """The Finch uuid of the company associated with the `access_token`."""

    connection_type: Literal["provider", "finch"]
    """The type of the connection associated with the token.

    `provider` - connection to an external provider

    `finch` - finch-generated data.
    """

    manual: bool
    """
    Whether the connection associated with the `access_token` uses the Assisted
    Connect Flow. (`true` if using Assisted Connect, `false` if connection is
    automated)
    """

    payroll_provider_id: str
    """The payroll provider associated with the `access_token`."""

    products: List[str]
    """An array of the authorized products associated with the `access_token`."""

    username: str
    """The account username used for login associated with the `access_token`."""
