# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .pay_statement_response_body import PayStatementResponseBody

__all__ = ["PayStatementResponse"]


class PayStatementResponse(BaseModel):
    body: PayStatementResponseBody

    code: int

    payment_id: str
