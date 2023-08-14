# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel
from ..benfit_contribution import BenfitContribution

__all__ = ["IndividualBenefit", "Body"]


class Body(BaseModel):
    annual_maximum: Optional[int]
    """
    If the benefit supports annual maximum, the amount in cents for this individual.
    """

    catch_up: Optional[bool]
    """
    If the benefit supports catch up (401k, 403b, etc.), whether catch up is enabled
    for this individual.
    """

    company_contribution: Optional[BenfitContribution]

    employee_deduction: Optional[BenfitContribution]

    hsa_contribution_limit: Optional[Literal["individual", "family"]]
    """Type for HSA contribution limit if the benefit is a HSA."""


class IndividualBenefit(BaseModel):
    body: Optional[Body]

    code: Optional[int]

    individual_id: Optional[str]
