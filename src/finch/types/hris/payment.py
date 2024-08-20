# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..money import Money
from ..._models import BaseModel

__all__ = ["Payment", "PayPeriod"]


class PayPeriod(BaseModel):
    end_date: Optional[str] = None

    start_date: Optional[str] = None


class Payment(BaseModel):
    id: Optional[str] = None
    """The unique id for the payment."""

    company_debit: Optional[Money] = None

    debit_date: Optional[str] = None

    employee_taxes: Optional[Money] = None

    employer_taxes: Optional[Money] = None

    gross_pay: Optional[Money] = None

    individual_ids: Optional[List[str]] = None
    """Array of every individual on this payment."""

    net_pay: Optional[Money] = None

    pay_date: Optional[str] = None

    pay_frequencies: Optional[
        List[
            Literal[
                "annually",
                "semi_annually",
                "quarterly",
                "monthly",
                "semi_monthly",
                "bi_weekly",
                "weekly",
                "daily",
                "other",
            ]
        ]
    ] = None
    """List of pay frequencies associated with this payment."""

    pay_group_ids: Optional[List[str]] = None
    """Array of the Finch id (uuidv4) of every pay group associated with this payment."""

    pay_period: Optional[PayPeriod] = None
    """The pay period object."""
