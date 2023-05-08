# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel
from ...types.hris import individual

__all__ = ["IndividualResponse"]


class IndividualResponse(BaseModel):
    body: Optional[individual.Individual]

    code: Optional[int]

    individual_id: Optional[str]
