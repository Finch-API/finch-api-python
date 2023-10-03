# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .hris import BenefitFrequency
from .._models import BaseModel

__all__ = [
    "BenefitSupportType",
    "SupportedFeatures",
    "SupportedOperations",
    "SupportedOperationsCompanyBenefits",
    "SupportedOperationsIndividualBenefits",
]


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


class SupportedOperationsCompanyBenefits(BaseModel):
    create: Optional[
        Literal["supported", "not_supported_by_finch", "not_supported_by_provider", "client_access_only"]
    ] = None
    """
    - `supported`: This operation is supported by both the provider and Finch <br>
    - `not_supported_by_finch`: This operation is not supported by Finch but
      supported by the provider <br>
    - `not_supported_by_provider`: This operation is not supported by the provider,
      so Finch cannot support <br>
    - `client_access_only`: This behavior is supported by the provider, but only
      available to the client and not to Finch
    """

    delete: Optional[
        Literal["supported", "not_supported_by_finch", "not_supported_by_provider", "client_access_only"]
    ] = None
    """
    - `supported`: This operation is supported by both the provider and Finch <br>
    - `not_supported_by_finch`: This operation is not supported by Finch but
      supported by the provider <br>
    - `not_supported_by_provider`: This operation is not supported by the provider,
      so Finch cannot support <br>
    - `client_access_only`: This behavior is supported by the provider, but only
      available to the client and not to Finch
    """

    read: Optional[
        Literal["supported", "not_supported_by_finch", "not_supported_by_provider", "client_access_only"]
    ] = None
    """
    - `supported`: This operation is supported by both the provider and Finch <br>
    - `not_supported_by_finch`: This operation is not supported by Finch but
      supported by the provider <br>
    - `not_supported_by_provider`: This operation is not supported by the provider,
      so Finch cannot support <br>
    - `client_access_only`: This behavior is supported by the provider, but only
      available to the client and not to Finch
    """

    update: Optional[
        Literal["supported", "not_supported_by_finch", "not_supported_by_provider", "client_access_only"]
    ] = None
    """
    - `supported`: This operation is supported by both the provider and Finch <br>
    - `not_supported_by_finch`: This operation is not supported by Finch but
      supported by the provider <br>
    - `not_supported_by_provider`: This operation is not supported by the provider,
      so Finch cannot support <br>
    - `client_access_only`: This behavior is supported by the provider, but only
      available to the client and not to Finch
    """


class SupportedOperationsIndividualBenefits(BaseModel):
    create: Optional[
        Literal["supported", "not_supported_by_finch", "not_supported_by_provider", "client_access_only"]
    ] = None
    """
    - `supported`: This operation is supported by both the provider and Finch <br>
    - `not_supported_by_finch`: This operation is not supported by Finch but
      supported by the provider <br>
    - `not_supported_by_provider`: This operation is not supported by the provider,
      so Finch cannot support <br>
    - `client_access_only`: This behavior is supported by the provider, but only
      available to the client and not to Finch
    """

    delete: Optional[
        Literal["supported", "not_supported_by_finch", "not_supported_by_provider", "client_access_only"]
    ] = None
    """
    - `supported`: This operation is supported by both the provider and Finch <br>
    - `not_supported_by_finch`: This operation is not supported by Finch but
      supported by the provider <br>
    - `not_supported_by_provider`: This operation is not supported by the provider,
      so Finch cannot support <br>
    - `client_access_only`: This behavior is supported by the provider, but only
      available to the client and not to Finch
    """

    read: Optional[
        Literal["supported", "not_supported_by_finch", "not_supported_by_provider", "client_access_only"]
    ] = None
    """
    - `supported`: This operation is supported by both the provider and Finch <br>
    - `not_supported_by_finch`: This operation is not supported by Finch but
      supported by the provider <br>
    - `not_supported_by_provider`: This operation is not supported by the provider,
      so Finch cannot support <br>
    - `client_access_only`: This behavior is supported by the provider, but only
      available to the client and not to Finch
    """

    update: Optional[
        Literal["supported", "not_supported_by_finch", "not_supported_by_provider", "client_access_only"]
    ] = None
    """
    - `supported`: This operation is supported by both the provider and Finch <br>
    - `not_supported_by_finch`: This operation is not supported by Finch but
      supported by the provider <br>
    - `not_supported_by_provider`: This operation is not supported by the provider,
      so Finch cannot support <br>
    - `client_access_only`: This behavior is supported by the provider, but only
      available to the client and not to Finch
    """


class SupportedOperations(BaseModel):
    company_benefits: Optional[SupportedOperationsCompanyBenefits] = None

    individual_benefits: Optional[SupportedOperationsIndividualBenefits] = None


class BenefitSupportType(BaseModel):
    supported_features: Optional[SupportedFeatures] = None

    supported_operations: Optional[SupportedOperations] = None
