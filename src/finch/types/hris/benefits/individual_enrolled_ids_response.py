# File generated from our OpenAPI spec by Stainless.

from typing import List

from ...._models import BaseModel

__all__ = ["IndividualEnrolledIDsResponse"]


class IndividualEnrolledIDsResponse(BaseModel):
    benefit_id: str

    individual_ids: List[str]
