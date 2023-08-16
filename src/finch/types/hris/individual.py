# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..location import Location

__all__ = ["Individual", "Email", "PhoneNumber"]


class Email(BaseModel):
    data: Optional[str] = None

    type: Optional[Literal["work", "personal"]] = None


class PhoneNumber(BaseModel):
    data: Optional[str] = None

    type: Optional[Literal["work", "personal"]] = None


class Individual(BaseModel):
    id: Optional[str] = None
    """A stable Finch `id` (UUID v4) for an individual in the company."""

    dob: Optional[str] = None

    emails: Optional[List[Email]] = None

    first_name: Optional[str] = None
    """The legal first name of the individual."""

    gender: Optional[Literal["female", "male", "other", "decline_to_specify"]] = None
    """The gender of the individual."""

    last_name: Optional[str] = None
    """The legal last name of the individual."""

    middle_name: Optional[str] = None
    """The legal middle name of the individual."""

    phone_numbers: Optional[List[Optional[PhoneNumber]]] = None

    preferred_name: Optional[str] = None
    """The preferred name of the individual."""

    residence: Optional[Location] = None

    ssn: Optional[str] = None
    """Note: This property is only available if enabled for your account.

    Please reach out to your Finch representative if you would like access.
    """
