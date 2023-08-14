# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel
from .benefit_type import BenefitType
from .benefit_frequency import BenefitFrequency
from .benfit_contribution import BenfitContribution

__all__ = ["CompanyBenefit"]


class CompanyBenefit(BaseModel):
    benefit_id: str

    company_contribution: Optional[BenfitContribution]

    description: Optional[str]

    employee_deduction: Optional[BenfitContribution]

    frequency: Optional[BenefitFrequency]

    type: Optional[BenefitType]
    """Type of benefit."""
