# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Stage"]


class Stage(BaseModel):
    id: Optional[str] = None

    job_id: Optional[str] = None
    """The job id that this stage applies to, if applicable.

    Not all systems enumerate stages specific to jobs.
    """

    name: Optional[str] = None
