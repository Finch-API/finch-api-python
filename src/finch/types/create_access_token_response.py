# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreateAccessTokenResponse"]


class CreateAccessTokenResponse(BaseModel):
    access_token: str

    account_id: str
    """The Finch uuid of the account used to connect this company."""

    client_type: Literal["production", "development", "sandbox"]
    """The type of application associated with a token."""

    company_id: str
    """The Finch uuid of the company associated with the `access_token`."""

    connection_type: Literal["provider", "finch"]
    """The type of the connection associated with the token.

    - `provider` - connection to an external provider
    - `finch` - finch-generated data.
    """

    products: List[str]
    """An array of the authorized products associated with the `access_token`."""

    provider_id: str
    """The payroll provider associated with the `access_token`."""
