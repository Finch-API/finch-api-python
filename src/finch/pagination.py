# File generated from our OpenAPI spec by Stainless.

from typing import Any, List, Type, Generic, Mapping, TypeVar, Optional, cast
from typing_extensions import override

from httpx import Response

from ._types import ModelT
from ._utils import is_mapping
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage
from .types.shared import Paging

__all__ = [
    "SyncSinglePage",
    "AsyncSinglePage",
    "SyncResponsesPage",
    "AsyncResponsesPage",
    "SyncIndividualsPage",
    "AsyncIndividualsPage",
    "SyncPage",
    "AsyncPage",
]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)


class SyncSinglePage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    items: List[ModelT]

    @override
    def _get_page_items(self) -> List[ModelT]:
        return self.items

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class AsyncSinglePage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    items: List[ModelT]

    @override
    def _get_page_items(self) -> List[ModelT]:
        return self.items

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class SyncResponsesPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    responses: List[ModelT]

    @override
    def _get_page_items(self) -> List[ModelT]:
        return self.responses

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None


class AsyncResponsesPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    responses: List[ModelT]

    @override
    def _get_page_items(self) -> List[ModelT]:
        return self.responses

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None


class SyncIndividualsPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    individuals: List[ModelT]
    paging: Paging

    @override
    def _get_page_items(self) -> List[ModelT]:
        return self.individuals

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.paging.offset
        if offset is None:
            return None

        length = len(self.individuals)
        current_count = offset + length

        total_count = self.paging.count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncIndividualsPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    individuals: List[ModelT]
    paging: Paging

    @override
    def _get_page_items(self) -> List[ModelT]:
        return self.individuals

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.paging.offset
        if offset is None:
            return None

        length = len(self.individuals)
        current_count = offset + length

        total_count = self.paging.count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    paging: Paging
    data: List[ModelT]

    @override
    def _get_page_items(self) -> List[ModelT]:
        return self.data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.paging.offset
        if offset is None:
            return None

        length = len(self.data)
        current_count = offset + length

        total_count = self.paging.count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    paging: Paging
    data: List[ModelT]

    @override
    def _get_page_items(self) -> List[ModelT]:
        return self.data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.paging.offset
        if offset is None:
            return None

        length = len(self.data)
        current_count = offset + length

        total_count = self.paging.count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None
