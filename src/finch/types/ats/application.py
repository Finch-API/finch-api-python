# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from .stage import Stage
from ..._models import BaseModel

__all__ = ["Application", "RejectedReason"]


class RejectedReason(BaseModel):
    text: Optional[str] = None


class Application(BaseModel):
    id: str

    candidate_id: str

    job_id: str

    offer_id: Optional[str]

    rejected_at: Optional[datetime]

    rejected_reason: Optional[RejectedReason]

    stage: Optional[Stage]
