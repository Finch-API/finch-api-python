# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

__all__ = ["ConnectionStatusType"]

ConnectionStatusType = Literal[
    "pending", "processing", "connected", "error_no_account_setup", "error_permissions", "reauth"
]
