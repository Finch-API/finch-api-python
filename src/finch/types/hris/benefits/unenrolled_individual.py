# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["UnenrolledIndividual", "Body"]


class Body(BaseModel):
    finch_code: Optional[str] = None
    """A descriptive identifier for the response."""

    message: Optional[str] = None
    """Short description in English that provides more information about the response."""

    name: Optional[str] = None
    """Identifier indicating whether the benefit was newly enrolled or updated."""


class UnenrolledIndividual(BaseModel):
    body: Optional[Body] = None

    code: Optional[int] = None
    """HTTP status code"""

    individual_id: Optional[str] = None
