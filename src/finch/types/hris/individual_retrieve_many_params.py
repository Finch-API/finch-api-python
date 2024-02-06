# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import TypedDict

__all__ = ["IndividualRetrieveManyParams", "Options", "Request"]


class IndividualRetrieveManyParams(TypedDict, total=False):
    options: Optional[Options]

    requests: Iterable[Request]


class Options(TypedDict, total=False):
    include: List[str]


class Request(TypedDict, total=False):
    individual_id: str
