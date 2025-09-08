# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccessTokenCreateParams"]


class AccessTokenCreateParams(TypedDict, total=False):
    code: Required[str]
    """The authorization code received from the authorization server"""

    client_id: str
    """The client ID for your application"""

    client_secret: str
    """The client secret for your application"""

    redirect_uri: str
    """The redirect URI used in the authorization request (optional)"""
