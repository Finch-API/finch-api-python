# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Provider"]


class Provider(BaseModel):
    id: Optional[str]
    """The id of the payroll provider used in Connect."""

    display_name: Optional[str]
    """The display name of the payroll provider."""

    icon: Optional[str]
    """The url to the official icon of the payroll provider."""

    logo: Optional[str]
    """The url to the official logo of the payroll provider."""

    manual: Optional[bool]
    """
    Whether the Finch integration with this provider uses the Assisted Connect Flow
    by default.
    """

    mfa_required: Optional[bool]
    """whether MFA is required for the provider."""

    primary_color: Optional[str]
    """The hex code for the primary color of the payroll provider."""

    products: Optional[List[str]]
    """The list of Finch products supported on this payroll provider."""
