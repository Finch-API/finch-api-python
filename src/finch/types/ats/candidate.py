# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Candidate", "Email", "PhoneNumber"]


class Email(BaseModel):
    data: Optional[str]

    type: Optional[str]


class PhoneNumber(BaseModel):
    data: Optional[str]

    type: Optional[str]


class Candidate(BaseModel):
    id: str

    application_ids: List[str]
    """Array of Finch uuids corresponding to `application`s for this individual"""

    created_at: datetime

    emails: List[Email]

    first_name: Optional[str]

    full_name: Optional[str]

    last_activity_at: datetime

    last_name: Optional[str]

    phone_numbers: List[PhoneNumber]
