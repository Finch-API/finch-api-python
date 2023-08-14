# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..money import Money
from ..._models import BaseModel

__all__ = ["Payment", "PayPeriod"]


class PayPeriod(BaseModel):
    end_date: Optional[str]

    start_date: Optional[str]


class Payment(BaseModel):
    id: Optional[str]
    """The unique id for the payment."""

    company_debit: Optional[Money]

    debit_date: Optional[str]

    employee_taxes: Optional[Money]

    employer_taxes: Optional[Money]

    gross_pay: Optional[Money]

    individual_ids: Optional[List[str]]
    """Array of every individual on this payment."""

    net_pay: Optional[Money]

    pay_date: Optional[str]

    pay_period: Optional[PayPeriod]
    """The pay period object."""
