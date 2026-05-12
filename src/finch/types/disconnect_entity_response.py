# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["DisconnectEntityResponse"]


class DisconnectEntityResponse(BaseModel):
    status: str
    """If the request is successful, Finch will return "success" (HTTP 200 status)."""
