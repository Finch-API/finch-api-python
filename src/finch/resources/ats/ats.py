# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .jobs import Jobs, AsyncJobs
from .offers import Offers, AsyncOffers
from .stages import Stages, AsyncStages
from .candidates import Candidates, AsyncCandidates
from ..._resource import SyncAPIResource, AsyncAPIResource
from .applications import Applications, AsyncApplications

if TYPE_CHECKING:
    from ..._client import Finch, AsyncFinch

__all__ = ["ATS", "AsyncATS"]


class ATS(SyncAPIResource):
    candidates: Candidates
    applications: Applications
    stages: Stages
    jobs: Jobs
    offers: Offers

    def __init__(self, client: Finch) -> None:
        super().__init__(client)
        self.candidates = Candidates(client)
        self.applications = Applications(client)
        self.stages = Stages(client)
        self.jobs = Jobs(client)
        self.offers = Offers(client)


class AsyncATS(AsyncAPIResource):
    candidates: AsyncCandidates
    applications: AsyncApplications
    stages: AsyncStages
    jobs: AsyncJobs
    offers: AsyncOffers

    def __init__(self, client: AsyncFinch) -> None:
        super().__init__(client)
        self.candidates = AsyncCandidates(client)
        self.applications = AsyncApplications(client)
        self.stages = AsyncStages(client)
        self.jobs = AsyncJobs(client)
        self.offers = AsyncOffers(client)
