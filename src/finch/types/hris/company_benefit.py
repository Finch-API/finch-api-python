# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel
from .benefit_type import BenefitType
from .benefit_frequency import BenefitFrequency
from .benefit_contribution import BenefitContribution

__all__ = ["CompanyBenefit"]


class CompanyBenefit(BaseModel):
    benefit_id: str

    company_contribution: Optional[BenefitContribution]

    description: Optional[str]

    employee_deduction: Optional[BenefitContribution]

    frequency: Optional[BenefitFrequency]

    type: Optional[BenefitType]
    """Type of benefit."""
