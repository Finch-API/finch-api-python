# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["EmploymentRetrieveManyParams", "Request"]


class EmploymentRetrieveManyParams(TypedDict, total=False):
    requests: Required[Iterable[Request]]
    """The array of batch requests."""


class Request(TypedDict, total=False):
    individual_id: Required[str]
    """A stable Finch `id` (UUID v4) for an individual in the company.

    There is no limit to the number of `individual_id` to send per request. It is
    preferantial to send all ids in a single request for Finch to optimize provider
    rate-limits.
    """
