# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["JobCreateResponse"]


class JobCreateResponse(BaseModel):
    allowed_refreshes: int
    """The number of allowed refreshes per hour (per hour, fixed window)"""

    job_id: str
    """The id of the job that has been created."""

    job_url: str
    """The url that can be used to retrieve the job status"""

    remaining_refreshes: int
    """The number of remaining refreshes available (per hour, fixed window)"""
