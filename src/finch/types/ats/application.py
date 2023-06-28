# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from ...types.ats import stage

__all__ = ["Application", "RejectedReason"]


class RejectedReason(BaseModel):
    text: Optional[str]


class Application(BaseModel):
    id: str

    candidate_id: str

    job_id: str

    offer_id: Optional[str]

    rejected_at: Optional[datetime]

    rejected_reason: Optional[RejectedReason]

    stage: Optional[stage.Stage]
