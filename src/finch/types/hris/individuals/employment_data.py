# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....types import income, location
from ...._models import BaseModel

__all__ = ["EmploymentData", "Department", "Employment", "Manager"]


class Department(BaseModel):
    name: Optional[str]
    """The name of the department associated with the individual."""


class Employment(BaseModel):
    subtype: Optional[Literal["full_time", "intern", "part_time", "temp", "seasonal", "individual_contractor"]]
    """The secondary employment type of the individual.

    Options: `full_time`, `part_time`, `intern`, `temp`, `seasonal` and
    `individual_contractor`.
    """

    type: Optional[Literal["employee", "contractor"]]
    """The main employment type of the individual."""


class Manager(BaseModel):
    id: Optional[str]
    """A stable Finch `id` (UUID v4) for an individual in the company."""


class EmploymentData(BaseModel):
    id: Optional[str]
    """string A stable Finch `id` (UUID v4) for an individual in the company."""

    class_code: Optional[str]
    """Worker's compensation classification code for this employee"""

    department: Optional[Department]
    """The department object."""

    employment: Optional[Employment]
    """The employment object."""

    end_date: Optional[str]

    first_name: Optional[str]
    """The legal first name of the individual."""

    income_history: Optional[List[Optional[income.Income]]]
    """The array of income history."""

    income: Optional[income.Income]
    """The employee's income as reported by the provider.

    This may not always be annualized income, but may be in units of bi-weekly,
    semi-monthly, daily, etc, depending on what information the provider returns.
    """

    is_active: Optional[bool]
    """`true` if the individual an an active employee or contractor at the company."""

    last_name: Optional[str]
    """The legal last name of the individual."""

    location: Optional[location.Location]

    manager: Optional[Manager]
    """The manager object representing the manager of the individual within the org."""

    middle_name: Optional[str]
    """The legal middle name of the individual."""

    pay_group_ids: Optional[List[str]]
    """Note: This property is only available if enabled for your account.

    Please reach out to your Finch representative if you would like access.
    """

    start_date: Optional[str]

    title: Optional[str]
    """The current title of the individual."""

    work_id: Optional[str]
    """Note: This property is only available if enabled for your account.

    Please reach out to your Finch representative if you would like access.
    """

    work_id2: Optional[str] = FieldInfo(alias="work_id_2")
    """Note: This property is only available if enabled for your account.

    Please reach out to your Finch representative if you would like access.
    """
