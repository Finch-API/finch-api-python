# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..shared import OperationSupportMatrix
from ..._models import BaseModel

__all__ = ["SupportPerBenefitType"]


class SupportPerBenefitType(BaseModel):
    company_benefits: Optional[OperationSupportMatrix] = None

    individual_benefits: Optional[OperationSupportMatrix] = None
