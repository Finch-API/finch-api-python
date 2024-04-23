# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.sandbox.connections.account_create_response import AccountCreateResponse
from finch.types.sandbox.connections.account_update_response import AccountUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    def test_method_create(self, client: Finch) -> None:
        account = client.sandbox.connections.accounts.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_id="string",
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    def test_method_create_with_all_params(self, client: Finch) -> None:
        account = client.sandbox.connections.accounts.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_id="string",
            authentication_type="credential",
            products=["string", "string", "string"],
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    def test_raw_response_create(self, client: Finch) -> None:
        response = client.sandbox.connections.accounts.with_raw_response.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    def test_streaming_response_create(self, client: Finch) -> None:
        with client.sandbox.connections.accounts.with_streaming_response.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountCreateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Finch) -> None:
        with client.sandbox.connections.accounts.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountUpdateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    async def test_method_create(self, async_client: AsyncFinch) -> None:
        account = await async_client.sandbox.connections.accounts.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_id="string",
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFinch) -> None:
        account = await async_client.sandbox.connections.accounts.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_id="string",
            authentication_type="credential",
            products=["string", "string", "string"],
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFinch) -> None:
        response = await async_client.sandbox.connections.accounts.with_raw_response.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Auth isn't setup correctly in this test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFinch) -> None:
        async with async_client.sandbox.connections.accounts.with_streaming_response.create(
            company_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            provider_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountCreateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncFinch) -> None:
        account = await async_client.sandbox.connections.accounts.update()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFinch) -> None:
        account = await async_client.sandbox.connections.accounts.update(
            connection_status="reauth",
        )
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFinch) -> None:
        response = await async_client.sandbox.connections.accounts.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFinch) -> None:
        async with async_client.sandbox.connections.accounts.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountUpdateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True
