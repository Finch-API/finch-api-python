# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ConnectionCreateResponse"]


class ConnectionCreateResponse(BaseModel):
    access_token: str

    account_id: str

    authentication_type: Literal["api_token", "assisted", "credential", "oauth"]

    connection_id: str

    entity_id: str

    products: List[str]

    provider_id: str

    token_type: str

    company_id: Optional[str] = None
