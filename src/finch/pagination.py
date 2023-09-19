# File generated from our OpenAPI spec by Stainless.

from typing import Any, List, Type, Generic, Mapping, TypeVar, Optional, cast

from httpx import Response

from .types import Paging
from ._types import ModelT
from ._utils import is_mapping
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncSinglePage",
    "AsyncSinglePage",
    "SyncResponsesPage",
    "AsyncResponsesPage",
    "SyncIndividualsPage",
    "AsyncIndividualsPage",
]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)


class SyncSinglePage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    items: List[ModelT]

    def _get_page_items(self) -> List[ModelT]:
        return self.items

    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:
        return cls.construct(
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            }
        )


class AsyncSinglePage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    items: List[ModelT]

    def _get_page_items(self) -> List[ModelT]:
        return self.items

    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:
        return cls.construct(
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            }
        )


class SyncResponsesPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    responses: List[ModelT]

    def _get_page_items(self) -> List[ModelT]:
        return self.responses

    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None


class AsyncResponsesPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    responses: List[ModelT]

    def _get_page_items(self) -> List[ModelT]:
        return self.responses

    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None


IndividualsPagePaging = Paging
"""This is deprecated, Paging should be used instead"""


class SyncIndividualsPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    individuals: List[ModelT]
    paging: Paging

    def _get_page_items(self) -> List[ModelT]:
        return self.individuals

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

    def _get_page_items(self) -> List[ModelT]:
        return self.individuals

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
