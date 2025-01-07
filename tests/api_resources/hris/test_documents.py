# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.types.hris import DocumentListResponse, DocumentRetreiveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Finch) -> None:
        document = client.hris.documents.list()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Finch) -> None:
        document = client.hris.documents.list(
            individual_ids=["string"],
            limit=0,
            offset=0,
            types=["w4_2020"],
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Finch) -> None:
        response = client.hris.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Finch) -> None:
        with client.hris.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retreive(self, client: Finch) -> None:
        document = client.hris.documents.retreive(
            "document_id",
        )
        assert_matches_type(DocumentRetreiveResponse, document, path=["response"])

    @parametrize
    def test_raw_response_retreive(self, client: Finch) -> None:
        response = client.hris.documents.with_raw_response.retreive(
            "document_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentRetreiveResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_retreive(self, client: Finch) -> None:
        with client.hris.documents.with_streaming_response.retreive(
            "document_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentRetreiveResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retreive(self, client: Finch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.hris.documents.with_raw_response.retreive(
                "",
            )


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncFinch) -> None:
        document = await async_client.hris.documents.list()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFinch) -> None:
        document = await async_client.hris.documents.list(
            individual_ids=["string"],
            limit=0,
            offset=0,
            types=["w4_2020"],
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFinch) -> None:
        response = await async_client.hris.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFinch) -> None:
        async with async_client.hris.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retreive(self, async_client: AsyncFinch) -> None:
        document = await async_client.hris.documents.retreive(
            "document_id",
        )
        assert_matches_type(DocumentRetreiveResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_retreive(self, async_client: AsyncFinch) -> None:
        response = await async_client.hris.documents.with_raw_response.retreive(
            "document_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentRetreiveResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_retreive(self, async_client: AsyncFinch) -> None:
        async with async_client.hris.documents.with_streaming_response.retreive(
            "document_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentRetreiveResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retreive(self, async_client: AsyncFinch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.hris.documents.with_raw_response.retreive(
                "",
            )
