# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SessionNewParams", "Integration"]


class SessionNewParams(TypedDict, total=False):
    customer_id: Required[str]

    customer_name: Required[str]

    products: Required[
        List[Literal["company", "directory", "individual", "employment", "payment", "pay_statement", "benefits", "ssn"]]
    ]

    customer_email: Optional[str]

    integration: Optional[Integration]

    manual: Optional[bool]

    minutes_to_expire: Optional[float]
    """
    The number of minutes until the session expires (defaults to 43,200, which is 30
    days)
    """

    redirect_uri: Optional[str]

    sandbox: Optional[Literal["finch", "provider"]]


class Integration(TypedDict, total=False):
    auth_method: Optional[Literal["assisted", "credential", "oauth", "api_token"]]

    provider: Optional[str]
