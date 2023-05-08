# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["IndividualEnrollManyParam"]


class IndividualEnrollManyParam(TypedDict, total=False):
    configuration: object

    individual_id: str
    """Finch id (uuidv4) for the individual to enroll"""


IndividualEnrollManyParams = List[IndividualEnrollManyParam]
