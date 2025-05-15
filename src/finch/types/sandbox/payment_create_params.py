# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

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
    metadata: Required[Dict[str, Optional[object]]]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class PayStatementEarningAttributes(TypedDict, total=False):
    metadata: Required[PayStatementEarningAttributesMetadata]


class PayStatementEarning(TypedDict, total=False):
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

    attributes: Optional[PayStatementEarningAttributes]


class PayStatementEmployeeDeductionAttributesMetadata(TypedDict, total=False):
    metadata: Required[Dict[str, Optional[object]]]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class PayStatementEmployeeDeductionAttributes(TypedDict, total=False):
    metadata: Required[PayStatementEmployeeDeductionAttributesMetadata]


class PayStatementEmployeeDeduction(TypedDict, total=False):
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

    attributes: Optional[PayStatementEmployeeDeductionAttributes]


class PayStatementEmployerContributionAttributesMetadata(TypedDict, total=False):
    metadata: Required[Dict[str, Optional[object]]]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class PayStatementEmployerContributionAttributes(TypedDict, total=False):
    metadata: Required[PayStatementEmployerContributionAttributesMetadata]


class PayStatementEmployerContribution(TypedDict, total=False):
    amount: Required[Optional[int]]
    """The contribution amount in cents."""

    currency: Required[Optional[str]]
    """The contribution currency."""

    name: Required[Optional[str]]
    """The contribution name from the pay statement."""

    type: Required[Optional[BenefitType]]
    """Type of benefit."""

    attributes: Optional[PayStatementEmployerContributionAttributes]


class PayStatementTaxAttributesMetadata(TypedDict, total=False):
    metadata: Required[Dict[str, Optional[object]]]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class PayStatementTaxAttributes(TypedDict, total=False):
    metadata: Required[PayStatementTaxAttributesMetadata]


class PayStatementTax(TypedDict, total=False):
    amount: Required[Optional[int]]
    """The tax amount in cents."""

    currency: Required[Optional[str]]
    """The currency code."""

    employer: Required[Optional[bool]]
    """`true` if the amount is paid by the employers."""

    name: Required[Optional[str]]
    """The exact name of tax from the pay statement."""

    type: Required[Optional[Literal["state", "federal", "local", "fica"]]]
    """The type of taxes."""

    attributes: Optional[PayStatementTaxAttributes]


class PayStatement(TypedDict, total=False):
    earnings: Required[Optional[Iterable[Optional[PayStatementEarning]]]]
    """The array of earnings objects associated with this pay statement"""

    employee_deductions: Required[Optional[Iterable[Optional[PayStatementEmployeeDeduction]]]]
    """The array of deductions objects associated with this pay statement."""

    employer_contributions: Required[Optional[Iterable[Optional[PayStatementEmployerContribution]]]]

    gross_pay: Required[Optional[MoneyParam]]

    individual_id: Required[str]
    """A stable Finch `id` (UUID v4) for an individual in the company"""

    net_pay: Required[Optional[MoneyParam]]

    payment_method: Required[Optional[Literal["check", "direct_deposit"]]]
    """The payment method."""

    taxes: Required[Optional[Iterable[Optional[PayStatementTax]]]]
    """The array of taxes objects associated with this pay statement."""

    total_hours: Required[Optional[float]]
    """The number of hours worked for this pay period"""

    type: Required[Optional[Literal["regular_payroll", "off_cycle_payroll", "one_time_payment"]]]
    """The type of the payment associated with the pay statement."""
