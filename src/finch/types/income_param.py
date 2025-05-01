# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["IncomeParam"]


class IncomeParam(TypedDict, total=False):
    amount: Required[Optional[int]]
    """The income amount in cents."""

    currency: Required[Optional[str]]
    """The currency code."""

    effective_date: Required[Optional[str]]
    """The date the income amount went into effect."""

    unit: Required[
        Optional[
            Literal["yearly", "quarterly", "monthly", "semi_monthly", "bi_weekly", "weekly", "daily", "hourly", "fixed"]
        ]
    ]
    """The income unit of payment.

    Options: `yearly`, `quarterly`, `monthly`, `semi_monthly`, `bi_weekly`,
    `weekly`, `daily`, `hourly`, and `fixed`.
    """
