# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..paging import Paging
from ..._models import BaseModel
from .pay_statement import PayStatement

__all__ = ["PayStatementResponseBody"]


class PayStatementResponseBody(BaseModel):
    paging: Optional[Paging]

    pay_statements: Optional[List[PayStatement]]
    """The array of pay statements for the current payment."""
