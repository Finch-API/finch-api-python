# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["OperationSupport"]

OperationSupport: TypeAlias = Literal[
    "supported", "not_supported_by_finch", "not_supported_by_provider", "client_access_only"
]
