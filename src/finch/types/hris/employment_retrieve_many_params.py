# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["EmploymentRetrieveManyParams", "Request"]


class EmploymentRetrieveManyParams(TypedDict, total=False):
    requests: Required[Iterable[Request]]
    """The array of batch requests. Maximum 10000 items per request."""

    entity_ids: SequenceNotStr[str]
    """The entity IDs to specify which entities' data to access."""


class Request(TypedDict, total=False):
    individual_id: Required[str]
    """A stable Finch `id` (UUID v4) for an individual in the company."""
