# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

from ..location_param import LocationParam

__all__ = ["IndividualUpdateParams", "Email", "PhoneNumber"]


class IndividualUpdateParams(TypedDict, total=False):
    dob: Optional[str]

    emails: Optional[Iterable[Email]]

    encrypted_ssn: Optional[str]
    """Social Security Number of the individual in **encrypted** format.

    This field is only available with the `ssn` scope enabled and the
    `options: { include: ['ssn'] }` param set in the body.
    """

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

    gender: Optional[Literal["female", "male", "other", "decline_to_specify"]]
    """The gender of the individual."""

    last_name: Optional[str]
    """The legal last name of the individual."""

    middle_name: Optional[str]
    """The legal middle name of the individual."""

    phone_numbers: Optional[Iterable[Optional[PhoneNumber]]]

    preferred_name: Optional[str]
    """The preferred name of the individual."""

    residence: Optional[LocationParam]

    ssn: Optional[str]
    """Social Security Number of the individual.

    This field is only available with the `ssn` scope enabled and the
    `options: { include: ['ssn'] }` param set in the body.
    [Click here to learn more about enabling the SSN field](/developer-resources/Enable-SSN-Field).
    """


class Email(TypedDict, total=False):
    data: str

    type: Optional[Literal["work", "personal"]]


class PhoneNumber(TypedDict, total=False):
    data: Optional[str]

    type: Optional[Literal["work", "personal"]]
