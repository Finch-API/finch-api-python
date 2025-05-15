# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .pay_statement import PayStatement

__all__ = ["PayStatementResponseBody", "Paging"]


class Paging(BaseModel):
    offset: int
    """The current start index of the returned list of elements"""

    count: Optional[int] = None
    """The total number of elements for the entire query (not just the given page)"""


class PayStatementResponseBody(BaseModel):
    paging: Paging

    pay_statements: List[PayStatement]
