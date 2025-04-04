# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["IndividualEnrolledIDsResponse"]


class IndividualEnrolledIDsResponse(BaseModel):
    benefit_id: str
    """The id of the benefit."""

    individual_ids: List[str]
