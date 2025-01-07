# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["DocumentListParams"]


class DocumentListParams(TypedDict, total=False):
    individual_ids: List[str]
    """Comma-delimited list of stable Finch uuids for each individual.

    If empty, defaults to all individuals
    """

    limit: int
    """Number of documents to return (defaults to all)"""

    offset: int
    """Index to start from (defaults to 0)"""

    types: List[Literal["w4_2020", "w4_2005"]]
    """Comma-delimited list of document types to filter on.

    If empty, defaults to all types
    """
