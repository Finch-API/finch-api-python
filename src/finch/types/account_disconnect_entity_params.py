# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AccountDisconnectEntityParams"]


class AccountDisconnectEntityParams(TypedDict, total=False):
    entity_ids: Required[SequenceNotStr[str]]
    """Array of entity UUIDs to disconnect. At least one entity ID must be provided."""
