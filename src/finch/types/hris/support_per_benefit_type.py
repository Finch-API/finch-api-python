# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..shared.operation_support_matrix import OperationSupportMatrix

__all__ = ["SupportPerBenefitType"]


class SupportPerBenefitType(BaseModel):
    company_benefits: Optional[OperationSupportMatrix] = None

    individual_benefits: Optional[OperationSupportMatrix] = None
