# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .benefit_frequency import BenefitFrequency

__all__ = ["SupportedBenefit"]


class SupportedBenefit(BaseModel):
    annual_maximum: Optional[bool] = None
    """Whether the provider supports an annual maximum for this benefit."""

    company_contribution: Optional[List[Optional[Literal["fixed", "percent"]]]] = None
    """Supported contribution types.

    An empty array indicates contributions are not supported.
    """

    description: Optional[str] = None

    employee_deduction: Optional[List[Optional[Literal["fixed", "percent"]]]] = None
    """Supported deduction types.

    An empty array indicates deductions are not supported.
    """

    frequencies: List[Optional[BenefitFrequency]]
    """The list of frequencies supported by the provider for this benefit"""

    catch_up: Optional[bool] = None
    """Whether the provider supports catch up for this benefit.

    This field will only be true for retirement benefits.
    """

    hsa_contribution_limit: Optional[List[Optional[Literal["family", "individual"]]]] = None
    """Whether the provider supports HSA contribution limits.

    Empty if this feature is not supported for the benefit. This array only has
    values for HSA benefits.
    """
