# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch._client import Finch, AsyncFinch
from finch.types.sandbox.connections import (
    AccountCreateResponse,
    AccountUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestAccounts:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Finch) -> None:
        account = client.sandbox.connections.accounts.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_id="string",
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Finch) -> None:
        account = client.sandbox.connections.accounts.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_id="string",
            authentication_type="credentials",
            products=["string", "string", "string"],
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Finch) -> None:
        response = client.sandbox.connections.accounts.with_raw_response.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @parametrize
    def test_method_update(self, client: Finch) -> None:
        account = client.sandbox.connections.accounts.update()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Finch) -> None:
        account = client.sandbox.connections.accounts.update(
            connection_status="reauth",
        )
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Finch) -> None:
        response = client.sandbox.connections.accounts.with_raw_response.update()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])


class TestAsyncAccounts:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncFinch) -> None:
        account = await client.sandbox.connections.accounts.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_id="string",
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncFinch) -> None:
        account = await client.sandbox.connections.accounts.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_id="string",
            authentication_type="credentials",
            products=["string", "string", "string"],
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncFinch) -> None:
        response = await client.sandbox.connections.accounts.with_raw_response.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncFinch) -> None:
        account = await client.sandbox.connections.accounts.update()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncFinch) -> None:
        account = await client.sandbox.connections.accounts.update(
            connection_status="reauth",
        )
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncFinch) -> None:
        response = await client.sandbox.connections.accounts.with_raw_response.update()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])