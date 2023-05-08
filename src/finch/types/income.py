# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Income"]


class Income(BaseModel):
    amount: Optional[int]
    """The income amount in cents."""

    currency: Optional[str]
    """The currency code."""

    effective_date: Optional[str]
    """The date the income amount went into effect."""

    unit: Optional[
        Literal["yearly", "quarterly", "monthly", "semi_monthly", "bi_weekly", "weekly", "daily", "hourly", "fixed"]
    ]
    """The income unit of payment.

    Options: `yearly`, `quarterly`, `monthly`, `semi_monthly`, `bi_weekly`,
    `weekly`, `daily`, `hourly`, and `fixed`.
    """
