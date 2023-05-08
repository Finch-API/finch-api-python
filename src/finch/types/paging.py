# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["Paging"]


class Paging(BaseModel):
    count: Optional[int]
    """The total number of elements for the entire query (not just the given page)"""

    offset: Optional[int]
    """The current start index of the returned list of elements"""
