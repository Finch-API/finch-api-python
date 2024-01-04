# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel
from .benefit_type import BenefitType
from .benefit_frequency import BenefitFrequency
from .benefit_contribution import BenefitContribution

__all__ = ["CompanyBenefit"]


class CompanyBenefit(BaseModel):
    benefit_id: str

    company_contribution: Optional[BenefitContribution] = None

    description: Optional[str] = None

    employee_deduction: Optional[BenefitContribution] = None

    frequency: Optional[BenefitFrequency] = None

    type: Optional[BenefitType] = None
    """Type of benefit."""
