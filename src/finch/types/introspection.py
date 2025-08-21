# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.connection_status_type import ConnectionStatusType

__all__ = ["Introspection", "ConnectionStatus", "AuthenticationMethod", "AuthenticationMethodConnectionStatus"]


class ConnectionStatus(BaseModel):
    status: ConnectionStatusType

    last_successful_sync: Union[datetime, str, None] = None
    """The datetime when the connection was last successfully synced"""

    message: Optional[str] = None


class AuthenticationMethodConnectionStatus(BaseModel):
    status: ConnectionStatusType

    last_successful_sync: Union[datetime, str, None] = None
    """The datetime when the connection was last successfully synced"""

    message: Optional[str] = None


class AuthenticationMethod(BaseModel):
    type: Literal["assisted", "credential", "api_token", "api_credential", "oauth"]
    """The type of authentication method"""

    connection_status: Optional[AuthenticationMethodConnectionStatus] = None

    products: Optional[List[str]] = None
    """An array of the authorized products associated with the `access_token`"""


class Introspection(BaseModel):
    id: str
    """The Finch UUID of the token being introspected"""

    client_id: str
    """The client ID of the application associated with the `access_token`"""

    client_type: Literal["development", "production", "sandbox"]
    """The type of application associated with a token."""

    connection_id: str
    """The Finch UUID of the connection associated with the `access_token`"""

    connection_status: ConnectionStatus

    connection_type: Literal["finch", "provider"]
    """The type of the connection associated with the token.

    - `provider` - connection to an external provider
    - `finch` - finch-generated data.
    """

    products: List[str]
    """An array of the authorized products associated with the `access_token`."""

    provider_id: str
    """The ID of the provider associated with the `access_token`."""

    account_id: Optional[str] = None
    """
    [DEPRECATED] Use `connection_id` to associate tokens with a Finch connection
    instead of this account ID
    """

    authentication_methods: Optional[List[AuthenticationMethod]] = None

    company_id: Optional[str] = None
    """
    [DEPRECATED] Use `connection_id` to associate tokens with a Finch connection
    instead of this company ID
    """

    customer_email: Optional[str] = None
    """
    The email of your customer you provided to Finch when a connect session was
    created for this connection
    """

    customer_id: Optional[str] = None
    """
    The ID of your customer you provided to Finch when a connect session was created
    for this connection
    """

    customer_name: Optional[str] = None
    """
    The name of your customer you provided to Finch when a connect session was
    created for this connection
    """

    entity_ids: Optional[List[str]] = None
    """Array of entity IDs associated with this connection."""

    entity_mode: Optional[Literal["single", "multi"]] = None
    """Indicates whether this connection manages a single entity or multiple entities."""

    manual: Optional[bool] = None
    """
    Whether the connection associated with the `access_token` uses the Assisted
    Connect Flow. (`true` if using Assisted Connect, `false` if connection is
    automated)
    """

    payroll_provider_id: Optional[str] = None
    """
    [DEPRECATED] Use `provider_id` to identify the provider instead of this payroll
    provider ID.
    """

    username: Optional[str] = None
    """The account username used for login associated with the `access_token`."""
