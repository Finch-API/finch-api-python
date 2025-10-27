# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ....._types import SequenceNotStr

__all__ = ["RuleListParams"]


class RuleListParams(TypedDict, total=False):
    entity_ids: SequenceNotStr[str]
    """The entity IDs to retrieve rules for."""
