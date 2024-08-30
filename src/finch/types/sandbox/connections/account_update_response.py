# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AccountUpdateResponse"]


class AccountUpdateResponse(BaseModel):
    account_id: str
    """[DEPRECATED] Use `connection_id` to associate a connection with an access token"""

    authentication_type: Literal["credential", "api_token", "oauth", "assisted"]

    company_id: str
    """[DEPRECATED] Use `connection_id` to associate a connection with an access token"""

    products: List[str]

    provider_id: str
    """The ID of the provider associated with the `access_token`"""

    connection_id: Optional[str] = None
    """The ID of the new connection"""
