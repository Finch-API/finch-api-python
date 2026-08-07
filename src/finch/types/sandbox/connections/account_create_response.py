# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AccountCreateResponse"]


class AccountCreateResponse(BaseModel):
    access_token: str

    account_id: str
    """[DEPRECATED] Use `connection_id` to associate a connection with an access token"""

    authentication_type: Literal["api_token", "assisted", "credential", "oauth"]

    company_id: str
    """The Finch UUID of the company associated with the `access_token`."""

    connection_id: str
    """The ID of the new connection"""

    entity_id: str
    """The ID of the entity for this connection"""

    products: List[str]

    provider_id: str
    """The ID of the provider associated with the `access_token`"""
