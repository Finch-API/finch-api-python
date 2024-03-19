# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PayStatementRetrieveManyParams", "Request"]


class PayStatementRetrieveManyParams(TypedDict, total=False):
    requests: Required[Iterable[Request]]
    """The array of batch requests."""


class Request(TypedDict, total=False):
    payment_id: Required[str]
    """A stable Finch `id` (UUID v4) for a payment."""

    limit: int
    """Number of pay statements to return (defaults to all)."""

    offset: int
    """Index to start from."""
