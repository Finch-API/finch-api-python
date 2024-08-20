# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PaymentListParams"]


class PaymentListParams(TypedDict, total=False):
    end_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """
    The end date to retrieve payments by a company (inclusive) in `YYYY-MM-DD`
    format.
    """

    start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """
    The start date to retrieve payments by a company (inclusive) in `YYYY-MM-DD`
    format.
    """
