# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from ...shared import ConnectionStatusType

__all__ = ["AccountUpdateParams"]


class AccountUpdateParams(TypedDict, total=False):
    connection_status: ConnectionStatusType
