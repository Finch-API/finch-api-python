# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConnectionCreateParams"]


class ConnectionCreateParams(TypedDict, total=False):
    provider_id: Required[str]
    """The provider associated with the connection"""

    authentication_type: Literal["credential", "api_token", "oauth", "assisted"]

    employee_size: int
    """Optional: the size of the employer to be created with this connection.

    Defaults to 20. Note that if this is higher than 100, historical payroll data
    will not be generated, and instead only one pay period will be created.
    """

    products: List[str]
