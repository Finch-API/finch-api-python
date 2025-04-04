# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["RuleUpdateParams"]


class RuleUpdateParams(TypedDict, total=False):
    optional_property: Annotated[object, PropertyInfo(alias="optionalProperty")]
