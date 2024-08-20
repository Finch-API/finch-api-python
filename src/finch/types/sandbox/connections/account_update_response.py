# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AccountUpdateResponse"]


class AccountUpdateResponse(BaseModel):
    account_id: str

    authentication_type: Literal["credential", "api_token", "oauth", "assisted"]

    company_id: str

    products: List[str]

    provider_id: str
