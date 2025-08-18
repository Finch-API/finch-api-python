# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ManualRetrieveParams"]


class ManualRetrieveParams(TypedDict, total=False):
    entity_id: str
    """The entity ID to use when authenticating with a multi-account token.

    Required when using a multi-account token to specify which entity's data to
    access. Example: `123e4567-e89b-12d3-a456-426614174000`
    """
