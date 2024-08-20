# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConfigurationUpdateParams"]


class ConfigurationUpdateParams(TypedDict, total=False):
    completion_status: Required[Literal["complete", "reauth_error", "permissions_error", "error"]]

    type: Required[Literal["data_sync_all"]]
