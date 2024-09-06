# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RequestForwardingForwardParams"]


class RequestForwardingForwardParams(TypedDict, total=False):
    method: Required[str]
    """The HTTP method for the forwarded request.

    Valid values include: `GET` , `POST` , `PUT` , `DELETE` , and `PATCH`.
    """

    route: Required[str]
    """The URL route path for the forwarded request.

    This value must begin with a forward-slash ( / ) and may only contain
    alphanumeric characters, hyphens, and underscores.
    """

    data: Optional[str]
    """The body for the forwarded request.

    This value must be specified as either a string or a valid JSON object.
    """

    headers: Optional[object]
    """The HTTP headers to include on the forwarded request.

    This value must be specified as an object of key-value pairs. Example:
    `{"Content-Type": "application/xml", "X-API-Version": "v1" }`
    """

    params: Optional[object]
    """The query parameters for the forwarded request.

    This value must be specified as a valid JSON object rather than a query string.
    """
