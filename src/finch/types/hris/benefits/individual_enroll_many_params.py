# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "IndividualEnrollManyParams",
    "Individual",
    "IndividualConfiguration",
    "IndividualConfigurationCompanyContribution",
    "IndividualConfigurationCompanyContributionTier",
    "IndividualConfigurationEmployeeDeduction",
]


class IndividualEnrollManyParams(TypedDict, total=False):
    entity_ids: SequenceNotStr[str]
    """The entity IDs to specify which entities' data to access."""

    individuals: Iterable[Individual]
    """Array of the individual_id to enroll and a configuration object."""


class IndividualConfigurationCompanyContributionTier(TypedDict, total=False):
    match: Required[int]
    """The employer match percentage in basis points (0-10000 = 0-100%)"""

    threshold: Required[int]
    """The employee contribution threshold in basis points (0-10000 = 0-100%)"""


class IndividualConfigurationCompanyContribution(TypedDict, total=False):
    amount: int
    """
    Amount in cents for fixed type or basis points (1/100th of a percent) for
    percent type
    """

    tiers: Iterable[IndividualConfigurationCompanyContributionTier]
    """
    Array of tier objects for tiered contribution matching (required when type is
    tiered)
    """

    type: Literal["fixed", "percent", "tiered"]


class IndividualConfigurationEmployeeDeduction(TypedDict, total=False):
    amount: int
    """
    Amount in cents for fixed type or basis points (1/100th of a percent) for
    percent type
    """

    type: Literal["fixed", "percent"]


class IndividualConfiguration(TypedDict, total=False):
    annual_contribution_limit: Literal["individual", "family"]
    """
    For HSA benefits only - whether the contribution limit is for an individual or
    family
    """

    annual_maximum: Optional[int]
    """Maximum annual amount in cents"""

    catch_up: bool
    """For retirement benefits only - whether catch up contributions are enabled"""

    company_contribution: IndividualConfigurationCompanyContribution

    effective_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """The date the enrollment will take effect"""

    employee_deduction: IndividualConfigurationEmployeeDeduction


class Individual(TypedDict, total=False):
    configuration: IndividualConfiguration

    individual_id: str
    """Finch id (uuidv4) for the individual to enroll"""
