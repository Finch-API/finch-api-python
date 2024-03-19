# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .benefit_frequency import BenefitFrequency
from .support_per_benefit_type import SupportPerBenefitType

__all__ = ["BenefitFeaturesAndOperations", "SupportedFeatures"]


class SupportedFeatures(BaseModel):
    annual_maximum: Optional[bool] = None
    """Whether the provider supports an annual maximum for this benefit."""

    catch_up: Optional[bool] = None
    """Whether the provider supports catch up for this benefit.

    This field will only be true for retirement benefits.
    """

    company_contribution: Optional[List[Literal["fixed", "percent"]]] = None
    """Supported contribution types.

    An empty array indicates contributions are not supported.
    """

    description: Optional[str] = None

    employee_deduction: Optional[List[Literal["fixed", "percent"]]] = None
    """Supported deduction types.

    An empty array indicates deductions are not supported.
    """

    frequencies: Optional[List[Optional[BenefitFrequency]]] = None
    """The list of frequencies supported by the provider for this benefit"""

    hsa_contribution_limit: Optional[List[Literal["individual", "family"]]] = None
    """Whether the provider supports HSA contribution limits.

    Empty if this feature is not supported for the benefit. This array only has
    values for HSA benefits.
    """


class BenefitFeaturesAndOperations(BaseModel):
    supported_features: Optional[SupportedFeatures] = None

    supported_operations: Optional[SupportPerBenefitType] = None
