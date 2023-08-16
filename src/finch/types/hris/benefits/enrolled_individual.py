# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["EnrolledIndividual", "Body"]


class Body(BaseModel):
    finch_code: Optional[str] = None
    """A descriptive identifier for the response"""

    message: Optional[str] = None
    """Short description in English that provides more information about the response."""

    name: Optional[str] = None
    """Identifier indicating whether the benefit was newly enrolled or updated."""


class EnrolledIndividual(BaseModel):
    body: Optional[Body] = None

    code: Optional[Literal[200, 201, 404, 403]] = None
    """HTTP status code. Either 201 or 200"""

    individual_id: Optional[str] = None
