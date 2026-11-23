# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ManualAsyncJob"]


class ManualAsyncJob(BaseModel):
    body: Optional[List[Optional[object]]] = None
    """Specific information about the job, such as individual statuses for batch jobs."""

    job_id: str

    sla_deadline: datetime
    """The datetime by which the job is expected to be completed.

    Only returned for jobs that include requests Finch processes manually
    (assisted).
    """

    status: Literal["pending", "in_progress", "error", "complete"]
