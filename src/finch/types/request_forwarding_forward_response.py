# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RequestForwardingForwardResponse", "Request"]


class Request(BaseModel):
    data: Optional[str] = None
    """The body that was specified for the forwarded request.

    If a value was not specified in the original request, this value will be
    returned as null ; otherwise, this value will always be returned as a string.
    """

    headers: Optional[object] = None
    """The specified HTTP headers that were included in the forwarded request.

    If no headers were specified, this will be returned as `null`.
    """

    method: str
    """The HTTP method that was specified for the forwarded request.

    Valid values include: `GET` , `POST` , `PUT` , `DELETE` , and `PATCH`.
    """

    params: Optional[object] = None
    """The query parameters that were included in the forwarded request.

    If no query parameters were specified, this will be returned as `null`.
    """

    route: str
    """The URL route path that was specified for the forwarded request."""


class RequestForwardingForwardResponse(BaseModel):
    data: Optional[str] = None
    """
    A string representation of the HTTP response body of the forwarded request’s
    response received from the underlying integration’s API. This field may be null
    in the case where the upstream system’s response is empty.
    """

    headers: Optional[object] = None
    """
    The HTTP headers of the forwarded request’s response, exactly as received from
    the underlying integration’s API.
    """

    request: Request
    """
    An object containing details of your original forwarded request, for your ease
    of reference.
    """

    status_code: int = FieldInfo(alias="statusCode")
    """
    The HTTP status code of the forwarded request’s response, exactly received from
    the underlying integration’s API. This value will be returned as an integer.
    """
