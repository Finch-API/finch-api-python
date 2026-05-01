# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["Individual", "BatchError"]


class BatchError(BaseModel):
    code: float

    message: str

    name: str

    finch_code: Optional[str] = None


Individual: TypeAlias = Union[Individual, BatchError]
