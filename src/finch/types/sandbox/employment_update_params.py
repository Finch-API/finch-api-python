# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

from ..income_param import IncomeParam
from ..location_param import LocationParam

__all__ = ["EmploymentUpdateParams", "CustomField", "Department", "Employment", "Manager"]


class EmploymentUpdateParams(TypedDict, total=False):
    class_code: Optional[str]
    """Worker's compensation classification code for this employee"""

    custom_fields: Iterable[CustomField]
    """Custom fields for the individual.

    These are fields which are defined by the employer in the system. Custom fields
    are not currently supported for assisted connections.
    """

    department: Optional[Department]
    """The department object."""

    employment: Optional[Employment]
    """The employment object."""

    end_date: Optional[str]

    first_name: Optional[str]
    """The legal first name of the individual."""

    income: Optional[IncomeParam]
    """The employee's income as reported by the provider.

    This may not always be annualized income, but may be in units of bi-weekly,
    semi-monthly, daily, etc, depending on what information the provider returns.
    """

    income_history: Optional[Iterable[Optional[IncomeParam]]]
    """The array of income history."""

    is_active: Optional[bool]
    """`true` if the individual an an active employee or contractor at the company."""

    last_name: Optional[str]
    """The legal last name of the individual."""

    location: Optional[LocationParam]

    manager: Optional[Manager]
    """The manager object representing the manager of the individual within the org."""

    middle_name: Optional[str]
    """The legal middle name of the individual."""

    source_id: str
    """The source system's unique employment identifier for this individual"""

    start_date: Optional[str]

    title: Optional[str]
    """The current title of the individual."""


class CustomField(TypedDict, total=False):
    name: Optional[str]

    value: object


class Department(TypedDict, total=False):
    name: Optional[str]
    """The name of the department associated with the individual."""


class Employment(TypedDict, total=False):
    subtype: Optional[Literal["full_time", "intern", "part_time", "temp", "seasonal", "individual_contractor"]]
    """The secondary employment type of the individual.

    Options: `full_time`, `part_time`, `intern`, `temp`, `seasonal` and
    `individual_contractor`.
    """

    type: Optional[Literal["employee", "contractor"]]
    """The main employment type of the individual."""


class Manager(TypedDict, total=False):
    id: str
    """A stable Finch `id` (UUID v4) for an individual in the company."""
