# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..money import Money
from ..._models import BaseModel
from .benefit_type import BenefitType

__all__ = [
    "PayStatementResponseBody",
    "UnionMember0",
    "UnionMember0Paging",
    "UnionMember0PayStatement",
    "UnionMember0PayStatementEarning",
    "UnionMember0PayStatementEarningAttributes",
    "UnionMember0PayStatementEarningAttributesMetadata",
    "UnionMember0PayStatementEmployeeDeduction",
    "UnionMember0PayStatementEmployeeDeductionAttributes",
    "UnionMember0PayStatementEmployeeDeductionAttributesMetadata",
    "UnionMember0PayStatementEmployerContribution",
    "UnionMember0PayStatementEmployerContributionAttributes",
    "UnionMember0PayStatementEmployerContributionAttributesMetadata",
    "UnionMember0PayStatementTax",
    "UnionMember0PayStatementTaxAttributes",
    "UnionMember0PayStatementTaxAttributesMetadata",
    "BatchError",
    "UnionMember2",
]


class UnionMember0Paging(BaseModel):
    offset: int
    """The current start index of the returned list of elements"""

    count: Optional[int] = None
    """The total number of elements for the entire query (not just the given page)"""


class UnionMember0PayStatementEarningAttributesMetadata(BaseModel):
    metadata: Dict[str, Optional[object]]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class UnionMember0PayStatementEarningAttributes(BaseModel):
    metadata: UnionMember0PayStatementEarningAttributesMetadata


class UnionMember0PayStatementEarning(BaseModel):
    amount: Optional[int] = None
    """The earnings amount in cents."""

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

    attributes: Optional[UnionMember0PayStatementEarningAttributes] = None


class UnionMember0PayStatementEmployeeDeductionAttributesMetadata(BaseModel):
    metadata: Dict[str, Optional[object]]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class UnionMember0PayStatementEmployeeDeductionAttributes(BaseModel):
    metadata: UnionMember0PayStatementEmployeeDeductionAttributesMetadata


class UnionMember0PayStatementEmployeeDeduction(BaseModel):
    amount: Optional[int] = None
    """The deduction amount in cents."""

    currency: Optional[str] = None
    """The deduction currency."""

    name: Optional[str] = None
    """The deduction name from the pay statement."""

    pre_tax: Optional[bool] = None
    """Boolean indicating if the deduction is pre-tax."""

    type: Optional[BenefitType] = None
    """Type of benefit."""

    attributes: Optional[UnionMember0PayStatementEmployeeDeductionAttributes] = None


class UnionMember0PayStatementEmployerContributionAttributesMetadata(BaseModel):
    metadata: Dict[str, Optional[object]]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class UnionMember0PayStatementEmployerContributionAttributes(BaseModel):
    metadata: UnionMember0PayStatementEmployerContributionAttributesMetadata


class UnionMember0PayStatementEmployerContribution(BaseModel):
    currency: Optional[str] = None
    """The contribution currency."""

    name: Optional[str] = None
    """The contribution name from the pay statement."""

    type: Optional[BenefitType] = None
    """Type of benefit."""

    amount: Optional[int] = None
    """The contribution amount in cents."""

    attributes: Optional[UnionMember0PayStatementEmployerContributionAttributes] = None


class UnionMember0PayStatementTaxAttributesMetadata(BaseModel):
    metadata: Dict[str, Optional[object]]
    """The metadata to be attached to the entity by existing rules.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class UnionMember0PayStatementTaxAttributes(BaseModel):
    metadata: UnionMember0PayStatementTaxAttributesMetadata


class UnionMember0PayStatementTax(BaseModel):
    currency: Optional[str] = None
    """The currency code."""

    employer: Optional[bool] = None
    """`true` if the amount is paid by the employers."""

    name: Optional[str] = None
    """The exact name of tax from the pay statement."""

    type: Optional[Literal["state", "federal", "local", "fica"]] = None
    """The type of taxes."""

    amount: Optional[int] = None
    """The tax amount in cents."""

    attributes: Optional[UnionMember0PayStatementTaxAttributes] = None


class UnionMember0PayStatement(BaseModel):
    earnings: Optional[List[Optional[UnionMember0PayStatementEarning]]] = None
    """The array of earnings objects associated with this pay statement"""

    employee_deductions: Optional[List[Optional[UnionMember0PayStatementEmployeeDeduction]]] = None
    """The array of deductions objects associated with this pay statement."""

    employer_contributions: Optional[List[Optional[UnionMember0PayStatementEmployerContribution]]] = None

    gross_pay: Optional[Money] = None

    individual_id: str
    """A stable Finch `id` (UUID v4) for an individual in the company"""

    net_pay: Optional[Money] = None

    payment_method: Optional[Literal["check", "direct_deposit", "other"]] = None
    """The payment method."""

    taxes: Optional[List[Optional[UnionMember0PayStatementTax]]] = None
    """The array of taxes objects associated with this pay statement."""

    total_hours: Optional[float] = None
    """The number of hours worked for this pay period"""

    type: Optional[Literal["off_cycle_payroll", "one_time_payment", "regular_payroll"]] = None
    """The type of the payment associated with the pay statement."""


class UnionMember0(BaseModel):
    paging: UnionMember0Paging

    pay_statements: List[UnionMember0PayStatement]


class BatchError(BaseModel):
    code: float

    message: str

    name: str

    finch_code: Optional[str] = None


class UnionMember2(BaseModel):
    code: Literal[202]

    finch_code: Literal["data_sync_in_progress"]

    message: Literal["The pay statements for this payment are being fetched. Please check back later."]

    name: Literal["accepted"]


PayStatementResponseBody: TypeAlias = Union[UnionMember0, BatchError, UnionMember2]
