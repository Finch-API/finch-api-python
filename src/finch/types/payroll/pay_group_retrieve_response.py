# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PayGroupRetrieveResponse"]


class PayGroupRetrieveResponse(BaseModel):
    id: str
    """Finch id (uuidv4) for the pay group"""

    individual_ids: List[str]

    name: str
    """Name of the pay group"""

    pay_frequencies: List[
        Literal[
            "annually", "semi_annually", "quarterly", "monthly", "semi_monthly", "bi_weekly", "weekly", "daily", "other"
        ]
    ]
    """List of pay frequencies associated with this pay group"""
