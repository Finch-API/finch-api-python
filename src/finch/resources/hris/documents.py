# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, cast
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...types.hris import document_list_params, document_retreive_params
from ..._base_client import make_request_options
from ...types.hris.document_list_response import DocumentListResponse
from ...types.hris.document_retreive_response import DocumentRetreiveResponse

__all__ = ["Documents", "AsyncDocuments"]


class Documents(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return DocumentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return DocumentsWithStreamingResponse(self)

    def list(
        self,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        individual_ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        types: List[Literal["w4_2020", "w4_2005"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentListResponse:
        """**Beta:** This endpoint is in beta and may change.

        Retrieve a list of
        company-wide documents.

        Args:
          entity_ids: The entity IDs to specify which entities' data to access.

          individual_ids: Comma-delimited list of stable Finch uuids for each individual. If empty,
              defaults to all individuals

          limit: Number of documents to return (defaults to all)

          offset: Index to start from (defaults to 0)

          types: Comma-delimited list of document types to filter on. If empty, defaults to all
              types

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/employer/documents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_ids": entity_ids,
                        "individual_ids": individual_ids,
                        "limit": limit,
                        "offset": offset,
                        "types": types,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            cast_to=DocumentListResponse,
        )

    def retreive(
        self,
        document_id: str,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentRetreiveResponse:
        """**Beta:** This endpoint is in beta and may change.

        Retrieve details of a
        specific document by its ID.

        Args:
          entity_ids: The entity IDs to specify which entities' data to access.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return cast(
            DocumentRetreiveResponse,
            self._get(
                f"/employer/documents/{document_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"entity_ids": entity_ids}, document_retreive_params.DocumentRetreiveParams),
                ),
                cast_to=cast(
                    Any, DocumentRetreiveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncDocuments(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Finch-API/finch-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Finch-API/finch-api-python#with_streaming_response
        """
        return AsyncDocumentsWithStreamingResponse(self)

    async def list(
        self,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        individual_ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        types: List[Literal["w4_2020", "w4_2005"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentListResponse:
        """**Beta:** This endpoint is in beta and may change.

        Retrieve a list of
        company-wide documents.

        Args:
          entity_ids: The entity IDs to specify which entities' data to access.

          individual_ids: Comma-delimited list of stable Finch uuids for each individual. If empty,
              defaults to all individuals

          limit: Number of documents to return (defaults to all)

          offset: Index to start from (defaults to 0)

          types: Comma-delimited list of document types to filter on. If empty, defaults to all
              types

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/employer/documents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "entity_ids": entity_ids,
                        "individual_ids": individual_ids,
                        "limit": limit,
                        "offset": offset,
                        "types": types,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            cast_to=DocumentListResponse,
        )

    async def retreive(
        self,
        document_id: str,
        *,
        entity_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentRetreiveResponse:
        """**Beta:** This endpoint is in beta and may change.

        Retrieve details of a
        specific document by its ID.

        Args:
          entity_ids: The entity IDs to specify which entities' data to access.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return cast(
            DocumentRetreiveResponse,
            await self._get(
                f"/employer/documents/{document_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {"entity_ids": entity_ids}, document_retreive_params.DocumentRetreiveParams
                    ),
                ),
                cast_to=cast(
                    Any, DocumentRetreiveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class DocumentsWithRawResponse:
    def __init__(self, documents: Documents) -> None:
        self._documents = documents

        self.list = _legacy_response.to_raw_response_wrapper(
            documents.list,
        )
        self.retreive = _legacy_response.to_raw_response_wrapper(
            documents.retreive,
        )


class AsyncDocumentsWithRawResponse:
    def __init__(self, documents: AsyncDocuments) -> None:
        self._documents = documents

        self.list = _legacy_response.async_to_raw_response_wrapper(
            documents.list,
        )
        self.retreive = _legacy_response.async_to_raw_response_wrapper(
            documents.retreive,
        )


class DocumentsWithStreamingResponse:
    def __init__(self, documents: Documents) -> None:
        self._documents = documents

        self.list = to_streamed_response_wrapper(
            documents.list,
        )
        self.retreive = to_streamed_response_wrapper(
            documents.retreive,
        )


class AsyncDocumentsWithStreamingResponse:
    def __init__(self, documents: AsyncDocuments) -> None:
        self._documents = documents

        self.list = async_to_streamed_response_wrapper(
            documents.list,
        )
        self.retreive = async_to_streamed_response_wrapper(
            documents.retreive,
        )
