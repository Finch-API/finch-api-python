# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = ["JobCompletionEvent", "JobCompletionEventData"]


class JobCompletionEventData(BaseModel):
    job_id: str
    """The id of the job which has completed."""

    job_url: str
    """The url to query the result of the job."""


class JobCompletionEvent(BaseWebhookEvent):
    data: Optional[JobCompletionEventData] = None

    event_type: Optional[
        Literal[
            "job.benefit_create.completed",
            "job.benefit_enroll.completed",
            "job.benefit_register.completed",
            "job.benefit_unenroll.completed",
            "job.benefit_update.completed",
            "job.data_sync_all.completed",
        ]
    ] = None
