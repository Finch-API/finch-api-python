# File generated from our OpenAPI spec by Stainless.

from ..._models import BaseModel

__all__ = ["PaymentCreateResponse"]


class PaymentCreateResponse(BaseModel):
    pay_date: str
    """The date of the payment."""

    payment_id: str
    """The ID of the payment."""
