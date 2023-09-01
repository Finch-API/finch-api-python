# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .benefit_type import BenefitType
from .benefit_frequency import BenefitFrequency

__all__ = ["BenefitCreateParams"]


class BenefitCreateParams(TypedDict, total=False):
    description: str

    frequency: Optional[BenefitFrequency]

    type: Optional[BenefitType]
    """Type of benefit."""
