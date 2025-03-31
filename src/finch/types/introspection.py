# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.connection_status_type import ConnectionStatusType

__all__ = ["Introspection", "AuthenticationMethod", "AuthenticationMethodConnectionStatus", "ConnectionStatus"]


class AuthenticationMethodConnectionStatus(BaseModel):
    message: Optional[str] = None

    status: Optional[ConnectionStatusType] = None


class AuthenticationMethod(BaseModel):
    connection_status: Optional[AuthenticationMethodConnectionStatus] = None

    products: Optional[List[str]] = None
    """An array of the authorized products associated with the `access_token`."""

    type: Optional[Literal["assisted", "credential", "api_token", "api_credential", "oauth"]] = None
    """The type of authentication method."""


class ConnectionStatus(BaseModel):
    last_successful_sync: Optional[datetime] = None
    """The datetime when the connection was last successfully synced."""

    message: Optional[str] = None

    status: Optional[ConnectionStatusType] = None


class Introspection(BaseModel):
    account_id: str
    """
    [DEPRECATED] Use `connection_id` to associate tokens with a Finch connection
    instead of this account ID.
    """

    authentication_methods: List[AuthenticationMethod]

    client_id: str
    """The client ID of the application associated with the `access_token`."""

    client_type: Literal["production", "development", "sandbox"]
    """The type of application associated with a token."""

    company_id: str
    """
    [DEPRECATED] Use `connection_id` to associate tokens with a Finch connection
    instead of this company ID.
    """

    connection_id: str
    """The Finch UUID of the connection associated with the `access_token`."""

    connection_status: ConnectionStatus

    connection_type: Literal["provider", "finch"]
    """The type of the connection associated with the token.

    - `provider` - connection to an external provider
    - `finch` - finch-generated data.
    """

    customer_email: Optional[str] = None
    """
    The email of your customer you provided to Finch when a connect session was
    created for this connection.
    """

    customer_id: Optional[str] = None
    """
    The ID of your customer you provided to Finch when a connect session was created
    for this connection.
    """

    customer_name: Optional[str] = None
    """
    The name of your customer you provided to Finch when a connect session was
    created for this connection.
    """

    manual: bool
    """
    Whether the connection associated with the `access_token` uses the Assisted
    Connect Flow. (`true` if using Assisted Connect, `false` if connection is
    automated)
    """

    payroll_provider_id: str
    """
    [DEPRECATED] Use `provider_id` to identify the provider instead of this payroll
    provider ID.
    """

    products: List[str]
    """An array of the authorized products associated with the `access_token`."""

    provider_id: str
    """The ID of the provider associated with the `access_token`."""

    username: str
    """The account username used for login associated with the `access_token`."""
