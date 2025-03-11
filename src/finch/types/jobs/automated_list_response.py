# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .automated_async_job import AutomatedAsyncJob

__all__ = ["AutomatedListResponse", "Meta", "MetaQuotas", "MetaQuotasDataSyncAll"]


class MetaQuotasDataSyncAll(BaseModel):
    allowed_refreshes: Optional[int] = None

    remaining_refreshes: Optional[int] = None


class MetaQuotas(BaseModel):
    data_sync_all: Optional[MetaQuotasDataSyncAll] = None


class Meta(BaseModel):
    quotas: Optional[MetaQuotas] = None
    """Information about remaining quotas for this connection.

    Only applicable for customers opted in to use Finch's Data Sync Refresh endpoint
    (`POST /jobs/automated`). Please contact a Finch representative for more
    details.
    """


class AutomatedListResponse(BaseModel):
    data: List[AutomatedAsyncJob]

    meta: Meta
