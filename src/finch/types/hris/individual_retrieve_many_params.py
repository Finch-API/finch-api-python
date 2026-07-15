# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["IndividualRetrieveManyParams", "Request", "Options"]


class IndividualRetrieveManyParams(TypedDict, total=False):
    requests: Required[Iterable[Request]]
    """The array of batch requests. Maximum 10000 items per request."""

    entity_ids: SequenceNotStr[str]
    """The entity IDs to specify which entities' data to access.

    Provide exactly one entity ID per request; a maximum of one is accepted.
    """

    options: Optional[Options]


class Request(TypedDict, total=False):
    individual_id: Required[str]


class Options(TypedDict, total=False):
    include: SequenceNotStr[str]
