# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AutomatedCreateResponse"]


class AutomatedCreateResponse(BaseModel):
    allowed_refreshes: int
    """The number of allowed refreshes per hour (per hour, fixed window)"""

    remaining_refreshes: int
    """The number of remaining refreshes available (per hour, fixed window)"""

    job_id: Optional[str] = None
    """The id of the job that has been created."""

    job_url: Optional[str] = None
    """The url that can be used to retrieve the job status"""

    retry_at: Optional[str] = None
    """ISO 8601 timestamp indicating when to retry the request"""
