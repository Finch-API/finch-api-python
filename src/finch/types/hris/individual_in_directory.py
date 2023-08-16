# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["IndividualInDirectory", "Department", "Manager"]


class Department(BaseModel):
    name: Optional[str] = None
    """The name of the department."""


class Manager(BaseModel):
    id: Optional[str] = None
    """A stable Finch `id` (UUID v4) for an individual in the company."""


class IndividualInDirectory(BaseModel):
    id: Optional[str] = None
    """A stable Finch id (UUID v4) for an individual in the company."""

    department: Optional[Department] = None
    """The department object."""

    first_name: Optional[str] = None
    """The legal first name of the individual."""

    is_active: Optional[bool] = None
    """`true` if the individual is an active employee or contractor at the company."""

    last_name: Optional[str] = None
    """The legal last name of the individual."""

    manager: Optional[Manager] = None
    """The manager object."""

    middle_name: Optional[str] = None
    """The legal middle name of the individual."""
