# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PayGroupListResponse"]


class PayGroupListResponse(BaseModel):
    id: Optional[str] = None
    """Finch id (uuidv4) for the pay group"""

    name: Optional[str] = None
    """Name of the pay group"""

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
    """List of pay frequencies associated with this pay group"""
