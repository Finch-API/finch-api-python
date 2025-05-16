# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MoneyParam"]


class MoneyParam(TypedDict, total=False):
    amount: Optional[int]
    """Amount for money object (in cents)"""

    currency: str
