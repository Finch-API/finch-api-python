# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .individual import Individual

__all__ = ["IndividualResponse"]


class IndividualResponse(BaseModel):
    body: Individual

    code: int

    individual_id: str
