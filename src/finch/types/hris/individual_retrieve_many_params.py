# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["IndividualRetrieveManyParams", "Options", "Request"]


class IndividualRetrieveManyParams(TypedDict, total=False):
    options: Optional[Options]

    requests: Iterable[Request]


class Options(TypedDict, total=False):
    include: SequenceNotStr[str]


class Request(TypedDict, total=False):
    individual_id: str
