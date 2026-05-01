# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "IndividualBenefit",
    "Body",
    "BodyIndividualBenefit",
    "BodyIndividualBenefitCompanyContribution",
    "BodyIndividualBenefitCompanyContributionCompanyContributionFixed",
    "BodyIndividualBenefitCompanyContributionCompanyContributionPercent",
    "BodyIndividualBenefitCompanyContributionCompanyContributionTiered",
    "BodyIndividualBenefitCompanyContributionCompanyContributionTieredTier",
    "BodyIndividualBenefitEmployeeDeduction",
    "BodyIndividualBenefitEmployeeDeductionEmployeeDeductionContributionFixed",
    "BodyIndividualBenefitEmployeeDeductionEmployeeDeductionContributionPercent",
    "BodyBatchError",
]


class BodyIndividualBenefitCompanyContributionCompanyContributionFixed(BaseModel):
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


class BodyIndividualBenefitCompanyContributionCompanyContributionPercent(BaseModel):
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


class BodyIndividualBenefitCompanyContributionCompanyContributionTieredTier(BaseModel):
    match: int

    threshold: int


class BodyIndividualBenefitCompanyContributionCompanyContributionTiered(BaseModel):
    tiers: List[BodyIndividualBenefitCompanyContributionCompanyContributionTieredTier]
    """
    Array of tier objects defining employer match tiers based on employee
    contribution thresholds. Required when type=tiered.
    """

    type: Literal["tiered"]
    """Contribution type.

    Supported values: "fixed" (amount in cents), "percent" (amount in basis points),
    or "tiered" (multi-tier matching).
    """


BodyIndividualBenefitCompanyContribution: TypeAlias = Union[
    BodyIndividualBenefitCompanyContributionCompanyContributionFixed,
    BodyIndividualBenefitCompanyContributionCompanyContributionPercent,
    BodyIndividualBenefitCompanyContributionCompanyContributionTiered,
    None,
]


class BodyIndividualBenefitEmployeeDeductionEmployeeDeductionContributionFixed(BaseModel):
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


class BodyIndividualBenefitEmployeeDeductionEmployeeDeductionContributionPercent(BaseModel):
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


BodyIndividualBenefitEmployeeDeduction: TypeAlias = Union[
    BodyIndividualBenefitEmployeeDeductionEmployeeDeductionContributionFixed,
    BodyIndividualBenefitEmployeeDeductionEmployeeDeductionContributionPercent,
    None,
]


class BodyIndividualBenefit(BaseModel):
    annual_maximum: Optional[int] = None
    """
    If the benefit supports annual maximum, the amount in cents for this individual.
    """

    catch_up: Optional[bool] = None
    """
    If the benefit supports catch up (401k, 403b, etc.), whether catch up is enabled
    for this individual.
    """

    company_contribution: Optional[BodyIndividualBenefitCompanyContribution] = None
    """Company contribution configuration.

    Supports fixed amounts (in cents), percentage-based contributions (in basis
    points where 100 = 1%), or tiered matching structures.
    """

    employee_deduction: Optional[BodyIndividualBenefitEmployeeDeduction] = None
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


Body: TypeAlias = Union[BodyIndividualBenefit, BodyBatchError]


class IndividualBenefit(BaseModel):
    body: Body

    code: int

    individual_id: str
