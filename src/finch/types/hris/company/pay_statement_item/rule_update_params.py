# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["RuleUpdateParams"]


class RuleUpdateParams(TypedDict, total=False):
    entity_ids: SequenceNotStr[str]
    """The entity IDs to update the rule for."""

    optional_property: Annotated[object, PropertyInfo(alias="optionalProperty")]
