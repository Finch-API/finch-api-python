# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PayStatementDataSyncInProgress"]


class PayStatementDataSyncInProgress(BaseModel):
    code: Literal[202]

    finch_code: Literal["data_sync_in_progress"]

    message: Literal["The pay statements for this payment are being fetched. Please check back later."]

    name: Literal["accepted"]
