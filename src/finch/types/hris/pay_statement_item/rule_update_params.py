# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["RuleUpdateParams"]


class RuleUpdateParams(TypedDict, total=False):
    entity_ids: SequenceNotStr[str]
    """The entity IDs to update the rule for.

    Provide exactly one entity ID per request; a maximum of one is accepted.
    Required when the connection has more than one entity — omitting it returns a
    `400` `invalid_request_error`. Optional for single-entity connections.
    """

    optional_property: Annotated[object, PropertyInfo(alias="optionalProperty")]
