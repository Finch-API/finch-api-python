# File generated from our OpenAPI spec by Stainless.

from typing import List, Type, Generic, Mapping, TypeVar, Optional

from httpx import Response

from ._types import ModelT
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncSinglePage",
    "AsyncSinglePage",
    "SyncResponsesPage",
    "AsyncResponsesPage",
    "SyncIndividualsPage",
    "AsyncIndividualsPage",
    "SyncCandidatesPage",
    "AsyncCandidatesPage",
    "SyncApplicationsPage",
    "AsyncApplicationsPage",
    "SyncJobsPage",
    "AsyncJobsPage",
    "SyncOffersPage",
    "AsyncOffersPage",
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
                **(data if isinstance(data, Mapping) else {"items": data}),
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
                **(data if isinstance(data, Mapping) else {"items": data}),
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


class IndividualsPagePaging(BaseModel):
    count: Optional[int]
    """The total number of elements for the entire query (not just the given page)"""

    offset: Optional[int]
    """The current start index of the returned list of elements"""


class SyncIndividualsPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    paging: IndividualsPagePaging
    individuals: List[ModelT]

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
    paging: IndividualsPagePaging
    individuals: List[ModelT]

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


class CandidatesPagePaging(BaseModel):
    count: Optional[int]
    """The total number of elements for the entire query (not just the given page)"""

    offset: Optional[int]
    """The current start index of the returned list of elements"""


class SyncCandidatesPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    paging: CandidatesPagePaging
    candidates: List[ModelT]

    def _get_page_items(self) -> List[ModelT]:
        return self.candidates

    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.paging.offset
        if offset is None:
            return None

        length = len(self.candidates)
        current_count = offset + length

        total_count = self.paging.count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncCandidatesPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    paging: CandidatesPagePaging
    candidates: List[ModelT]

    def _get_page_items(self) -> List[ModelT]:
        return self.candidates

    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.paging.offset
        if offset is None:
            return None

        length = len(self.candidates)
        current_count = offset + length

        total_count = self.paging.count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class ApplicationsPagePaging(BaseModel):
    count: Optional[int]
    """The total number of elements for the entire query (not just the given page)"""

    offset: Optional[int]
    """The current start index of the returned list of elements"""


class SyncApplicationsPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    paging: ApplicationsPagePaging
    applications: List[ModelT]

    def _get_page_items(self) -> List[ModelT]:
        return self.applications

    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.paging.offset
        if offset is None:
            return None

        length = len(self.applications)
        current_count = offset + length

        total_count = self.paging.count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncApplicationsPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    paging: ApplicationsPagePaging
    applications: List[ModelT]

    def _get_page_items(self) -> List[ModelT]:
        return self.applications

    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.paging.offset
        if offset is None:
            return None

        length = len(self.applications)
        current_count = offset + length

        total_count = self.paging.count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class JobsPagePaging(BaseModel):
    count: Optional[int]
    """The total number of elements for the entire query (not just the given page)"""

    offset: Optional[int]
    """The current start index of the returned list of elements"""


class SyncJobsPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    paging: JobsPagePaging
    jobs: List[ModelT]

    def _get_page_items(self) -> List[ModelT]:
        return self.jobs

    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.paging.offset
        if offset is None:
            return None

        length = len(self.jobs)
        current_count = offset + length

        total_count = self.paging.count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncJobsPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    paging: JobsPagePaging
    jobs: List[ModelT]

    def _get_page_items(self) -> List[ModelT]:
        return self.jobs

    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.paging.offset
        if offset is None:
            return None

        length = len(self.jobs)
        current_count = offset + length

        total_count = self.paging.count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class OffersPagePaging(BaseModel):
    count: Optional[int]
    """The total number of elements for the entire query (not just the given page)"""

    offset: Optional[int]
    """The current start index of the returned list of elements"""


class SyncOffersPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    paging: OffersPagePaging
    offers: List[ModelT]

    def _get_page_items(self) -> List[ModelT]:
        return self.offers

    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.paging.offset
        if offset is None:
            return None

        length = len(self.offers)
        current_count = offset + length

        total_count = self.paging.count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffersPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    paging: OffersPagePaging
    offers: List[ModelT]

    def _get_page_items(self) -> List[ModelT]:
        return self.offers

    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.paging.offset
        if offset is None:
            return None

        length = len(self.offers)
        current_count = offset + length

        total_count = self.paging.count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None
