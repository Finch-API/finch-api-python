# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.ats import Stage
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options

__all__ = ["Stages", "AsyncStages"]


class Stages(SyncAPIResource):
    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Stage]:
        """Get all job stages for an organization.

        Depending on the system, some jobs may
        have stages specific to that job. Other job stages may apply broadly to all jobs
        in the system. Use the `job_id` to determine whether a job applies specifically
        to a job.
        """
        return self._get_api_list(
            "/ats/stages",
            page=SyncSinglePage[Stage],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Stage,
        )


class AsyncStages(AsyncAPIResource):
    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Stage, AsyncSinglePage[Stage]]:
        """Get all job stages for an organization.

        Depending on the system, some jobs may
        have stages specific to that job. Other job stages may apply broadly to all jobs
        in the system. Use the `job_id` to determine whether a job applies specifically
        to a job.
        """
        return self._get_api_list(
            "/ats/stages",
            page=AsyncSinglePage[Stage],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Stage,
        )
