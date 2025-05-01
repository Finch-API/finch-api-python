# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .employment_data import EmploymentData

__all__ = ["EmploymentDataResponse"]


class EmploymentDataResponse(BaseModel):
    body: EmploymentData

    code: int

    individual_id: str
    """A stable Finch `id` (UUID v4) for an individual in the company."""
