# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = ["PaymentEvent", "PaymentEventData"]


class PaymentEventData(BaseModel):
    pay_date: str
    """The date of the payment."""

    payment_id: str
    """The ID of the payment."""


class PaymentEvent(BaseWebhookEvent):
    data: Optional[PaymentEventData] = None

    event_type: Optional[Literal["payment.created", "payment.updated", "payment.deleted"]] = None
