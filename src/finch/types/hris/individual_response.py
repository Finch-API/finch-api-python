# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel
from .individual import Individual

__all__ = ["IndividualResponse"]


class IndividualResponse(BaseModel):
    body: Optional[Individual]

    code: Optional[int]

    individual_id: Optional[str]
