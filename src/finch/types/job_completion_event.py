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
            "job.benefit_create.updated",
            "job.benefit_enroll.updated",
            "job.benefit_register.updated",
            "job.benefit_unenroll.updated",
            "job.benefit_update.updated",
            "job.data_sync_all.updated",
        ]
    ] = None
