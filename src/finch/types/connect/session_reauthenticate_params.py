# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SessionReauthenticateParams"]


class SessionReauthenticateParams(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of the existing connection to reauthenticate"""

    minutes_to_expire: Optional[int]
    """
    The number of minutes until the session expires (defaults to 43,200, which is 30
    days)
    """

    products: Optional[
        List[Literal["company", "directory", "individual", "employment", "payment", "pay_statement", "benefits", "ssn"]]
    ]
    """The products to request access to (optional for reauthentication)"""

    redirect_uri: Optional[str]
    """The URI to redirect to after the Connect flow is completed"""
