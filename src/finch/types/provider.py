# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Provider"]


class Provider(BaseModel):
    id: Optional[str] = None
    """The id of the payroll provider used in Connect."""

    display_name: Optional[str] = None
    """The display name of the payroll provider."""

    icon: Optional[str] = None
    """The url to the official icon of the payroll provider."""

    logo: Optional[str] = None
    """The url to the official logo of the payroll provider."""

    manual: Optional[bool] = None
    """
    Whether the Finch integration with this provider uses the Assisted Connect Flow
    by default.
    """

    mfa_required: Optional[bool] = None
    """whether MFA is required for the provider."""

    primary_color: Optional[str] = None
    """The hex code for the primary color of the payroll provider."""

    products: Optional[List[str]] = None
    """The list of Finch products supported on this payroll provider."""
