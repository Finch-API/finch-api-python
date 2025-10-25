# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["IndividualUnenrollManyParams"]


class IndividualUnenrollManyParams(TypedDict, total=False):
    entity_ids: Required[SequenceNotStr[str]]
    """The entity IDs to specify which entities' data to access."""

    individual_ids: SequenceNotStr[str]
    """Array of individual_ids to unenroll."""
