# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["JobCreateParams"]


class JobCreateParams(TypedDict, total=False):
    type: Required[Literal["data_sync_all"]]
    """The type of job to start. Currently the only supported type is `data_sync_all`"""
