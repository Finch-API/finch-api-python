# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional

from ..._models import BaseModel
from .benefit_features_and_operations import BenefitFeaturesAndOperations

__all__ = ["BenefitsSupport"]


class BenefitsSupport(BaseModel):
    commuter: Optional[BenefitFeaturesAndOperations] = None

    custom_post_tax: Optional[BenefitFeaturesAndOperations] = None

    custom_pre_tax: Optional[BenefitFeaturesAndOperations] = None

    fsa_dependent_care: Optional[BenefitFeaturesAndOperations] = None

    fsa_medical: Optional[BenefitFeaturesAndOperations] = None

    hsa_post: Optional[BenefitFeaturesAndOperations] = None

    hsa_pre: Optional[BenefitFeaturesAndOperations] = None

    s125_dental: Optional[BenefitFeaturesAndOperations] = None

    s125_medical: Optional[BenefitFeaturesAndOperations] = None

    s125_vision: Optional[BenefitFeaturesAndOperations] = None

    simple: Optional[BenefitFeaturesAndOperations] = None

    simple_ira: Optional[BenefitFeaturesAndOperations] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[BenefitFeaturesAndOperations]: ...
