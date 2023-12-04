# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["Paging"]


class Paging(TypedDict, total=False):
    count: int
    """The total number of elements for the entire query (not just the given page)"""

    offset: int
    """The current start index of the returned list of elements"""
