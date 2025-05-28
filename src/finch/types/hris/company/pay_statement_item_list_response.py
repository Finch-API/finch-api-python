# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["PayStatementItemListResponse", "Attributes"]


class Attributes(BaseModel):
    metadata: Optional[Dict[str, Optional[object]]] = None
    """The metadata of the pay statement item derived by the rules engine if available.

    Each attribute will be a key-value pair defined by a rule.
    """

    employer: Optional[bool] = None
    """`true` if the amount is paid by the employers.

    This field is only available for taxes.
    """

    pre_tax: Optional[bool] = None
    """`true` if the pay statement item is pre-tax.

    This field is only available for employee deductions.
    """

    type: Optional[str] = None
    """The type of the pay statement item."""


class PayStatementItemListResponse(BaseModel):
    attributes: Attributes
    """The attributes of the pay statement item."""

    category: Literal["earnings", "taxes", "employee_deductions", "employer_contributions"]
    """The category of the pay statement item."""

    name: str
    """The name of the pay statement item."""
