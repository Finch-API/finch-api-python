# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["RuleListResponse", "Attributes", "Condition"]


class Attributes(BaseModel):
    metadata: Optional[Dict[str, object]] = None
    """The metadata to be attached in the entity.

    It is a key-value pairs where the values can be of any type (string, number,
    boolean, object, array, etc.).
    """


class Condition(BaseModel):
    field: Optional[str] = None
    """The field to be checked in the rule."""

    operator: Optional[Literal["equals"]] = None
    """The operator to be used in the rule."""

    value: Optional[str] = None
    """The value of the field to be checked in the rule."""


class RuleListResponse(BaseModel):
    id: Optional[str] = None
    """Finch id (uuidv4) for the rule."""

    attributes: Optional[Attributes] = None
    """Specifies the fields to be applied when the condition is met."""

    conditions: Optional[List[Condition]] = None

    created_at: Optional[datetime] = None
    """The datetime when the rule was created."""

    effective_end_date: Optional[str] = None
    """Specifies when the rules should stop applying rules based on the date."""

    effective_start_date: Optional[str] = None
    """Specifies when the rule should begin applying based on the date."""

    entity_type: Optional[Literal["pay_statement_item"]] = None
    """The entity type to which the rule is applied."""

    priority: Optional[int] = None
    """The priority of the rule."""

    updated_at: Optional[datetime] = None
    """The datetime when the rule was last updated."""
