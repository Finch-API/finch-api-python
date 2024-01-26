# File generated from our OpenAPI spec by Stainless.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ConnectionCreateResponse"]


class ConnectionCreateResponse(BaseModel):
    access_token: str

    account_id: str

    authentication_type: Literal["credential", "api_token", "oauth", "assisted"]

    company_id: str

    products: List[str]

    provider_id: str
