# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["W42020", "Data"]


class Data(BaseModel):
    amount_for_other_dependents: Optional[int] = None
    """
    Amount claimed for dependents other than qualifying children under 17 (in
    cents).
    """

    amount_for_qualifying_children_under_17: Optional[int] = None
    """Amount claimed for dependents under 17 years old (in cents)."""

    deductions: Optional[int] = None
    """Deductible expenses (in cents)."""

    extra_withholding: Optional[int] = None
    """Additional withholding amount (in cents)."""

    filing_status: Optional[
        Literal[
            "head_of_household",
            "married_filing_jointly_or_qualifying_surviving_spouse",
            "single_or_married_filing_separately",
        ]
    ] = None
    """The individual's filing status for tax purposes."""

    individual_id: Optional[str] = None
    """The unique identifier for the individual associated with this document."""

    other_income: Optional[int] = None
    """Additional income from sources outside of primary employment (in cents)."""

    total_claim_dependent_and_other_credits: Optional[int] = None
    """Total amount claimed for dependents and other credits (in cents)."""


class W42020(BaseModel):
    data: Optional[Data] = None
    """Detailed information specific to the 2020 W4 form."""

    type: Optional[Literal["w4_2020"]] = None
    """Specifies the form type, indicating that this document is a 2020 W4 form."""

    year: Optional[float] = None
    """The tax year this W4 document applies to."""
