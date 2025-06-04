# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PayGroupListResponse"]


class PayGroupListResponse(BaseModel):
    id: str
    """Finch id (uuidv4) for the pay group"""

    name: str
    """Name of the pay group"""

    pay_frequencies: List[
        Literal[
            "annually", "bi_weekly", "daily", "monthly", "other", "quarterly", "semi_annually", "semi_monthly", "weekly"
        ]
    ]
    """List of pay frequencies associated with this pay group"""
