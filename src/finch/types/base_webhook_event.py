# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BaseWebhookEvent"]


class BaseWebhookEvent(BaseModel):
    account_id: str
    """
    [DEPRECATED] Unique Finch ID of the employer account used to make this
    connection. Use `connection_id` instead to identify the connection associated
    with this event.
    """

    company_id: str
    """Unique Finch ID of the company for which data has been updated."""

    connection_id: Optional[str] = None
    """Unique Finch ID of the connection associated with the webhook event."""

    entity_id: Optional[str] = None
    """Unique Finch id of the entity for which data has been updated."""
