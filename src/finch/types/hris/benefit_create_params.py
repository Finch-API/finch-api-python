# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from .benefit_type import BenefitType
from .benefit_frequency import BenefitFrequency

__all__ = ["BenefitCreateParams"]


class BenefitCreateParams(TypedDict, total=False):
    description: str

    frequency: BenefitFrequency

    type: BenefitType
    """Type of benefit."""
