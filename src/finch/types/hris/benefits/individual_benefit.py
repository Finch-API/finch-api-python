# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "IndividualBenefit",
    "Body",
    "BodyUnionMember0",
    "BodyUnionMember0CompanyContribution",
    "BodyUnionMember0CompanyContributionUnionMember0",
    "BodyUnionMember0CompanyContributionUnionMember1",
    "BodyUnionMember0CompanyContributionUnionMember2",
    "BodyUnionMember0CompanyContributionUnionMember2Tier",
    "BodyUnionMember0EmployeeDeduction",
    "BodyUnionMember0EmployeeDeductionUnionMember0",
    "BodyUnionMember0EmployeeDeductionUnionMember1",
    "BodyBatchError",
]


class BodyUnionMember0CompanyContributionUnionMember0(BaseModel):
    amount: int
    """Contribution amount in cents."""

    type: Literal["fixed"]
    """Fixed contribution type."""


class BodyUnionMember0CompanyContributionUnionMember1(BaseModel):
    amount: int
    """Contribution amount in basis points (1/100th of a percent)."""

    type: Literal["percent"]
    """Percentage contribution type."""


class BodyUnionMember0CompanyContributionUnionMember2Tier(BaseModel):
    match: int

    threshold: int


class BodyUnionMember0CompanyContributionUnionMember2(BaseModel):
    tiers: List[BodyUnionMember0CompanyContributionUnionMember2Tier]
    """
    Array of tier objects defining employer match tiers based on employee
    contribution thresholds.
    """

    type: Literal["tiered"]
    """Tiered contribution type (only valid for company_contribution)."""


BodyUnionMember0CompanyContribution: TypeAlias = Union[
    BodyUnionMember0CompanyContributionUnionMember0,
    BodyUnionMember0CompanyContributionUnionMember1,
    BodyUnionMember0CompanyContributionUnionMember2,
    None,
]


class BodyUnionMember0EmployeeDeductionUnionMember0(BaseModel):
    amount: int
    """Contribution amount in cents."""

    type: Literal["fixed"]
    """Fixed contribution type."""


class BodyUnionMember0EmployeeDeductionUnionMember1(BaseModel):
    amount: int
    """Contribution amount in basis points (1/100th of a percent)."""

    type: Literal["percent"]
    """Percentage contribution type."""


BodyUnionMember0EmployeeDeduction: TypeAlias = Union[
    BodyUnionMember0EmployeeDeductionUnionMember0, BodyUnionMember0EmployeeDeductionUnionMember1, None
]


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

    company_contribution: Optional[BodyUnionMember0CompanyContribution] = None

    employee_deduction: Optional[BodyUnionMember0EmployeeDeduction] = None

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
