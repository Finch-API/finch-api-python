# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .benefit_type import BenefitType
from .benefit_frequency import BenefitFrequency

__all__ = ["CompanyBenefit"]


class CompanyBenefit(BaseModel):
    benefit_id: str

    description: Optional[str] = None

    frequency: Optional[BenefitFrequency] = None

    type: Optional[BenefitType] = None
    """Type of benefit."""
