# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from ..benefit_contribution import BenefitContribution

__all__ = ["IndividualBenefit", "Body", "BodyUnionMember0", "BodyBatchError"]


class BodyUnionMember0(BaseModel):
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


class BodyBatchError(BaseModel):
    code: float

    message: str

    name: str

    finch_code: Optional[str] = None


Body: TypeAlias = Union[BodyUnionMember0, BodyBatchError]


class IndividualBenefit(BaseModel):
    body: Body

    code: int

    individual_id: str
