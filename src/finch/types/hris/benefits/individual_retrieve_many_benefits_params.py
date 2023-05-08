# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["IndividualRetrieveManyBenefitsParams"]


class IndividualRetrieveManyBenefitsParams(TypedDict, total=False):
    individual_ids: str
    """comma-delimited list of stable Finch uuids for each individual.

    If empty, defaults to all individuals
    """
