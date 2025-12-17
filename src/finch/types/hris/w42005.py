# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["W42005", "Data"]


class Data(BaseModel):
    """Detailed information specific to the 2005 W4 form."""

    additional_withholding: int
    """Additional withholding amount (in cents)."""

    exemption: Optional[Literal["exempt", "non_exempt"]] = None
    """Indicates exemption status from federal tax withholding."""

    filing_status: Optional[Literal["married", "married_but_withhold_at_higher_single_rate", "single"]] = None
    """The individual's filing status for tax purposes."""

    individual_id: str
    """The unique identifier for the individual associated with this 2005 W4 form."""

    total_number_of_allowances: int
    """Total number of allowances claimed (in cents)."""


class W42005(BaseModel):
    """
    A 2005 version of the W-4 tax form containing information on an individual's filing status, dependents, and withholding details.
    """

    data: Data
    """Detailed information specific to the 2005 W4 form."""

    type: Literal["w4_2005"]
    """Specifies the form type, indicating that this document is a 2005 W4 form."""

    year: float
    """The tax year this W4 document applies to."""
