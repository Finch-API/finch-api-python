# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ApplicationListParams"]


class ApplicationListParams(TypedDict, total=False):
    limit: int
    """Number of applications to return (defaults to all)"""

    offset: int
    """Index to start from (defaults to 0)"""
