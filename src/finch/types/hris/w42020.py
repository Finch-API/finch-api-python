# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["W42020", "Data"]


class Data(BaseModel):
    amount_for_other_dependents: int
    """
    Amount claimed for dependents other than qualifying children under 17 (in
    cents).
    """

    amount_for_qualifying_children_under_17: int
    """Amount claimed for dependents under 17 years old (in cents)."""

    deductions: int
    """Deductible expenses (in cents)."""

    extra_withholding: int
    """Additional withholding amount (in cents)."""

    filing_status: Optional[
        Literal[
            "head_of_household",
            "married_filing_jointly_or_qualifying_surviving_spouse",
            "single_or_married_filing_separately",
        ]
    ] = None
    """The individual's filing status for tax purposes."""

    individual_id: str
    """The unique identifier for the individual associated with this document."""

    other_income: int
    """Additional income from sources outside of primary employment (in cents)."""

    total_claim_dependent_and_other_credits: int
    """Total amount claimed for dependents and other credits (in cents)."""


class W42020(BaseModel):
    data: Data
    """Detailed information specific to the 2020 W4 form."""

    type: Literal["w4_2020"]
    """Specifies the form type, indicating that this document is a 2020 W4 form."""

    year: float
    """The tax year this W4 document applies to."""
