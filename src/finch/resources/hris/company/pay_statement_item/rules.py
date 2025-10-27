# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..... import _legacy_response
from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .....pagination import SyncResponsesPage, AsyncResponsesPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.hris.company.pay_statement_item import (
    rule_list_params,
    rule_create_params,
    rule_delete_params,
    rule_update_params,
)
from .....types.hris.company.pay_statement_item.rule_list_response import RuleListResponse
from .....types.hris.company.pay_statement_item.rule_create_response import RuleCreateResponse
from .....types.hris.company.pay_statement_item.rule_delete_response import RuleDeleteResponse
from .....types.hris.company.pay_statement_item.rule_update_response import RuleUpdateResponse

__all__ = ["Rules", "AsyncRules"]


class Rules(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RulesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return RulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return RulesWithStreamingResponse(self)

    def create(
        self,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        attributes: rule_create_params.Attributes | Omit = omit,
        conditions: Iterable[rule_create_params.Condition] | Omit = omit,
        effective_end_date: Optional[str] | Omit = omit,
        effective_start_date: Optional[str] | Omit = omit,
        entity_type: Literal["pay_statement_item"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """
        **Beta:** this endpoint currently serves employers onboarded after March 4th and
        historical support will be added soon Custom rules can be created to associate
        specific attributes to pay statement items depending on the use case. For
        example, pay statement items that meet certain conditions can be labeled as a
        pre-tax 401k. This metadata can be retrieved where pay statement item
        information is available.

        Args:
          entity_ids: The entity IDs to create the rule for.

          attributes: Specifies the fields to be applied when the condition is met.

          effective_end_date: Specifies when the rules should stop applying rules based on the date.

          effective_start_date: Specifies when the rule should begin applying based on the date.

          entity_type: The entity type to which the rule is applied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/employer/pay-statement-item/rule",
            body=maybe_transform(
                {
                    "attributes": attributes,
                    "conditions": conditions,
                    "effective_end_date": effective_end_date,
                    "effective_start_date": effective_start_date,
                    "entity_type": entity_type,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"entity_ids": entity_ids}, rule_create_params.RuleCreateParams),
            ),
            cast_to=RuleCreateResponse,
        )

    def update(
        self,
        rule_id: str,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        optional_property: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleUpdateResponse:
        """
        **Beta:** this endpoint currently serves employers onboarded after March 4th and
        historical support will be added soon Update a rule for a pay statement item.

        Args:
          entity_ids: The entity IDs to update the rule for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._put(
            f"/employer/pay-statement-item/rule/{rule_id}",
            body=maybe_transform({"optional_property": optional_property}, rule_update_params.RuleUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"entity_ids": entity_ids}, rule_update_params.RuleUpdateParams),
            ),
            cast_to=RuleUpdateResponse,
        )

    def list(
        self,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncResponsesPage[RuleListResponse]:
        """
        **Beta:** this endpoint currently serves employers onboarded after March 4th and
        historical support will be added soon List all rules of a connection account.

        Args:
          entity_ids: The entity IDs to retrieve rules for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/pay-statement-item/rule",
            page=SyncResponsesPage[RuleListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"entity_ids": entity_ids}, rule_list_params.RuleListParams),
            ),
            model=RuleListResponse,
        )

    def delete(
        self,
        rule_id: str,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleDeleteResponse:
        """
        **Beta:** this endpoint currently serves employers onboarded after March 4th and
        historical support will be added soon Delete a rule for a pay statement item.

        Args:
          entity_ids: The entity IDs to delete the rule for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._delete(
            f"/employer/pay-statement-item/rule/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"entity_ids": entity_ids}, rule_delete_params.RuleDeleteParams),
            ),
            cast_to=RuleDeleteResponse,
        )


class AsyncRules(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AsyncRulesWithStreamingResponse(self)

    async def create(
        self,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        attributes: rule_create_params.Attributes | Omit = omit,
        conditions: Iterable[rule_create_params.Condition] | Omit = omit,
        effective_end_date: Optional[str] | Omit = omit,
        effective_start_date: Optional[str] | Omit = omit,
        entity_type: Literal["pay_statement_item"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """
        **Beta:** this endpoint currently serves employers onboarded after March 4th and
        historical support will be added soon Custom rules can be created to associate
        specific attributes to pay statement items depending on the use case. For
        example, pay statement items that meet certain conditions can be labeled as a
        pre-tax 401k. This metadata can be retrieved where pay statement item
        information is available.

        Args:
          entity_ids: The entity IDs to create the rule for.

          attributes: Specifies the fields to be applied when the condition is met.

          effective_end_date: Specifies when the rules should stop applying rules based on the date.

          effective_start_date: Specifies when the rule should begin applying based on the date.

          entity_type: The entity type to which the rule is applied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/employer/pay-statement-item/rule",
            body=await async_maybe_transform(
                {
                    "attributes": attributes,
                    "conditions": conditions,
                    "effective_end_date": effective_end_date,
                    "effective_start_date": effective_start_date,
                    "entity_type": entity_type,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"entity_ids": entity_ids}, rule_create_params.RuleCreateParams),
            ),
            cast_to=RuleCreateResponse,
        )

    async def update(
        self,
        rule_id: str,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        optional_property: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleUpdateResponse:
        """
        **Beta:** this endpoint currently serves employers onboarded after March 4th and
        historical support will be added soon Update a rule for a pay statement item.

        Args:
          entity_ids: The entity IDs to update the rule for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._put(
            f"/employer/pay-statement-item/rule/{rule_id}",
            body=await async_maybe_transform(
                {"optional_property": optional_property}, rule_update_params.RuleUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"entity_ids": entity_ids}, rule_update_params.RuleUpdateParams),
            ),
            cast_to=RuleUpdateResponse,
        )

    def list(
        self,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RuleListResponse, AsyncResponsesPage[RuleListResponse]]:
        """
        **Beta:** this endpoint currently serves employers onboarded after March 4th and
        historical support will be added soon List all rules of a connection account.

        Args:
          entity_ids: The entity IDs to retrieve rules for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/employer/pay-statement-item/rule",
            page=AsyncResponsesPage[RuleListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"entity_ids": entity_ids}, rule_list_params.RuleListParams),
            ),
            model=RuleListResponse,
        )

    async def delete(
        self,
        rule_id: str,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleDeleteResponse:
        """
        **Beta:** this endpoint currently serves employers onboarded after March 4th and
        historical support will be added soon Delete a rule for a pay statement item.

        Args:
          entity_ids: The entity IDs to delete the rule for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._delete(
            f"/employer/pay-statement-item/rule/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"entity_ids": entity_ids}, rule_delete_params.RuleDeleteParams),
            ),
            cast_to=RuleDeleteResponse,
        )


class RulesWithRawResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

        self.create = _legacy_response.to_raw_response_wrapper(
            rules.create,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            rules.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            rules.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            rules.delete,
        )


class AsyncRulesWithRawResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

        self.create = _legacy_response.async_to_raw_response_wrapper(
            rules.create,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            rules.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            rules.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            rules.delete,
        )


class RulesWithStreamingResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

        self.create = to_streamed_response_wrapper(
            rules.create,
        )
        self.update = to_streamed_response_wrapper(
            rules.update,
        )
        self.list = to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )


class AsyncRulesWithStreamingResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

        self.create = async_to_streamed_response_wrapper(
            rules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
