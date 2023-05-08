# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.ats import Application
from finch.pagination import SyncApplicationsPage, AsyncApplicationsPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
access_token = os.environ.get("API_KEY", "something1234")


class TestApplications:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Finch) -> None:
        application = client.ats.applications.retrieve(
            "string",
        )
        assert_matches_type(Application, application, path=["response"])

    @parametrize
    def test_method_list(self, client: Finch) -> None:
        application = client.ats.applications.list()
        assert_matches_type(SyncApplicationsPage[Application], application, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Finch) -> None:
        application = client.ats.applications.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncApplicationsPage[Application], application, path=["response"])


class TestAsyncApplications:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncFinch) -> None:
        application = await client.ats.applications.retrieve(
            "string",
        )
        assert_matches_type(Application, application, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncFinch) -> None:
        application = await client.ats.applications.list()
        assert_matches_type(AsyncApplicationsPage[Application], application, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncFinch) -> None:
        application = await client.ats.applications.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncApplicationsPage[Application], application, path=["response"])
