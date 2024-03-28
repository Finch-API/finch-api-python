# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = ["PayStatementEvent", "PayStatementEventData"]


class PayStatementEventData(BaseModel):
    individual_id: Optional[str] = None
    """The ID of the individual associated with the pay statement."""

    payment_id: Optional[str] = None
    """The ID of the payment associated with the pay statement."""


class PayStatementEvent(BaseWebhookEvent):
    data: Optional[PayStatementEventData] = None

    event_type: Optional[Literal["pay_statement.created", "pay_statement.updated", "pay_statement.deleted"]] = None
