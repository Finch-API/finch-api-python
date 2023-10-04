# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BenefitContribution"]


class BenefitContribution(BaseModel):
    amount: Optional[int] = None
    """Contribution amount in cents (if `fixed`) or basis points (if `percent`)."""

    type: Optional[Literal["fixed", "percent"]] = None
    """Contribution type."""
