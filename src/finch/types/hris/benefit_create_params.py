# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .benefit_type import BenefitType
from .benefit_frequency import BenefitFrequency

__all__ = ["BenefitCreateParams", "CompanyContribution", "CompanyContributionTier"]


class BenefitCreateParams(TypedDict, total=False):
    company_contribution: Optional[CompanyContribution]
    """The company match for this benefit."""

    description: str
    """Name of the benefit as it appears in the provider and pay statements.

    Recommend limiting this to <30 characters due to limitations in specific
    providers (e.g. Justworks).
    """

    frequency: Optional[BenefitFrequency]
    """The frequency of the benefit deduction/contribution."""

    type: Optional[BenefitType]
    """Type of benefit."""


class CompanyContributionTier(TypedDict, total=False):
    match: Required[int]

    threshold: Required[int]


class CompanyContribution(TypedDict, total=False):
    tiers: Required[Iterable[CompanyContributionTier]]

    type: Required[Literal["match"]]
