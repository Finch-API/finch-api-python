# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["Location"]


class Location(BaseModel):
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
