# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["SessionReauthenticateResponse"]


class SessionReauthenticateResponse(BaseModel):
    connect_url: str
    """The Connect URL to redirect the user to for reauthentication"""

    session_id: str
    """The unique identifier for the created connect session"""
