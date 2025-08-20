# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreateAccessTokenResponse"]


class CreateAccessTokenResponse(BaseModel):
    access_token: str
    """The access token for the connection"""

    client_type: Literal["development", "production", "sandbox"]
    """The type of application associated with a token."""

    connection_id: str
    """The Finch UUID of the connection associated with the `access_token`"""

    connection_type: Literal["finch", "provider"]
    """The type of the connection associated with the token.

    - `provider` - connection to an external provider
    - `finch` - finch-generated data.
    """

    products: List[str]
    """An array of the authorized products associated with the `access_token`"""

    provider_id: str
    """The ID of the provider associated with the `access_token`"""

    token_type: str
    """The RFC 8693 token type (Finch uses `bearer` tokens)"""

    account_id: Optional[str] = None
    """
    [DEPRECATED] Use `connection_id` to identify the connection instead of this
    account ID
    """

    company_id: Optional[str] = None
    """
    [DEPRECATED] Use `connection_id` to identify the connection instead of this
    company ID
    """

    customer_id: Optional[str] = None
    """
    The ID of your customer you provided to Finch when a connect session was created
    for this connection
    """
