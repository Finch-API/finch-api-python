# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..location import Location

__all__ = ["Individual", "UnionMember0", "UnionMember0PhoneNumber", "UnionMember0Email", "BatchError"]


class UnionMember0PhoneNumber(BaseModel):
    data: Optional[str] = None

    type: Optional[Literal["work", "personal"]] = None


class UnionMember0Email(BaseModel):
    data: str

    type: Optional[Literal["work", "personal"]] = None


class UnionMember0(BaseModel):
    id: str
    """A stable Finch `id` (UUID v4) for an individual in the company."""

    dob: Optional[str] = None

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
    ] = None
    """The EEOC-defined ethnicity of the individual."""

    first_name: Optional[str] = None
    """The legal first name of the individual."""

    gender: Optional[Literal["female", "male", "other", "decline_to_specify"]] = None
    """The gender of the individual."""

    last_name: Optional[str] = None
    """The legal last name of the individual."""

    middle_name: Optional[str] = None
    """The legal middle name of the individual."""

    phone_numbers: Optional[List[Optional[UnionMember0PhoneNumber]]] = None

    preferred_name: Optional[str] = None
    """The preferred name of the individual."""

    residence: Optional[Location] = None

    emails: Optional[List[UnionMember0Email]] = None

    encrypted_ssn: Optional[str] = None
    """Social Security Number of the individual in **encrypted** format.

    This field is only available with the `ssn` scope enabled and the
    `options: { include: ['ssn'] }` param set in the body.
    """

    ssn: Optional[str] = None
    """Social Security Number of the individual.

    This field is only available with the `ssn` scope enabled and the
    `options: { include: ['ssn'] }` param set in the body.
    [Click here to learn more about enabling the SSN field](/developer-resources/Enable-SSN-Field).
    """


class BatchError(BaseModel):
    code: float

    message: str

    name: str

    finch_code: Optional[str] = None


Individual: TypeAlias = Union[UnionMember0, BatchError]
