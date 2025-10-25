# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["IndividualRetrieveManyParams", "Options", "Request"]


class IndividualRetrieveManyParams(TypedDict, total=False):
    entity_ids: Required[SequenceNotStr[str]]
    """The entity IDs to specify which entities' data to access."""

    options: Optional[Options]

    requests: Iterable[Request]


class Options(TypedDict, total=False):
    include: SequenceNotStr[str]


class Request(TypedDict, total=False):
    individual_id: str
