# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel
from ...types.hris import benefit_type, benefit_frequency, benfit_contribution

__all__ = ["CompanyBenefit"]


class CompanyBenefit(BaseModel):
    benefit_id: str

    company_contribution: Optional[benfit_contribution.BenfitContribution]

    description: Optional[str]

    employee_deduction: Optional[benfit_contribution.BenfitContribution]

    frequency: Optional[benefit_frequency.BenefitFrequency]

    type: Optional[benefit_type.BenefitType]
    """Type of benefit."""
