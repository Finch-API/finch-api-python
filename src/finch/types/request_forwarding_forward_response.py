# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RequestForwardingForwardResponse", "Request"]


class Request(BaseModel):
    method: str
    """The HTTP method that was specified for the forwarded request.

    Valid values include: `GET` , `POST` , `PUT` , `DELETE` , and `PATCH`.
    """

    route: str
    """The URL route path that was specified for the forwarded request."""

    data: Union[str, Dict[str, Optional[object]], None] = None
    """The body that was specified for the forwarded request."""

    headers: Optional[Dict[str, str]] = None
    """The HTTP headers that were specified for the forwarded request."""

    params: Optional[Dict[str, Optional[object]]] = None
    """The query parameters that were specified for the forwarded request."""


class RequestForwardingForwardResponse(BaseModel):
    request: Request
    """
    An object containing details of your original forwarded request, for your ease
    of reference.
    """

    status_code: int = FieldInfo(alias="statusCode")
    """
    The HTTP status code of the forwarded request's response, exactly received from
    the underlying integration's API. This value will be returned as an integer.
    """

    data: Optional[str] = None
    """
    A string representation of the HTTP response body of the forwarded request's
    response received from the underlying integration's API. This field may be null
    in the case where the upstream system's response is empty.
    """

    headers: Optional[Dict[str, Optional[object]]] = None
    """
    The HTTP headers of the forwarded request's response, exactly as received from
    the underlying integration's API.
    """
