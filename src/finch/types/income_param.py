# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IncomeParam"]


class IncomeParam(TypedDict, total=False):
    amount: Required[Optional[int]]
    """The income amount in cents."""

    currency: Required[Optional[str]]
    """The currency code."""

    effective_date: Required[Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]]
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
