# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["IndividualUnenrollManyParams"]


class IndividualUnenrollManyParams(TypedDict, total=False):
    individual_ids: List[str]
    """Array of individual_ids to unenroll."""
