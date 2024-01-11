# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from typing_extensions import Literal

from .base_webhook_event import BaseWebhookEvent

__all__ = ["CompanyEvent"]


class CompanyEvent(BaseWebhookEvent):
    data: Optional[Dict[str, object]] = None

    event_type: Optional[Literal["company.updated"]] = None
