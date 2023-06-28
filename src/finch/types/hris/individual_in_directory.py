# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["IndividualInDirectory", "Department", "Manager"]


class Department(BaseModel):
    name: Optional[str]
    """The name of the department."""


class Manager(BaseModel):
    id: Optional[str]
    """A stable Finch `id` (UUID v4) for an individual in the company."""


class IndividualInDirectory(BaseModel):
    id: Optional[str]
    """A stable Finch id (UUID v4) for an individual in the company."""

    department: Optional[Department]
    """The department object."""

    first_name: Optional[str]
    """The legal first name of the individual."""

    is_active: Optional[bool]
    """`true` if the individual is an active employee or contractor at the company."""

    last_name: Optional[str]
    """The legal last name of the individual."""

    manager: Optional[Manager]
    """The manager object."""

    middle_name: Optional[str]
    """The legal middle name of the individual."""
