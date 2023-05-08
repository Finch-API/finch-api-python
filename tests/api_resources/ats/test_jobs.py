# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.ats import Job
from finch.pagination import SyncJobsPage, AsyncJobsPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
access_token = os.environ.get("API_KEY", "something1234")


class TestJobs:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Finch) -> None:
        job = client.ats.jobs.retrieve(
            "string",
        )
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    def test_method_list(self, client: Finch) -> None:
        job = client.ats.jobs.list()
        assert_matches_type(SyncJobsPage[Job], job, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Finch) -> None:
        job = client.ats.jobs.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncJobsPage[Job], job, path=["response"])


class TestAsyncJobs:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncFinch) -> None:
        job = await client.ats.jobs.retrieve(
            "string",
        )
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncFinch) -> None:
        job = await client.ats.jobs.list()
        assert_matches_type(AsyncJobsPage[Job], job, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncFinch) -> None:
        job = await client.ats.jobs.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncJobsPage[Job], job, path=["response"])
