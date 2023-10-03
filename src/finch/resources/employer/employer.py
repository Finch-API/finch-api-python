# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .benefits import Benefits, AsyncBenefits
from ..._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ..._client import Finch, AsyncFinch

__all__ = ["Employer", "AsyncEmployer"]


class Employer(SyncAPIResource):
    benefits: Benefits

    def __init__(self, client: Finch) -> None:
        super().__init__(client)
        self.benefits = Benefits(client)


class AsyncEmployer(AsyncAPIResource):
    benefits: AsyncBenefits

    def __init__(self, client: AsyncFinch) -> None:
        super().__init__(client)
        self.benefits = AsyncBenefits(client)
