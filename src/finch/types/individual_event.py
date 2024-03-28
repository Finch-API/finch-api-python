# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = ["IndividualEvent", "IndividualEventData"]


class IndividualEventData(BaseModel):
    individual_id: Optional[str] = None
    """The ID of the individual related to the event."""


class IndividualEvent(BaseWebhookEvent):
    data: Optional[IndividualEventData] = None

    event_type: Optional[Literal["individual.created", "individual.updated", "individual.deleted"]] = None
