# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["PayStatementItemListResponse", "Attributes"]


class Attributes(BaseModel):
    employer: Optional[bool] = None
    """`true` if the amount is paid by the employers.

    This field is only available for taxes.
    """

    metadata: Optional[object] = None
    """The metadata of the pay statement item derived by the rules engine if available.

    Each attribute will be a key-value pair defined by a rule.
    """

    pre_tax: Optional[bool] = None
    """`true` if the pay statement item is pre-tax.

    This field is only available for employee deductions.
    """

    type: Optional[str] = None
    """The type of the pay statement item."""


class PayStatementItemListResponse(BaseModel):
    attributes: Optional[Attributes] = None
    """The attributes of the pay statement item."""

    category: Optional[Literal["earnings", "taxes", "employee_deductions", "employer_contributions"]] = None
    """The category of the pay statement item."""

    name: Optional[str] = None
    """The name of the pay statement item."""
