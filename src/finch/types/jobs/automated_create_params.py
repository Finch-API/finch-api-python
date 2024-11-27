# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["AutomatedCreateParams", "DataSyncAll", "W4FormEmployeeSync"]


class DataSyncAll(TypedDict, total=False):
    type: Required[Literal["data_sync_all"]]
    """The type of job to start."""


class W4FormEmployeeSync(TypedDict, total=False):
    individual_id: Required[str]
    """The unique ID of the individual for W-4 data sync."""

    type: Required[Literal["w4_form_employee_sync"]]
    """The type of job to start."""


AutomatedCreateParams: TypeAlias = Union[DataSyncAll, W4FormEmployeeSync]
