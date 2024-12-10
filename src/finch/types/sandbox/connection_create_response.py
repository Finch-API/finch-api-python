# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ConnectionCreateResponse"]


class ConnectionCreateResponse(BaseModel):
    access_token: str

    account_id: str
    """[DEPRECATED] Use `connection_id` to associate a connection with an access token"""

    authentication_type: Literal["credential", "api_token", "oauth", "assisted"]

    company_id: str
    """[DEPRECATED] Use `connection_id` to associate a connection with an access token"""

    connection_id: str
    """The ID of the new connection"""

    products: List[str]

    provider_id: str
    """The ID of the provider associated with the `access_token`."""

    token_type: Optional[str] = None
