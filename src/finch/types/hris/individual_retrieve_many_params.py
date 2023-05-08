# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["IndividualRetrieveManyParams", "Request", "Options"]


class Request(TypedDict, total=False):
    individual_id: str


class Options(TypedDict, total=False):
    include: List[str]


class IndividualRetrieveManyParams(TypedDict, total=False):
    options: Optional[Options]

    requests: List[Request]
