# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.sandbox import DirectoryCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDirectory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Finch) -> None:
        directory = client.sandbox.directory.create(
            body=[{}],
        )
        assert_matches_type(DirectoryCreateResponse, directory, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Finch) -> None:
        response = client.sandbox.directory.with_raw_response.create(
            body=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert_matches_type(DirectoryCreateResponse, directory, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Finch) -> None:
        with client.sandbox.directory.with_streaming_response.create(
            body=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = response.parse()
            assert_matches_type(DirectoryCreateResponse, directory, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDirectory:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFinch) -> None:
        directory = await async_client.sandbox.directory.create(
            body=[{}],
        )
        assert_matches_type(DirectoryCreateResponse, directory, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFinch) -> None:
        response = await async_client.sandbox.directory.with_raw_response.create(
            body=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        directory = response.parse()
        assert_matches_type(DirectoryCreateResponse, directory, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFinch) -> None:
        async with async_client.sandbox.directory.with_streaming_response.create(
            body=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            directory = await response.parse()
            assert_matches_type(DirectoryCreateResponse, directory, path=["response"])

        assert cast(Any, response.is_closed) is True
