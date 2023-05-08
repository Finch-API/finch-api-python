# File generated from our OpenAPI spec by Stainless.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Offer"]


class Offer(BaseModel):
    application_id: str

    candidate_id: str

    created_at: datetime

    id: str

    job_id: str

    status: Literal[
        "signed", "rejected", "draft", "approval-sent", "approved", "sent", "sent-manually", "opened", "archived"
    ]

    updated_at: datetime
