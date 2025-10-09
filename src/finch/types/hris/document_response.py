# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DocumentResponse"]


class DocumentResponse(BaseModel):
    id: str
    """A stable Finch id for the document."""

    individual_id: Optional[str] = None
    """The ID of the individual associated with the document.

    This will be null for employer-level documents.
    """

    type: Literal["w4_2020", "w4_2005"]
    """The type of document."""

    url: str
    """A URL to access the document.

    Format: `https://api.tryfinch.com/employer/documents/:document_id`.
    """

    year: float
    """The year the document applies to, if available."""
