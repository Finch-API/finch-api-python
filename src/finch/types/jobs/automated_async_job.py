# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AutomatedAsyncJob"]


class AutomatedAsyncJob(BaseModel):
    completed_at: Optional[datetime] = None
    """The datetime the job completed."""

    created_at: datetime
    """The datetime when the job was created.

    for scheduled jobs, this will be the initial connection time. For ad-hoc jobs,
    this will be the time the creation request was received.
    """

    job_id: str
    """The id of the job that has been created."""

    job_url: str
    """The url that can be used to retrieve the job status"""

    scheduled_at: Optional[datetime] = None
    """The datetime a job is scheduled to be run.

    For scheduled jobs, this datetime can be in the future if the job has not yet
    been enqueued. For ad-hoc jobs, this field will be null.
    """

    started_at: Optional[datetime] = None
    """The datetime a job entered into the job queue."""

    status: Literal["pending", "in_progress", "complete", "error", "reauth_error", "permissions_error"]

    type: Literal["data_sync_all"]
    """Only `data_sync_all` currently supported"""
