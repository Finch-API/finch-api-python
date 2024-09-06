# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["LocationParam"]


class LocationParam(TypedDict, total=False):
    city: Optional[str]
    """City, district, suburb, town, or village."""

    country: Optional[str]
    """The 2-letter ISO 3166 country code."""

    line1: Optional[str]
    """Street address or PO box."""

    line2: Optional[str]
    """Apartment, suite, unit, or building."""

    name: Optional[str]

    postal_code: Optional[str]
    """The postal code or zip code."""

    source_id: Optional[str]

    state: Optional[str]
    """The state code."""
