# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConnectionCreateParams"]


class ConnectionCreateParams(TypedDict, total=False):
    provider_id: Required[str]

    authentication_type: Literal["credential", "api_token", "oauth", "assisted"]

    employee_size: int
    """Optional: the size of the employer to be created with this connection.

    Defaults to 20
    """

    products: List[str]
