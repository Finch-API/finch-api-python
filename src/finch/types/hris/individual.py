# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ...types import location
from ..._models import BaseModel

__all__ = ["Individual", "Email", "PhoneNumber"]


class Email(BaseModel):
    data: Optional[str]

    type: Optional[Literal["work", "personal"]]


class PhoneNumber(BaseModel):
    data: Optional[str]

    type: Optional[Literal["work", "personal"]]


class Individual(BaseModel):
    id: Optional[str]
    """A stable Finch `id` (UUID v4) for an individual in the company."""

    dob: Optional[str]

    emails: Optional[List[Email]]

    first_name: Optional[str]
    """The legal first name of the individual."""

    gender: Optional[Literal["female", "male", "other", "decline_to_specify"]]
    """The gender of the individual."""

    last_name: Optional[str]
    """The legal last name of the individual."""

    middle_name: Optional[str]
    """The legal middle name of the individual."""

    phone_numbers: Optional[List[Optional[PhoneNumber]]]

    preferred_name: Optional[str]
    """The preferred name of the individual."""

    residence: Optional[location.Location]

    ssn: Optional[str]
    """Note: This property is only available if enabled for your account.

    Please reach out to your Finch representative if you would like access.
    """
