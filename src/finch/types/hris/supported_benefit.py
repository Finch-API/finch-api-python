# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ...types.hris import benefit_type

__all__ = ["SupportedBenefit"]


class SupportedBenefit(BaseModel):
    annual_maximum: Optional[bool]
    """Whether the provider supports an annual maximum for this benefit."""

    catch_up: Optional[bool]
    """Whether the provider supports catch up for this benefit.

    This field will only be true for retirement benefits.
    """

    company_contribution: Optional[List[Literal["fixed", "percent"]]]
    """Supported contribution types.

    An empty array indicates contributions are not supported.
    """

    description: Optional[str]

    employee_deduction: Optional[List[Literal["fixed", "percent"]]]
    """Supported deduction types.

    An empty array indicates deductions are not supported.
    """

    frequencies: Optional[List[Optional[Literal["one_time", "every_paycheck"]]]]
    """The list of frequencies supported by the provider for this benefit"""

    hsa_contribution_limit: Optional[List[Literal["individual", "family"]]]
    """Whether the provider supports HSA contribution limits.

    Empty if this feature is not supported for the benefit. This array only has
    values for HSA benefits.
    """

    type: Optional[benefit_type.BenefitType]
    """Type of benefit."""
