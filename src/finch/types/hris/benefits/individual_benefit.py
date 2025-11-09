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
    """
    Contribution amount in cents (for type=fixed) or basis points (for type=percent,
    where 100 = 1%). Not used for type=tiered.
    """

    type: Literal["fixed"]
    """Contribution type.

    Supported values: "fixed" (amount in cents), "percent" (amount in basis points),
    or "tiered" (multi-tier matching).
    """


class BodyUnionMember0CompanyContributionUnionMember1(BaseModel):
    amount: int
    """
    Contribution amount in cents (for type=fixed) or basis points (for type=percent,
    where 100 = 1%). Not used for type=tiered.
    """

    type: Literal["percent"]
    """Contribution type.

    Supported values: "fixed" (amount in cents), "percent" (amount in basis points),
    or "tiered" (multi-tier matching).
    """


class BodyUnionMember0CompanyContributionUnionMember2Tier(BaseModel):
    match: int

    threshold: int


class BodyUnionMember0CompanyContributionUnionMember2(BaseModel):
    tiers: List[BodyUnionMember0CompanyContributionUnionMember2Tier]
    """
    Array of tier objects defining employer match tiers based on employee
    contribution thresholds. Required when type=tiered.
    """

    type: Literal["tiered"]
    """Contribution type.

    Supported values: "fixed" (amount in cents), "percent" (amount in basis points),
    or "tiered" (multi-tier matching).
    """


BodyUnionMember0CompanyContribution: TypeAlias = Union[
    BodyUnionMember0CompanyContributionUnionMember0,
    BodyUnionMember0CompanyContributionUnionMember1,
    BodyUnionMember0CompanyContributionUnionMember2,
    None,
]


class BodyUnionMember0EmployeeDeductionUnionMember0(BaseModel):
    amount: int
    """
    Contribution amount in cents (for type=fixed) or basis points (for type=percent,
    where 100 = 1%).
    """

    type: Literal["fixed"]
    """Contribution type.

    Supported values: "fixed" (amount in cents) or "percent" (amount in basis
    points).
    """


class BodyUnionMember0EmployeeDeductionUnionMember1(BaseModel):
    amount: int
    """
    Contribution amount in cents (for type=fixed) or basis points (for type=percent,
    where 100 = 1%).
    """

    type: Literal["percent"]
    """Contribution type.

    Supported values: "fixed" (amount in cents) or "percent" (amount in basis
    points).
    """


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
    """Company contribution configuration.

    Supports fixed amounts (in cents), percentage-based contributions (in basis
    points where 100 = 1%), or tiered matching structures.
    """

    employee_deduction: Optional[BodyUnionMember0EmployeeDeduction] = None
    """Employee deduction configuration.

    Supports both fixed amounts (in cents) and percentage-based contributions (in
    basis points where 100 = 1%).
    """

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
