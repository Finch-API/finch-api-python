# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["IndividualEnrollManyParams", "Individual"]


class IndividualEnrollManyParams(TypedDict, total=False):
    individuals: Required[Iterable[Individual]]
    """Array of the individual_id to enroll and a configuration object."""


class Individual(TypedDict, total=False):
    configuration: object

    individual_id: str
    """Finch id (uuidv4) for the individual to enroll"""
