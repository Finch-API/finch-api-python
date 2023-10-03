# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..hris import BenefitType, BenefitFrequency

__all__ = ["BenefitRegisterParams"]


class BenefitRegisterParams(TypedDict, total=False):
    description: str

    frequency: Optional[BenefitFrequency]

    type: Optional[BenefitType]
    """Type of benefit."""
