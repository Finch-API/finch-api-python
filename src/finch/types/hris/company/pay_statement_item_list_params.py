# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PayStatementItemListParams"]


class PayStatementItemListParams(TypedDict, total=False):
    categories: List[Literal["earnings", "taxes", "employee_deductions", "employer_contributions"]]
    """Comma-delimited list of pay statement item categories to filter on.

    If empty, defaults to all categories.
    """

    end_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    The end date to retrieve pay statement items by via their last seen pay date in
    `YYYY-MM-DD` format.
    """

    name: str
    """Case-insensitive partial match search by pay statement item name."""

    start_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    The start date to retrieve pay statement items by via their last seen pay date
    (inclusive) in `YYYY-MM-DD` format.
    """

    type: str
    """String search by pay statement item type."""
