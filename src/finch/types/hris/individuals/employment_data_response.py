# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel
from ....types.hris.individuals import employment_data

__all__ = ["EmploymentDataResponse"]


class EmploymentDataResponse(BaseModel):
    body: Optional[employment_data.EmploymentData]

    code: Optional[int]

    individual_id: Optional[str]
