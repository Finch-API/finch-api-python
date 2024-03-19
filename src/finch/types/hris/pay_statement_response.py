# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .pay_statement_response_body import PayStatementResponseBody

__all__ = ["PayStatementResponse"]


class PayStatementResponse(BaseModel):
    body: Optional[PayStatementResponseBody] = None

    code: Optional[int] = None

    payment_id: Optional[str] = None
