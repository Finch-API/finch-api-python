# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

__all__ = ["ConnectionStatusType"]

ConnectionStatusType = Literal[
    "pending", "processing", "connected", "error_no_account_setup", "error_permissions", "reauth"
]
