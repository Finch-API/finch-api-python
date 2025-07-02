# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..income import Income
from ..._models import BaseModel
from ..location import Location

__all__ = [
    "EmploymentData",
    "UnionMember0",
    "UnionMember0Department",
    "UnionMember0Employment",
    "UnionMember0Manager",
    "UnionMember0CustomField",
    "BatchError",
]


class UnionMember0Department(BaseModel):
    name: Optional[str] = None
    """The name of the department associated with the individual."""


class UnionMember0Employment(BaseModel):
    subtype: Optional[Literal["full_time", "intern", "part_time", "temp", "seasonal", "individual_contractor"]] = None
    """The secondary employment type of the individual.

    Options: `full_time`, `part_time`, `intern`, `temp`, `seasonal` and
    `individual_contractor`.
    """

    type: Optional[Literal["employee", "contractor"]] = None
    """The main employment type of the individual."""


class UnionMember0Manager(BaseModel):
    id: str
    """A stable Finch `id` (UUID v4) for an individual in the company."""


class UnionMember0CustomField(BaseModel):
    name: Optional[str] = None

    value: Union[Optional[str], Optional[List[object]], Optional[float], Optional[bool], Optional[object], None] = None


class UnionMember0(BaseModel):
    id: str
    """A stable Finch `id` (UUID v4) for an individual in the company."""

    class_code: Optional[str] = None
    """Worker's compensation classification code for this employee"""

    department: Optional[UnionMember0Department] = None
    """The department object."""

    employment: Optional[UnionMember0Employment] = None
    """The employment object."""

    employment_status: Optional[
        Literal["active", "deceased", "leave", "onboarding", "prehire", "retired", "terminated"]
    ] = None
    """The detailed employment status of the individual.

    Available options: `active`, `deceased`, `leave`, `onboarding`, `prehire`,
    `retired`, `terminated`.
    """

    end_date: Optional[str] = None

    first_name: Optional[str] = None
    """The legal first name of the individual."""

    is_active: Optional[bool] = None
    """`true` if the individual an an active employee or contractor at the company."""

    last_name: Optional[str] = None
    """The legal last name of the individual."""

    latest_rehire_date: Optional[str] = None

    location: Optional[Location] = None

    manager: Optional[UnionMember0Manager] = None
    """The manager object representing the manager of the individual within the org."""

    middle_name: Optional[str] = None
    """The legal middle name of the individual."""

    start_date: Optional[str] = None

    title: Optional[str] = None
    """The current title of the individual."""

    custom_fields: Optional[List[UnionMember0CustomField]] = None
    """Custom fields for the individual.

    These are fields which are defined by the employer in the system. Custom fields
    are not currently supported for assisted connections.
    """

    income_history: Optional[List[Optional[Income]]] = None
    """The array of income history."""

    income: Optional[Income] = None
    """The employee's income as reported by the provider.

    This may not always be annualized income, but may be in units of bi-weekly,
    semi-monthly, daily, etc, depending on what information the provider returns.
    """

    source_id: Optional[str] = None
    """The source system's unique employment identifier for this individual"""

    work_id: Optional[str] = None
    """This field is deprecated in favour of `source_id`"""


class BatchError(BaseModel):
    code: float

    message: str

    name: str

    finch_code: Optional[str] = None


EmploymentData: TypeAlias = Union[UnionMember0, BatchError]
