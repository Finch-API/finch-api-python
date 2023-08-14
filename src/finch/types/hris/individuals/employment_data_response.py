# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel
from .employment_data import EmploymentData

__all__ = ["EmploymentDataResponse"]


class EmploymentDataResponse(BaseModel):
    body: Optional[EmploymentData]

    code: Optional[int]

    individual_id: Optional[str]
