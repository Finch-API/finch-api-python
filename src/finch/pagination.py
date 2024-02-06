# File generated from our OpenAPI spec by Stainless.

from typing import Any, List, Type, Generic, Mapping, TypeVar, Optional, cast
from typing_extensions import override

from httpx import Response

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

_T = TypeVar("_T")


class SyncSinglePage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

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


class AsyncSinglePage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

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


class SyncResponsesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    responses: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        responses = self.responses
        if not responses:
            return []
        return responses

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None


class AsyncResponsesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    responses: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        responses = self.responses
        if not responses:
            return []
        return responses

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None


class SyncIndividualsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    individuals: List[_T]
    """The array of employees."""
    paging: Paging

    @override
    def _get_page_items(self) -> List[_T]:
        individuals = self.individuals
        if not individuals:
            return []
        return individuals

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = None
        if self.paging is not None:  # pyright: ignore[reportUnnecessaryComparison]
            offset = self.paging.offset
        if offset is None:
            return None

        length = len(self._get_page_items())
        current_count = offset + length

        count = None
        if self.paging is not None:  # pyright: ignore[reportUnnecessaryComparison]
            count = self.paging.count
        if count is None:
            return None

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncIndividualsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    individuals: List[_T]
    """The array of employees."""
    paging: Paging

    @override
    def _get_page_items(self) -> List[_T]:
        individuals = self.individuals
        if not individuals:
            return []
        return individuals

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = None
        if self.paging is not None:  # pyright: ignore[reportUnnecessaryComparison]
            offset = self.paging.offset
        if offset is None:
            return None

        length = len(self._get_page_items())
        current_count = offset + length

        count = None
        if self.paging is not None:  # pyright: ignore[reportUnnecessaryComparison]
            count = self.paging.count
        if count is None:
            return None

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    paging: Paging

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = None
        if self.paging is not None:  # pyright: ignore[reportUnnecessaryComparison]
            offset = self.paging.offset
        if offset is None:
            return None

        length = len(self._get_page_items())
        current_count = offset + length

        count = None
        if self.paging is not None:  # pyright: ignore[reportUnnecessaryComparison]
            count = self.paging.count
        if count is None:
            return None

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    paging: Paging

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = None
        if self.paging is not None:  # pyright: ignore[reportUnnecessaryComparison]
            offset = self.paging.offset
        if offset is None:
            return None

        length = len(self._get_page_items())
        current_count = offset + length

        count = None
        if self.paging is not None:  # pyright: ignore[reportUnnecessaryComparison]
            count = self.paging.count
        if count is None:
            return None

        if current_count < count:
            return PageInfo(params={"offset": current_count})

        return None
