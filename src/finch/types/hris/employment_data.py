# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..income import Income
from ..._models import BaseModel
from ..location import Location

__all__ = [
    "EmploymentData",
    "EmploymentDataResponseBody",
    "EmploymentDataResponseBodyDepartment",
    "EmploymentDataResponseBodyEmployment",
    "EmploymentDataResponseBodyManager",
    "EmploymentDataResponseBodyCustomField",
    "BatchError",
]


class EmploymentDataResponseBodyDepartment(BaseModel):
    """The department object."""

    name: Optional[str] = None
    """The name of the department associated with the individual."""


class EmploymentDataResponseBodyEmployment(BaseModel):
    """The employment object."""

    subtype: Optional[Literal["full_time", "intern", "part_time", "temp", "seasonal", "individual_contractor"]] = None
    """The secondary employment type of the individual.

    Options: `full_time`, `part_time`, `intern`, `temp`, `seasonal` and
    `individual_contractor`.
    """

    type: Optional[Literal["employee", "contractor"]] = None
    """The main employment type of the individual."""


class EmploymentDataResponseBodyManager(BaseModel):
    """The manager object representing the manager of the individual within the org."""

    id: str
    """A stable Finch `id` (UUID v4) for an individual in the company."""


class EmploymentDataResponseBodyCustomField(BaseModel):
    name: Optional[str] = None

    value: Union[Optional[str], Optional[List[object]], Optional[float], Optional[bool], Optional[object], None] = None


class EmploymentDataResponseBody(BaseModel):
    id: str
    """A stable Finch `id` (UUID v4) for an individual in the company."""

    class_code: Optional[str] = None
    """Worker's compensation classification code for this employee"""

    department: Optional[EmploymentDataResponseBodyDepartment] = None
    """The department object."""

    employment: Optional[EmploymentDataResponseBodyEmployment] = None
    """The employment object."""

    employment_status: Optional[
        Literal["active", "deceased", "leave", "onboarding", "prehire", "retired", "terminated"]
    ] = None
    """The detailed employment status of the individual."""

    end_date: Optional[str] = None

    first_name: Optional[str] = None
    """The legal first name of the individual."""

    flsa_status: Optional[Literal["exempt", "non_exempt", "unknown"]] = None
    """The FLSA status of the individual.

    Available options: `exempt`, `non_exempt`, `unknown`.
    """

    highly_compensated_employee: Optional[bool] = None
    """
    IRS flag indicating whether the employee is classified as a Highly Compensated
    Employee for nondiscrimination testing purposes (ADP/ACP tests). US-only.
    """

    is_active: Optional[bool] = None
    """`true` if the individual an an active employee or contractor at the company."""

    key_employee: Optional[bool] = None
    """
    IRS flag indicating whether the employee is classified as a Key Employee for
    top-heavy testing purposes. US-only.
    """

    last_name: Optional[str] = None
    """The legal last name of the individual."""

    latest_rehire_date: Optional[str] = None

    location: Optional[Location] = None

    manager: Optional[EmploymentDataResponseBodyManager] = None
    """The manager object representing the manager of the individual within the org."""

    middle_name: Optional[str] = None
    """The legal middle name of the individual."""

    start_date: Optional[str] = None

    title: Optional[str] = None
    """The current title of the individual."""

    union_code: Optional[str] = None
    """
    The code identifying the union the employee is a member of, as configured in the
    payroll system.
    """

    union_local: Optional[str] = None
    """The local chapter or local number within the employee's union."""

    custom_fields: Optional[List[EmploymentDataResponseBodyCustomField]] = None
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


EmploymentData: TypeAlias = Union[EmploymentDataResponseBody, BatchError]
