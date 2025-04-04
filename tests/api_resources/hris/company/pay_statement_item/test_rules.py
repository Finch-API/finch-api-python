# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from finch import Finch, AsyncFinch
from tests.utils import assert_matches_type
from finch.pagination import SyncResponsesPage, AsyncResponsesPage
from finch.types.hris.company.pay_statement_item import (
    RuleListResponse,
    RuleCreateResponse,
    RuleDeleteResponse,
    RuleUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Finch) -> None:
        rule = client.hris.company.pay_statement_item.rules.create()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Finch) -> None:
        rule = client.hris.company.pay_statement_item.rules.create(
            attributes={"metadata": {"foo": "bar"}},
            conditions=[
                {
                    "field": "field",
                    "operator": "equals",
                    "value": "value",
                }
            ],
            effective_end_date="effective_end_date",
            effective_start_date="effective_start_date",
            entity_type="pay_statement_item",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Finch) -> None:
        response = client.hris.company.pay_statement_item.rules.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Finch) -> None:
        with client.hris.company.pay_statement_item.rules.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Finch) -> None:
        rule = client.hris.company.pay_statement_item.rules.update(
            rule_id="rule_id",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Finch) -> None:
        rule = client.hris.company.pay_statement_item.rules.update(
            rule_id="rule_id",
            optional_property={},
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Finch) -> None:
        response = client.hris.company.pay_statement_item.rules.with_raw_response.update(
            rule_id="rule_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Finch) -> None:
        with client.hris.company.pay_statement_item.rules.with_streaming_response.update(
            rule_id="rule_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Finch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.hris.company.pay_statement_item.rules.with_raw_response.update(
                rule_id="",
            )

    @parametrize
    def test_method_list(self, client: Finch) -> None:
        rule = client.hris.company.pay_statement_item.rules.list()
        assert_matches_type(SyncResponsesPage[RuleListResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Finch) -> None:
        response = client.hris.company.pay_statement_item.rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncResponsesPage[RuleListResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Finch) -> None:
        with client.hris.company.pay_statement_item.rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(SyncResponsesPage[RuleListResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Finch) -> None:
        rule = client.hris.company.pay_statement_item.rules.delete(
            "rule_id",
        )
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Finch) -> None:
        response = client.hris.company.pay_statement_item.rules.with_raw_response.delete(
            "rule_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Finch) -> None:
        with client.hris.company.pay_statement_item.rules.with_streaming_response.delete(
            "rule_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleDeleteResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Finch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.hris.company.pay_statement_item.rules.with_raw_response.delete(
                "",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncFinch) -> None:
        rule = await async_client.hris.company.pay_statement_item.rules.create()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFinch) -> None:
        rule = await async_client.hris.company.pay_statement_item.rules.create(
            attributes={"metadata": {"foo": "bar"}},
            conditions=[
                {
                    "field": "field",
                    "operator": "equals",
                    "value": "value",
                }
            ],
            effective_end_date="effective_end_date",
            effective_start_date="effective_start_date",
            entity_type="pay_statement_item",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFinch) -> None:
        response = await async_client.hris.company.pay_statement_item.rules.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFinch) -> None:
        async with async_client.hris.company.pay_statement_item.rules.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncFinch) -> None:
        rule = await async_client.hris.company.pay_statement_item.rules.update(
            rule_id="rule_id",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFinch) -> None:
        rule = await async_client.hris.company.pay_statement_item.rules.update(
            rule_id="rule_id",
            optional_property={},
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFinch) -> None:
        response = await async_client.hris.company.pay_statement_item.rules.with_raw_response.update(
            rule_id="rule_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFinch) -> None:
        async with async_client.hris.company.pay_statement_item.rules.with_streaming_response.update(
            rule_id="rule_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncFinch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.hris.company.pay_statement_item.rules.with_raw_response.update(
                rule_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncFinch) -> None:
        rule = await async_client.hris.company.pay_statement_item.rules.list()
        assert_matches_type(AsyncResponsesPage[RuleListResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFinch) -> None:
        response = await async_client.hris.company.pay_statement_item.rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(AsyncResponsesPage[RuleListResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFinch) -> None:
        async with async_client.hris.company.pay_statement_item.rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(AsyncResponsesPage[RuleListResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncFinch) -> None:
        rule = await async_client.hris.company.pay_statement_item.rules.delete(
            "rule_id",
        )
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFinch) -> None:
        response = await async_client.hris.company.pay_statement_item.rules.with_raw_response.delete(
            "rule_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFinch) -> None:
        async with async_client.hris.company.pay_statement_item.rules.with_streaming_response.delete(
            "rule_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleDeleteResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFinch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.hris.company.pay_statement_item.rules.with_raw_response.delete(
                "",
            )
