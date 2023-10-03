# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..income import Income
from ..._models import BaseModel
from ..location import Location

__all__ = ["EmploymentData", "Department", "Employment", "Manager"]


class Department(BaseModel):
    name: Optional[str] = None
    """The name of the department associated with the individual."""


class Employment(BaseModel):
    subtype: Optional[Literal["full_time", "intern", "part_time", "temp", "seasonal", "individual_contractor"]] = None
    """The secondary employment type of the individual.

    Options: `full_time`, `part_time`, `intern`, `temp`, `seasonal` and
    `individual_contractor`.
    """

    type: Optional[Literal["employee", "contractor"]] = None
    """The main employment type of the individual."""


class Manager(BaseModel):
    id: Optional[str] = None
    """A stable Finch `id` (UUID v4) for an individual in the company."""


class EmploymentData(BaseModel):
    id: Optional[str] = None
    """string A stable Finch `id` (UUID v4) for an individual in the company."""

    class_code: Optional[str] = None
    """Worker's compensation classification code for this employee"""

    department: Optional[Department] = None
    """The department object."""

    employment: Optional[Employment] = None
    """The employment object."""

    end_date: Optional[str] = None

    first_name: Optional[str] = None
    """The legal first name of the individual."""

    income_history: Optional[List[Optional[Income]]] = None
    """The array of income history."""

    income: Optional[Income] = None
    """The employee's income as reported by the provider.

    This may not always be annualized income, but may be in units of bi-weekly,
    semi-monthly, daily, etc, depending on what information the provider returns.
    """

    is_active: Optional[bool] = None
    """`true` if the individual an an active employee or contractor at the company."""

    last_name: Optional[str] = None
    """The legal last name of the individual."""

    location: Optional[Location] = None

    manager: Optional[Manager] = None
    """The manager object representing the manager of the individual within the org."""

    middle_name: Optional[str] = None
    """The legal middle name of the individual."""

    pay_group_ids: Optional[List[str]] = None
    """Note: This property is only available if enabled for your account.

    Please reach out to your Finch representative if you would like access.
    """

    source_id: Optional[str] = None
    """The source system's unique employment identifier for this individual"""

    start_date: Optional[str] = None

    title: Optional[str] = None
    """The current title of the individual."""

    work_id: Optional[str] = None
    """Note: This property is only available if enabled for your account.

    Please reach out to your Finch representative if you would like access.
    """

    work_id2: Optional[str] = FieldInfo(alias="work_id_2", default=None)
    """Note: This property is only available if enabled for your account.

    Please reach out to your Finch representative if you would like access.
    """
