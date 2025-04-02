# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .benefit_type import BenefitType
from .benefit_frequency import BenefitFrequency

__all__ = ["BenefitCreateParams"]


class BenefitCreateParams(TypedDict, total=False):
    description: str
    """Name of the benefit as it appears in the provider and pay statements.

    Recommend limiting this to <30 characters due to limitations in specific
    providers (e.g. Justworks).
    """

    frequency: Optional[BenefitFrequency]
    """The frequency of the benefit deduction/contribution."""

    type: Optional[BenefitType]
    """Type of benefit."""
