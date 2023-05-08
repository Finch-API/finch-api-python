# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import paging
from ..._models import BaseModel
from ...types.hris import pay_statement

__all__ = ["PayStatementResponseBody"]


class PayStatementResponseBody(BaseModel):
    paging: Optional[paging.Paging]

    pay_statements: Optional[List[pay_statement.PayStatement]]
    """The array of pay statements for the current payment."""
