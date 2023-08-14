# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel
from .pay_statement_response_body import PayStatementResponseBody

__all__ = ["PayStatementResponse"]


class PayStatementResponse(BaseModel):
    body: Optional[PayStatementResponseBody]

    code: Optional[int]

    payment_id: Optional[str]
