# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, TypedDict

from ..money_param import MoneyParam
from ..hris.benefit_type import BenefitType

__all__ = [
    "PaymentCreateParams",
    "PayStatement",
    "PayStatementEarning",
    "PayStatementEarningAttributes",
    "PayStatementEarningAttributesMetadata",
    "PayStatementEmployeeDeduction",
    "PayStatementEmployeeDeductionAttributes",
    "PayStatementEmployeeDeductionAttributesMetadata",
    "PayStatementEmployerContribution",
    "PayStatementEmployerContributionAttributes",
    "PayStatementEmployerContributionAttributesMetadata",
    "PayStatementTax",
    "PayStatementTaxAttributes",
    "PayStatementTaxAttributesMetadata",
]


class PaymentCreateParams(TypedDict, total=False):
    end_date: str

    pay_statements: Iterable[PayStatement]

    start_date: str


class PayStatementEarningAttributesMetadata(TypedDict, total=False):
    metadata: Dict[str, object]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class PayStatementEarningAttributes(TypedDict, total=False):
    metadata: PayStatementEarningAttributesMetadata


class PayStatementEarning(TypedDict, total=False):
    amount: Optional[int]
    """The earnings amount in cents."""

    attributes: Optional[PayStatementEarningAttributes]

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


class PayStatementEmployeeDeductionAttributesMetadata(TypedDict, total=False):
    metadata: Dict[str, object]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class PayStatementEmployeeDeductionAttributes(TypedDict, total=False):
    metadata: PayStatementEmployeeDeductionAttributesMetadata


class PayStatementEmployeeDeduction(TypedDict, total=False):
    amount: Optional[int]
    """The deduction amount in cents."""

    attributes: Optional[PayStatementEmployeeDeductionAttributes]

    currency: Optional[str]
    """The deduction currency."""

    name: Optional[str]
    """The deduction name from the pay statement."""

    pre_tax: Optional[bool]
    """Boolean indicating if the deduction is pre-tax."""

    type: Optional[BenefitType]
    """Type of benefit."""


class PayStatementEmployerContributionAttributesMetadata(TypedDict, total=False):
    metadata: Dict[str, object]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class PayStatementEmployerContributionAttributes(TypedDict, total=False):
    metadata: PayStatementEmployerContributionAttributesMetadata


class PayStatementEmployerContribution(TypedDict, total=False):
    amount: Optional[int]
    """The contribution amount in cents."""

    attributes: Optional[PayStatementEmployerContributionAttributes]

    currency: Optional[str]
    """The contribution currency."""

    name: Optional[str]
    """The contribution name from the pay statement."""

    type: Optional[BenefitType]
    """Type of benefit."""


class PayStatementTaxAttributesMetadata(TypedDict, total=False):
    metadata: Dict[str, object]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class PayStatementTaxAttributes(TypedDict, total=False):
    metadata: PayStatementTaxAttributesMetadata


class PayStatementTax(TypedDict, total=False):
    amount: Optional[int]
    """The tax amount in cents."""

    attributes: Optional[PayStatementTaxAttributes]

    currency: Optional[str]
    """The currency code."""

    employer: Optional[bool]
    """`true` if the amount is paid by the employers."""

    name: Optional[str]
    """The exact name of tax from the pay statement."""

    type: Optional[Literal["state", "federal", "local", "fica"]]
    """The type of taxes."""


class PayStatement(TypedDict, total=False):
    earnings: Optional[Iterable[Optional[PayStatementEarning]]]
    """The array of earnings objects associated with this pay statement"""

    employee_deductions: Optional[Iterable[Optional[PayStatementEmployeeDeduction]]]
    """The array of deductions objects associated with this pay statement."""

    employer_contributions: Optional[Iterable[Optional[PayStatementEmployerContribution]]]

    gross_pay: Optional[MoneyParam]

    individual_id: str
    """A stable Finch `id` (UUID v4) for an individual in the company"""

    net_pay: Optional[MoneyParam]

    payment_method: Optional[Literal["check", "direct_deposit"]]
    """The payment method."""

    taxes: Optional[Iterable[Optional[PayStatementTax]]]
    """The array of taxes objects associated with this pay statement."""

    total_hours: Optional[float]
    """The number of hours worked for this pay period"""

    type: Optional[Literal["regular_payroll", "off_cycle_payroll", "one_time_payment"]]
    """The type of the payment associated with the pay statement."""
