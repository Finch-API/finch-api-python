# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["DirectoryListParams"]


class DirectoryListParams(TypedDict, total=False):
    entity_ids: SequenceNotStr[str]
    """The entity IDs to specify which entities' data to access."""

    limit: int
    """Number of employees to return (defaults to all)"""

    offset: int
    """Index to start from (defaults to 0)"""
