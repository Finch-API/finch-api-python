# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .pay_statement_response_body import PayStatementResponseBody
from .pay_statement_data_sync_in_progress import PayStatementDataSyncInProgress

__all__ = ["PayStatementResponse", "Body", "BodyBatchError"]


class BodyBatchError(BaseModel):
    code: float

    message: str

    name: str

    finch_code: Optional[str] = None


Body: TypeAlias = Union[PayStatementResponseBody, BodyBatchError, PayStatementDataSyncInProgress]


class PayStatementResponse(BaseModel):
    body: Body

    code: int

    payment_id: str
