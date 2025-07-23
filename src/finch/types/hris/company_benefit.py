# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .benefit_type import BenefitType
from .benefit_frequency import BenefitFrequency

__all__ = ["CompanyBenefit", "CompanyContribution", "CompanyContributionTier"]


class CompanyContributionTier(BaseModel):
    match: int

    threshold: int


class CompanyContribution(BaseModel):
    tiers: List[CompanyContributionTier]

    type: Literal["match"]


class CompanyBenefit(BaseModel):
    benefit_id: str
    """The id of the benefit."""

    description: Optional[str] = None

    frequency: Optional[BenefitFrequency] = None
    """The frequency of the benefit deduction/contribution."""

    type: Optional[BenefitType] = None
    """Type of benefit."""

    company_contribution: Optional[CompanyContribution] = None
    """The company match for this benefit."""
