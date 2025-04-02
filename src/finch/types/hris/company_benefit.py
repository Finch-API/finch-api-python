# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .benefit_type import BenefitType
from .benefit_frequency import BenefitFrequency

__all__ = ["CompanyBenefit"]


class CompanyBenefit(BaseModel):
    benefit_id: str
    """The id of the benefit."""

    description: Optional[str] = None

    frequency: Optional[BenefitFrequency] = None
    """The frequency of the benefit deduction/contribution."""

    type: Optional[BenefitType] = None
    """Type of benefit."""
