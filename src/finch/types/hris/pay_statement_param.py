# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..money_param import MoneyParam
from .benefit_type import BenefitType

__all__ = [
    "PayStatementParam",
    "Earning",
    "EarningAttributes",
    "EarningAttributesMetadata",
    "EmployeeDeduction",
    "EmployeeDeductionAttributes",
    "EmployeeDeductionAttributesMetadata",
    "EmployerContribution",
    "EmployerContributionAttributes",
    "EmployerContributionAttributesMetadata",
    "Tax",
    "TaxAttributes",
    "TaxAttributesMetadata",
]


class EarningAttributesMetadata(TypedDict, total=False):
    metadata: Required[Dict[str, Optional[object]]]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class EarningAttributes(TypedDict, total=False):
    metadata: Required[EarningAttributesMetadata]


class Earning(TypedDict, total=False):
    amount: Required[Optional[int]]
    """The earnings amount in cents."""

    currency: Required[Optional[str]]
    """The earnings currency code."""

    hours: Required[Optional[float]]
    """The number of hours associated with this earning.

    (For salaried employees, this could be hours per pay period, `0` or `null`,
    depending on the provider).
    """

    name: Required[Optional[str]]
    """The exact name of the deduction from the pay statement."""

    type: Required[
        Optional[
            Literal[
                "salary",
                "wage",
                "reimbursement",
                "overtime",
                "severance",
                "double_overtime",
                "pto",
                "sick",
                "bonus",
                "commission",
                "tips",
                "1099",
                "other",
            ]
        ]
    ]
    """The type of earning."""

    attributes: Optional[EarningAttributes]


class EmployeeDeductionAttributesMetadata(TypedDict, total=False):
    metadata: Required[Dict[str, Optional[object]]]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class EmployeeDeductionAttributes(TypedDict, total=False):
    metadata: Required[EmployeeDeductionAttributesMetadata]


class EmployeeDeduction(TypedDict, total=False):
    amount: Required[Optional[int]]
    """The deduction amount in cents."""

    currency: Required[Optional[str]]
    """The deduction currency."""

    name: Required[Optional[str]]
    """The deduction name from the pay statement."""

    pre_tax: Required[Optional[bool]]
    """Boolean indicating if the deduction is pre-tax."""

    type: Required[Optional[BenefitType]]
    """Type of benefit."""

    attributes: Optional[EmployeeDeductionAttributes]


class EmployerContributionAttributesMetadata(TypedDict, total=False):
    metadata: Required[Dict[str, Optional[object]]]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class EmployerContributionAttributes(TypedDict, total=False):
    metadata: Required[EmployerContributionAttributesMetadata]


class EmployerContribution(TypedDict, total=False):
    currency: Required[Optional[str]]
    """The contribution currency."""

    name: Required[Optional[str]]
    """The contribution name from the pay statement."""

    type: Required[Optional[BenefitType]]
    """Type of benefit."""

    amount: Optional[int]
    """The contribution amount in cents."""

    attributes: Optional[EmployerContributionAttributes]


class TaxAttributesMetadata(TypedDict, total=False):
    metadata: Required[Dict[str, Optional[object]]]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class TaxAttributes(TypedDict, total=False):
    metadata: Required[TaxAttributesMetadata]


class Tax(TypedDict, total=False):
    currency: Required[Optional[str]]
    """The currency code."""

    employer: Required[Optional[bool]]
    """`true` if the amount is paid by the employers."""

    name: Required[Optional[str]]
    """The exact name of tax from the pay statement."""

    type: Required[Optional[Literal["state", "federal", "local", "fica"]]]
    """The type of taxes."""

    amount: Optional[int]
    """The tax amount in cents."""

    attributes: Optional[TaxAttributes]


class PayStatementParam(TypedDict, total=False):
    earnings: Required[Optional[Iterable[Optional[Earning]]]]
    """The array of earnings objects associated with this pay statement"""

    employee_deductions: Required[Optional[Iterable[Optional[EmployeeDeduction]]]]
    """The array of deductions objects associated with this pay statement."""

    employer_contributions: Required[Optional[Iterable[Optional[EmployerContribution]]]]

    gross_pay: Required[Optional[MoneyParam]]

    individual_id: Required[str]
    """A stable Finch `id` (UUID v4) for an individual in the company"""

    net_pay: Required[Optional[MoneyParam]]

    payment_method: Required[Optional[Literal["check", "direct_deposit", "other"]]]
    """The payment method."""

    taxes: Required[Optional[Iterable[Optional[Tax]]]]
    """The array of taxes objects associated with this pay statement."""

    total_hours: Required[Optional[float]]
    """The number of hours worked for this pay period"""

    type: Required[Optional[Literal["off_cycle_payroll", "one_time_payment", "regular_payroll"]]]
    """The type of the payment associated with the pay statement."""
