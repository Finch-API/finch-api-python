# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..money import Money
from ..._models import BaseModel
from .benefit_type import BenefitType

__all__ = [
    "PayStatement",
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


class EarningAttributesMetadata(BaseModel):
    metadata: Optional[Dict[str, object]] = None
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class EarningAttributes(BaseModel):
    metadata: Optional[EarningAttributesMetadata] = None


class Earning(BaseModel):
    amount: Optional[int] = None
    """The earnings amount in cents."""

    attributes: Optional[EarningAttributes] = None

    currency: Optional[str] = None
    """The earnings currency code."""

    hours: Optional[float] = None
    """The number of hours associated with this earning.

    (For salaried employees, this could be hours per pay period, `0` or `null`,
    depending on the provider).
    """

    name: Optional[str] = None
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
    ] = None
    """The type of earning."""


class EmployeeDeductionAttributesMetadata(BaseModel):
    metadata: Optional[Dict[str, object]] = None
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class EmployeeDeductionAttributes(BaseModel):
    metadata: Optional[EmployeeDeductionAttributesMetadata] = None


class EmployeeDeduction(BaseModel):
    amount: Optional[int] = None
    """The deduction amount in cents."""

    attributes: Optional[EmployeeDeductionAttributes] = None

    currency: Optional[str] = None
    """The deduction currency."""

    name: Optional[str] = None
    """The deduction name from the pay statement."""

    pre_tax: Optional[bool] = None
    """Boolean indicating if the deduction is pre-tax."""

    type: Optional[BenefitType] = None
    """Type of benefit."""


class EmployerContributionAttributesMetadata(BaseModel):
    metadata: Optional[Dict[str, object]] = None
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class EmployerContributionAttributes(BaseModel):
    metadata: Optional[EmployerContributionAttributesMetadata] = None


class EmployerContribution(BaseModel):
    amount: Optional[int] = None
    """The contribution amount in cents."""

    attributes: Optional[EmployerContributionAttributes] = None

    currency: Optional[str] = None
    """The contribution currency."""

    name: Optional[str] = None
    """The contribution name from the pay statement."""

    type: Optional[BenefitType] = None
    """Type of benefit."""


class TaxAttributesMetadata(BaseModel):
    metadata: Optional[Dict[str, object]] = None
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class TaxAttributes(BaseModel):
    metadata: Optional[TaxAttributesMetadata] = None


class Tax(BaseModel):
    amount: Optional[int] = None
    """The tax amount in cents."""

    attributes: Optional[TaxAttributes] = None

    currency: Optional[str] = None
    """The currency code."""

    employer: Optional[bool] = None
    """`true` if the amount is paid by the employers."""

    name: Optional[str] = None
    """The exact name of tax from the pay statement."""

    type: Optional[Literal["state", "federal", "local", "fica"]] = None
    """The type of taxes."""


class PayStatement(BaseModel):
    earnings: Optional[List[Optional[Earning]]] = None
    """The array of earnings objects associated with this pay statement"""

    employee_deductions: Optional[List[Optional[EmployeeDeduction]]] = None
    """The array of deductions objects associated with this pay statement."""

    employer_contributions: Optional[List[Optional[EmployerContribution]]] = None

    gross_pay: Optional[Money] = None

    individual_id: Optional[str] = None
    """A stable Finch `id` (UUID v4) for an individual in the company"""

    net_pay: Optional[Money] = None

    payment_method: Optional[Literal["check", "direct_deposit"]] = None
    """The payment method."""

    taxes: Optional[List[Optional[Tax]]] = None
    """The array of taxes objects associated with this pay statement."""

    total_hours: Optional[float] = None
    """The number of hours worked for this pay period"""

    type: Optional[Literal["regular_payroll", "off_cycle_payroll", "one_time_payment"]] = None
    """The type of the payment associated with the pay statement."""
