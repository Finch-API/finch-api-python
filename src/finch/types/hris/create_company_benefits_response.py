# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CreateCompanyBenefitsResponse"]


class CreateCompanyBenefitsResponse(BaseModel):
    benefit_id: str
    """The id of the benefit."""

    job_id: str
