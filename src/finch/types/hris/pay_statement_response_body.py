# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .pay_statement import PayStatement
from ..shared.paging import Paging

__all__ = ["PayStatementResponseBody"]


class PayStatementResponseBody(BaseModel):
    paging: Optional[Paging] = None

    pay_statements: Optional[List[PayStatement]] = None
    """The array of pay statements for the current payment."""
