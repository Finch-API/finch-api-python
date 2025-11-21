# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SessionNewParams", "Integration"]


class SessionNewParams(TypedDict, total=False):
    customer_id: Required[str]
    """Unique identifier for the customer"""

    customer_name: Required[str]
    """Name of the customer"""

    products: Required[
        List[
            Literal[
                "benefits",
                "company",
                "deduction",
                "directory",
                "documents",
                "employment",
                "individual",
                "payment",
                "pay_statement",
                "ssn",
            ]
        ]
    ]
    """The Finch products to request access to"""

    customer_email: Optional[str]
    """Email address of the customer"""

    integration: Optional[Integration]
    """Integration configuration for the connect session"""

    manual: Optional[bool]
    """Enable manual authentication mode"""

    minutes_to_expire: Optional[float]
    """
    The number of minutes until the session expires (defaults to 129,600, which is
    90 days)
    """

    redirect_uri: Optional[str]
    """The URI to redirect to after the Connect flow is completed"""

    sandbox: Optional[Literal["finch", "provider"]]
    """Sandbox mode for testing"""


class Integration(TypedDict, total=False):
    provider: Required[str]
    """The provider to integrate with"""

    auth_method: Optional[Literal["assisted", "credential", "oauth", "api_token"]]
    """The authentication method to use"""
