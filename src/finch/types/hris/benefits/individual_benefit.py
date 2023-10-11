# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel
from ..benefit_contribution import BenefitContribution

__all__ = ["IndividualBenefit", "Body"]


class Body(BaseModel):
    annual_maximum: Optional[int] = None
    """
    If the benefit supports annual maximum, the amount in cents for this individual.
    """

    catch_up: Optional[bool] = None
    """
    If the benefit supports catch up (401k, 403b, etc.), whether catch up is enabled
    for this individual.
    """

    company_contribution: Optional[BenefitContribution] = None

    employee_deduction: Optional[BenefitContribution] = None

    hsa_contribution_limit: Optional[Literal["individual", "family"]] = None
    """Type for HSA contribution limit if the benefit is a HSA."""


class IndividualBenefit(BaseModel):
    body: Optional[Body] = None

    code: Optional[int] = None

    individual_id: Optional[str] = None
