# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = ["EmploymentEvent", "EmploymentEventData"]


class EmploymentEventData(BaseModel):
    individual_id: Optional[str] = None
    """The ID of the individual related to the event."""


class EmploymentEvent(BaseWebhookEvent):
    data: Optional[EmploymentEventData] = None

    event_type: Optional[Literal["employment.created", "employment.updated", "employment.deleted"]] = None
