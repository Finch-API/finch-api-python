# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["RuleCreateParams", "Attributes", "Condition"]


class RuleCreateParams(TypedDict, total=False):
    attributes: Attributes
    """Specifies the fields to be applied when the condition is met."""

    conditions: Iterable[Condition]

    effective_end_date: Optional[str]
    """Specifies when the rules should stop applying rules based on the date."""

    effective_start_date: Optional[str]
    """Specifies when the rule should begin applying based on the date."""

    entity_type: Literal["pay_statement_item"]
    """The entity type to which the rule is applied."""


class Attributes(TypedDict, total=False):
    metadata: Dict[str, object]
    """The metadata to be attached in the entity.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class Condition(TypedDict, total=False):
    field: str
    """The field to be checked in the rule."""

    operator: Literal["equals"]
    """The operator to be used in the rule."""

    value: str
    """The value of the field to be checked in the rule."""
