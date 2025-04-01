# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "IndividualEnrollManyParams",
    "Individual",
    "IndividualConfiguration",
    "IndividualConfigurationCompanyContribution",
    "IndividualConfigurationEmployeeDeduction",
]


class IndividualEnrollManyParams(TypedDict, total=False):
    individuals: Iterable[Individual]
    """Array of the individual_id to enroll and a configuration object."""


class IndividualConfigurationCompanyContribution(TypedDict, total=False):
    amount: int
    """
    Amount in cents for fixed type or basis points (1/100th of a percent) for
    percent type
    """

    type: Literal["fixed", "percent"]


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
