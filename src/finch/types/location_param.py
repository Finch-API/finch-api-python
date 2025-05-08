# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["LocationParam"]


class LocationParam(TypedDict, total=False):
    city: Required[Optional[str]]
    """City, district, suburb, town, or village."""

    country: Required[Optional[str]]
    """The 2-letter ISO 3166 country code."""

    line1: Required[Optional[str]]
    """Street address or PO box."""

    line2: Required[Optional[str]]
    """Apartment, suite, unit, or building."""

    postal_code: Required[Optional[str]]
    """The postal code or zip code."""

    state: Required[Optional[str]]
    """The state code."""

    name: Optional[str]

    source_id: Optional[str]
