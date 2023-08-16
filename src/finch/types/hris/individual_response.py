# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel
from .individual import Individual

__all__ = ["IndividualResponse"]


class IndividualResponse(BaseModel):
    body: Optional[Individual] = None

    code: Optional[int] = None

    individual_id: Optional[str] = None
