# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel
from ...types.hris import pay_statement_response_body

__all__ = ["PayStatementResponse"]


class PayStatementResponse(BaseModel):
    body: Optional[pay_statement_response_body.PayStatementResponseBody]

    code: Optional[int]

    payment_id: Optional[str]
