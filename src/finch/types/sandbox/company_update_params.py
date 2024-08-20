# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..location_param import LocationParam

__all__ = ["CompanyUpdateParams", "Account", "Department", "DepartmentParent", "Entity"]


class CompanyUpdateParams(TypedDict, total=False):
    accounts: Required[Optional[Iterable[Account]]]
    """An array of bank account objects associated with the payroll/HRIS system."""

    departments: Required[Optional[Iterable[Optional[Department]]]]
    """The array of company departments."""

    ein: Required[Optional[str]]
    """The employer identification number."""

    entity: Required[Optional[Entity]]
    """The entity type object."""

    legal_name: Required[Optional[str]]
    """The legal name of the company."""

    locations: Required[Optional[Iterable[Optional[LocationParam]]]]

    primary_email: Required[Optional[str]]
    """The email of the main administrator on the account."""

    primary_phone_number: Required[Optional[str]]
    """The phone number of the main administrator on the account. Format: `XXXXXXXXXX`"""


class Account(TypedDict, total=False):
    account_name: Optional[str]
    """The name of the bank associated in the payroll/HRIS system."""

    account_number: Optional[str]
    """10-12 digit number to specify the bank account"""

    account_type: Optional[Literal["checking", "savings"]]
    """The type of bank account."""

    institution_name: Optional[str]
    """Name of the banking institution."""

    routing_number: Optional[str]
    """A nine-digit code that's based on the U.S.

    Bank location where your account was opened.
    """


class DepartmentParent(TypedDict, total=False):
    name: Optional[str]
    """The parent department's name."""


class Department(TypedDict, total=False):
    name: Optional[str]
    """The department name."""

    parent: Optional[DepartmentParent]
    """The parent department, if present."""


class Entity(TypedDict, total=False):
    subtype: Optional[Literal["s_corporation", "c_corporation", "b_corporation"]]
    """The tax payer subtype of the company."""

    type: Optional[Literal["llc", "lp", "corporation", "sole_proprietor", "non_profit", "partnership", "cooperative"]]
    """The tax payer type of the company."""
