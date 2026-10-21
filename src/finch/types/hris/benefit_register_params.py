# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr
from .benefit_type import BenefitType
from .benefit_frequency import BenefitFrequency

__all__ = ["BenefitRegisterParams"]


class BenefitRegisterParams(TypedDict, total=False):
    entity_ids: SequenceNotStr[str]
    """The entity IDs to specify which entities' data to access.

    Provide exactly one entity ID per request; a maximum of one is accepted.
    Required when the connection has more than one entity — omitting it returns a
    `400` `invalid_request_error`. Optional for single-entity connections.
    """

    description: str

    frequency: Optional[BenefitFrequency]
    """The frequency of the benefit deduction/contribution."""

    type: Optional[BenefitType]
    """Type of benefit."""
