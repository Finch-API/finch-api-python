# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ...types import money
from ..._models import BaseModel
from ...types.hris import benefit_type

__all__ = ["PayStatement", "Earning", "EmployeeDeduction", "EmployerContribution", "Tax"]


class Earning(BaseModel):
    amount: Optional[int]
    """The earnings amount in cents."""

    currency: Optional[str]
    """The earnings currency code."""

    hours: Optional[float]
    """The number of hours associated with this earning.

    (For salaried employees, this could be hours per pay period, `0` or `null`,
    depending on the provider).
    """

    name: Optional[str]
    """The exact name of the deduction from the pay statement."""

    type: Optional[
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
    """The type of earning."""


class EmployeeDeduction(BaseModel):
    amount: Optional[int]
    """The deduction amount in cents."""

    currency: Optional[str]
    """The deduction currency."""

    name: Optional[str]
    """The deduction name from the pay statement."""

    pre_tax: Optional[bool]
    """Boolean indicating if the deduction is pre-tax."""

    type: Optional[benefit_type.BenefitType]
    """Type of benefit."""


class EmployerContribution(BaseModel):
    amount: Optional[int]
    """The contribution amount in cents."""

    currency: Optional[str]
    """The contribution currency."""

    name: Optional[str]
    """The contribution name from the pay statement."""

    type: Optional[benefit_type.BenefitType]
    """Type of benefit."""


class Tax(BaseModel):
    amount: Optional[int]
    """The tax amount in cents."""

    currency: Optional[str]
    """The currency code."""

    employer: Optional[bool]
    """`true` if the amount is paid by the employers."""

    name: Optional[str]
    """The exact name of tax from the pay statement."""

    type: Optional[Literal["state", "federal", "local", "fica"]]
    """The type of taxes."""


class PayStatement(BaseModel):
    earnings: Optional[List[Optional[Earning]]]
    """The array of earnings objects associated with this pay statement"""

    employee_deductions: Optional[List[Optional[EmployeeDeduction]]]
    """The array of deductions objects associated with this pay statement."""

    employer_contributions: Optional[List[Optional[EmployerContribution]]]

    gross_pay: Optional[money.Money]

    individual_id: Optional[str]
    """A stable Finch `id` (UUID v4) for an individual in the company"""

    net_pay: Optional[money.Money]

    payment_method: Optional[Literal["check", "direct_deposit"]]
    """The payment method."""

    taxes: Optional[List[Optional[Tax]]]
    """The array of taxes objects associated with this pay statement."""

    total_hours: Optional[int]
    """The number of hours worked for this pay period"""

    type: Optional[Literal["regular_payroll", "off_cycle_payroll", "one_time_payment"]]
    """The type of the payment associated with the pay statement."""
