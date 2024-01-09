# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SandboxJobConfiguration"]


class SandboxJobConfiguration(BaseModel):
    completion_status: Literal["complete", "reauth_error", "permissions_error", "error"]

    type: Literal["data_sync_all"]
