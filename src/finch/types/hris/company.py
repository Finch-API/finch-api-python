# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..location import Location

__all__ = ["Company", "Account", "Department", "DepartmentParent", "Entity"]


class Account(BaseModel):
    account_name: Optional[str] = None
    """The name of the bank associated in the payroll/HRIS system."""

    account_number: Optional[str] = None
    """10-12 digit number to specify the bank account"""

    account_type: Optional[Literal["checking", "savings"]] = None
    """The type of bank account."""

    institution_name: Optional[str] = None
    """Name of the banking institution."""

    routing_number: Optional[str] = None
    """A nine-digit code that's based on the U.S.

    Bank location where your account was opened.
    """


class DepartmentParent(BaseModel):
    name: Optional[str] = None
    """The parent department's name."""


class Department(BaseModel):
    name: Optional[str] = None
    """The department name."""

    parent: Optional[DepartmentParent] = None
    """The parent department, if present."""


class Entity(BaseModel):
    subtype: Optional[Literal["s_corporation", "c_corporation", "b_corporation"]] = None
    """The tax payer subtype of the company."""

    type: Optional[Literal["llc", "corporation", "sole_proprietor", "non_profit", "partnership", "cooperative"]] = None
    """The tax payer type of the company."""


class Company(BaseModel):
    id: str
    """A stable Finch `id` (UUID v4) for the company."""

    accounts: Optional[List[Account]]
    """An array of bank account objects associated with the payroll/HRIS system."""

    departments: Optional[List[Optional[Department]]]
    """The array of company departments."""

    ein: Optional[str]
    """The employer identification number."""

    entity: Optional[Entity]
    """The entity type object."""

    legal_name: Optional[str]
    """The legal name of the company."""

    locations: Optional[List[Optional[Location]]]

    primary_email: Optional[str]
    """The email of the main administrator on the account."""

    primary_phone_number: Optional[str]
    """The phone number of the main administrator on the account. Format: `XXXXXXXXXX`"""
