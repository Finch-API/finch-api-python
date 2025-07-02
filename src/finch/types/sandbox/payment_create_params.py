# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "PaymentCreateParams",
    "PayStatement",
    "PayStatementEarning",
    "PayStatementEmployeeDeduction",
    "PayStatementEmployerContribution",
    "PayStatementTax",
]


class PaymentCreateParams(TypedDict, total=False):
    end_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    pay_statements: Iterable[PayStatement]
    """Array of pay statements to include in the payment."""

    start_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]


class PayStatementEarning(TypedDict, total=False):
    amount: int

    hours: float

    name: str

    type: Literal[
        "bonus",
        "commission",
        "double_overtime",
        "other",
        "overtime",
        "pto",
        "reimbursement",
        "salary",
        "severance",
        "sick",
        "tips",
        "wage",
        "1099",
    ]


class PayStatementEmployeeDeduction(TypedDict, total=False):
    amount: int

    name: str

    pre_tax: bool

    type: Literal[
        "457",
        "401k",
        "401k_roth",
        "401k_loan",
        "403b",
        "403b_roth",
        "457_roth",
        "commuter",
        "custom_post_tax",
        "custom_pre_tax",
        "fsa_dependent_care",
        "fsa_medical",
        "hsa_post",
        "hsa_pre",
        "s125_dental",
        "s125_medical",
        "s125_vision",
        "simple",
        "simple_ira",
    ]


class PayStatementEmployerContribution(TypedDict, total=False):
    amount: int

    name: str

    type: Literal[
        "457",
        "401k",
        "401k_roth",
        "401k_loan",
        "403b",
        "403b_roth",
        "457_roth",
        "commuter",
        "custom_post_tax",
        "custom_pre_tax",
        "fsa_dependent_care",
        "fsa_medical",
        "hsa_post",
        "hsa_pre",
        "s125_dental",
        "s125_medical",
        "s125_vision",
        "simple",
        "simple_ira",
    ]


class PayStatementTax(TypedDict, total=False):
    amount: int

    employer: bool

    name: str

    type: Literal["federal", "fica", "local", "state"]


class PayStatement(TypedDict, total=False):
    individual_id: Required[str]

    earnings: Iterable[PayStatementEarning]

    employee_deductions: Iterable[PayStatementEmployeeDeduction]

    employer_contributions: Iterable[PayStatementEmployerContribution]

    gross_pay: int

    net_pay: int

    payment_method: Optional[Literal["check", "direct_deposit", "other"]]

    taxes: Iterable[PayStatementTax]

    total_hours: float

    type: Optional[Literal["off_cycle_payroll", "one_time_payment", "regular_payroll"]]
