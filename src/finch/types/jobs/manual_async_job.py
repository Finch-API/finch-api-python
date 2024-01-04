# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ManualAsyncJob"]


class ManualAsyncJob(BaseModel):
    body: Optional[List[object]] = None
    """Specific information about the job, such as individual statuses for batch jobs."""

    job_id: str

    status: Literal["pending", "in_progress", "error", "complete"]
