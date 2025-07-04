# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Paging"]


class Paging(BaseModel):
    offset: int
    """The current start index of the returned list of elements"""

    count: Optional[int] = None
    """The total number of elements for the entire query (not just the given page)"""
