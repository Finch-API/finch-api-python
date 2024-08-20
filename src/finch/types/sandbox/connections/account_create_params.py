# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountCreateParams"]


class AccountCreateParams(TypedDict, total=False):
    company_id: Required[str]

    provider_id: Required[str]

    authentication_type: Literal["credential", "api_token", "oauth", "assisted"]

    products: List[str]
    """
    Optional, defaults to Organization products (`company`, `directory`,
    `employment`, `individual`)
    """
