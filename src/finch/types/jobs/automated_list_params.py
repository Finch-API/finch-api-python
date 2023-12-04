# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AutomatedListParams"]


class AutomatedListParams(TypedDict, total=False):
    limit: int
    """Number of items to return"""

    offset: int
    """Index to start from (defaults to 0)"""
