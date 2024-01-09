# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from finch.types import CreateAccessTokenResponse
from tests.utils import assert_matches_type
from finch._client import Finch, AsyncFinch

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestAccessTokens:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Finch) -> None:
        access_token = client.access_tokens.create(
            client_id="<your_client_id>",
            client_secret="<your_client_secret>",
            code="<your_authorization_code>",
            redirect_uri="https://example.com",
        )
        assert_matches_type(CreateAccessTokenResponse, access_token, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Finch) -> None:
        response = client.access_tokens.with_raw_response.create(
            client_id="<your_client_id>",
            client_secret="<your_client_secret>",
            code="<your_authorization_code>",
            redirect_uri="https://example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = response.parse()
        assert_matches_type(CreateAccessTokenResponse, access_token, path=["response"])


class TestAsyncAccessTokens:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncFinch) -> None:
        access_token = await client.access_tokens.create(
            client_id="<your_client_id>",
            client_secret="<your_client_secret>",
            code="<your_authorization_code>",
            redirect_uri="https://example.com",
        )
        assert_matches_type(CreateAccessTokenResponse, access_token, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncFinch) -> None:
        response = await client.access_tokens.with_raw_response.create(
            client_id="<your_client_id>",
            client_secret="<your_client_secret>",
            code="<your_authorization_code>",
            redirect_uri="https://example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = response.parse()
        assert_matches_type(CreateAccessTokenResponse, access_token, path=["response"])