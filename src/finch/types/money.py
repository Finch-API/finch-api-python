# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["Money"]


class Money(BaseModel):
    amount: Optional[int] = None
    """Amount for money object (in cents)"""

    currency: Optional[str] = None
