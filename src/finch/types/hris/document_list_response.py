# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.paging import Paging
from .document_response import DocumentResponse

__all__ = ["DocumentListResponse"]


class DocumentListResponse(BaseModel):
    documents: List[DocumentResponse]

    paging: Paging
