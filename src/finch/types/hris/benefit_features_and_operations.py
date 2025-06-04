# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .supported_benefit import SupportedBenefit
from .support_per_benefit_type import SupportPerBenefitType

__all__ = ["BenefitFeaturesAndOperations"]


class BenefitFeaturesAndOperations(BaseModel):
    supported_features: Optional[SupportedBenefit] = None

    supported_operations: Optional[SupportPerBenefitType] = None
