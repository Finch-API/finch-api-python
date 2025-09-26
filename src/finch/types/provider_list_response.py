# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProviderListResponse", "AuthenticationMethod"]


class AuthenticationMethod(BaseModel):
    type: Literal["assisted", "credential", "api_token", "api_credential", "oauth", "api"]
    """The type of authentication method"""

    benefits_support: Optional[Dict[str, Optional[object]]] = None
    """The supported benefit types and their configurations"""

    supported_fields: Optional[Dict[str, Optional[object]]] = None
    """The supported fields for each Finch product"""


class ProviderListResponse(BaseModel):
    id: str
    """The id of the payroll provider used in Connect."""

    display_name: str
    """The display name of the payroll provider."""

    products: List[str]
    """The list of Finch products supported on this payroll provider."""

    authentication_methods: Optional[List[AuthenticationMethod]] = None
    """The authentication methods supported by the provider."""

    beta: Optional[bool] = None
    """`true` if the integration is in a beta state, `false` otherwise"""

    icon: Optional[str] = None
    """The url to the official icon of the payroll provider."""

    logo: Optional[str] = None
    """The url to the official logo of the payroll provider."""

    manual: Optional[bool] = None
    """
    [DEPRECATED] Whether the Finch integration with this provider uses the Assisted
    Connect Flow by default. This field is now deprecated. Please check for a `type`
    of `assisted` in the `authentication_methods` field instead.
    """

    mfa_required: Optional[bool] = None
    """whether MFA is required for the provider."""

    primary_color: Optional[str] = None
    """The hex code for the primary color of the payroll provider."""
