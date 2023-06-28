# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import money
from ..._models import BaseModel

__all__ = ["Payment", "PayPeriod"]


class PayPeriod(BaseModel):
    end_date: Optional[str]

    start_date: Optional[str]


class Payment(BaseModel):
    id: Optional[str]
    """The unique id for the payment."""

    company_debit: Optional[money.Money]

    debit_date: Optional[str]

    employee_taxes: Optional[money.Money]

    employer_taxes: Optional[money.Money]

    gross_pay: Optional[money.Money]

    individual_ids: Optional[List[str]]
    """Array of every individual on this payment."""

    net_pay: Optional[money.Money]

    pay_date: Optional[str]

    pay_period: Optional[PayPeriod]
    """The pay period object."""
