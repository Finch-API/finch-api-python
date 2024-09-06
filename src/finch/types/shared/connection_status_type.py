# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ConnectionStatusType"]

ConnectionStatusType: TypeAlias = Literal[
    "pending", "processing", "connected", "error_no_account_setup", "error_permissions", "reauth"
]
