# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Location"]


class Location(BaseModel):
    city: Optional[str] = None
    """City, district, suburb, town, or village."""

    country: Optional[str] = None
    """The 2-letter ISO 3166 country code."""

    line1: Optional[str] = None
    """Street address or PO box."""

    line2: Optional[str] = None
    """Apartment, suite, unit, or building."""

    name: Optional[str] = None

    postal_code: Optional[str] = None
    """The postal code or zip code."""

    source_id: Optional[str] = None

    state: Optional[str] = None
    """The state code."""
