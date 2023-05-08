# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel

__all__ = ["UnenrolledIndividual", "Body"]


class Body(BaseModel):
    finch_code: Optional[str]
    """A descriptive identifier for the response."""

    message: Optional[str]
    """Short description in English that provides more information about the response."""

    name: Optional[str]
    """Identifier indicating whether the benefit was newly enrolled or updated."""


class UnenrolledIndividual(BaseModel):
    body: Optional[Body]

    code: Optional[int]
    """HTTP status code"""

    individual_id: Optional[str]
