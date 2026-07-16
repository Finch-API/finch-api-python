# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, TypedDict

from ..income_param import IncomeParam
from ..location_param import LocationParam

__all__ = [
    "DirectoryCreateParams",
    "Body",
    "BodyCustomField",
    "BodyDepartment",
    "BodyEmail",
    "BodyEmployment",
    "BodyManager",
    "BodyPhoneNumber",
]


class DirectoryCreateParams(TypedDict, total=False):
    body: Iterable[Body]
    """Array of individuals to create.

    Takes all combined fields from `/individual` and `/employment` endpoints. All
    fields are optional.
    """


class BodyCustomField(TypedDict, total=False):
    name: Optional[str]

    value: Union[Optional[str], Optional[Iterable[object]], Optional[float], Optional[bool], Optional[object], None]


class BodyDepartment(TypedDict, total=False):
    """The department object."""

    name: Optional[str]
    """The name of the department associated with the individual."""


class BodyEmail(TypedDict, total=False):
    data: str

    type: Optional[Literal["work", "personal"]]


class BodyEmployment(TypedDict, total=False):
    """The employment object."""

    subtype: Optional[Literal["full_time", "intern", "part_time", "temp", "seasonal", "individual_contractor"]]
    """The secondary employment type of the individual.

    Options: `full_time`, `part_time`, `intern`, `temp`, `seasonal` and
    `individual_contractor`.
    """

    type: Optional[Literal["employee", "contractor"]]
    """The main employment type of the individual."""


class BodyManager(TypedDict, total=False):
    """The manager object representing the manager of the individual within the org."""

    id: str
    """A stable Finch `id` (UUID v4) for an individual in the company."""


class BodyPhoneNumber(TypedDict, total=False):
    data: Optional[str]

    type: Optional[Literal["work", "personal"]]


class Body(TypedDict, total=False):
    class_code: Optional[str]
    """Worker's compensation classification code for this employee"""

    custom_fields: Optional[Iterable[BodyCustomField]]
    """Custom fields for the individual.

    These are fields which are defined by the employer in the system. Custom fields
    are not currently supported for assisted connections.
    """

    department: Optional[BodyDepartment]
    """The department object."""

    dob: Optional[str]

    emails: Optional[Iterable[BodyEmail]]

    employment: Optional[BodyEmployment]
    """The employment object."""

    employment_status: Optional[
        Literal["active", "deceased", "leave", "onboarding", "prehire", "retired", "terminated"]
    ]
    """The detailed employment status of the individual."""

    encrypted_ssn: Optional[str]
    """Social Security Number of the individual in **encrypted** format.

    This field is only available with the `ssn` scope enabled and the
    `options: { include: ['ssn'] }` param set in the body.
    """

    end_date: Optional[str]

    ethnicity: Optional[
        Literal[
            "asian",
            "white",
            "black_or_african_american",
            "native_hawaiian_or_pacific_islander",
            "american_indian_or_alaska_native",
            "hispanic_or_latino",
            "two_or_more_races",
            "decline_to_specify",
        ]
    ]
    """The EEOC-defined ethnicity of the individual."""

    first_name: Optional[str]
    """The legal first name of the individual."""

    flsa_status: Optional[Literal["exempt", "non_exempt", "unknown"]]
    """The FLSA status of the individual.

    Available options: `exempt`, `non_exempt`, `unknown`.
    """

    gender: Optional[Literal["female", "male", "other", "decline_to_specify"]]
    """The gender of the individual."""

    highly_compensated_employee: Optional[bool]
    """
    IRS flag indicating whether the employee is classified as a Highly Compensated
    Employee for nondiscrimination testing purposes (ADP/ACP tests). US-only.
    """

    income: Optional[IncomeParam]
    """The employee's income as reported by the provider.

    This may not always be annualized income, but may be in units of bi-weekly,
    semi-monthly, daily, etc, depending on what information the provider returns.
    """

    income_history: Optional[Iterable[Optional[IncomeParam]]]
    """The array of income history."""

    is_active: Optional[bool]
    """`true` if the individual an an active employee or contractor at the company."""

    key_employee: Optional[bool]
    """
    IRS flag indicating whether the employee is classified as a Key Employee for
    top-heavy testing purposes. US-only.
    """

    last_name: Optional[str]
    """The legal last name of the individual."""

    latest_rehire_date: Optional[str]

    location: Optional[LocationParam]

    manager: Optional[BodyManager]
    """The manager object representing the manager of the individual within the org."""

    marital_status: Optional[Literal["single", "married", "divorced", "widowed", "domestic_partner", "unknown"]]
    """
    The employee's marital status, used for beneficiary designation and spousal
    consent workflows.
    """

    middle_name: Optional[str]
    """The legal middle name of the individual."""

    phone_numbers: Optional[Iterable[Optional[BodyPhoneNumber]]]

    preferred_name: Optional[str]
    """The preferred name of the individual."""

    residence: Optional[LocationParam]

    source_id: Optional[str]
    """The source system's unique employment identifier for this individual"""

    ssn: Optional[str]
    """Social Security Number of the individual.

    This field is only available with the `ssn` scope enabled and the
    `options: { include: ['ssn'] }` param set in the body.
    [Click here to learn more about enabling the SSN field](/developer-resources/Enable-SSN-Field).
    """

    start_date: Optional[str]

    title: Optional[str]
    """The current title of the individual."""

    union_code: Optional[str]
    """
    The code identifying the union the employee is a member of, as configured in the
    payroll system.
    """

    union_local: Optional[str]
    """The local chapter or local number within the employee's union."""
