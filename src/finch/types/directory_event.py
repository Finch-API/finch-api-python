# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = ["DirectoryEvent", "DirectoryEventData"]


class DirectoryEventData(BaseModel):
    individual_id: Optional[str] = None
    """The ID of the individual related to the event."""


class DirectoryEvent(BaseWebhookEvent):
    data: Optional[DirectoryEventData] = None

    event_type: Optional[Literal["directory.created", "directory.updated", "directory.deleted"]] = None
