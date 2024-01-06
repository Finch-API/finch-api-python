# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccessTokenCreateParams"]


class AccessTokenCreateParams(TypedDict, total=False):
    client_id: Required[str]

    client_secret: Required[str]

    code: Required[str]

    redirect_uri: Required[str]
