# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["BaseWebhookEvent"]


class BaseWebhookEvent(BaseModel):
    account_id: str
    """Unique Finch id of the employer account that was used to make this connection."""

    company_id: str
    """Unique Finch id of the company for which data has been updated."""
