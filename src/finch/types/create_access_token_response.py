# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreateAccessTokenResponse"]


class CreateAccessTokenResponse(BaseModel):
    access_token: str
    """The access token for the connection."""

    account_id: str
    """
    [DEPRECATED] Use `connection_id` to identify the connection instead of this
    account ID.
    """

    client_type: Literal["production", "development", "sandbox"]
    """The type of application associated with a token."""

    company_id: str
    """
    [DEPRECATED] Use `connection_id` to identify the connection instead of this
    company ID.
    """

    connection_id: str
    """The Finch UUID of the connection associated with the `access_token`."""

    connection_type: Literal["provider", "finch"]
    """The type of the connection associated with the token.

    - `provider` - connection to an external provider
    - `finch` - finch-generated data.
    """

    products: List[str]
    """An array of the authorized products associated with the `access_token`."""

    provider_id: str
    """The ID of the provider associated with the `access_token`."""

    customer_id: Optional[str] = None
    """
    The ID of your customer you provided to Finch when a connect session was created
    for this connection.
    """

    token_type: Optional[str] = None
    """The RFC 8693 token type (Finch uses `bearer` tokens)"""
