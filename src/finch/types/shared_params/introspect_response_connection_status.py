# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

__all__ = ["IntrospectResponseConnectionStatus"]

IntrospectResponseConnectionStatus = Literal[
    "pending", "processing", "connected", "error_no_account_setup", "error_permissions", "reauth"
]