# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .operation_support import OperationSupport

__all__ = ["OperationSupportMatrix"]


class OperationSupportMatrix(BaseModel):
    create: Optional[OperationSupport] = None
    """
    - `supported`: This operation is supported by both the provider and Finch
    - `not_supported_by_finch`: This operation is not supported by Finch but
      supported by the provider
    - `not_supported_by_provider`: This operation is not supported by the provider,
      so Finch cannot support
    - `client_access_only`: This behavior is supported by the provider, but only
      available to the client and not to Finch
    """

    delete: Optional[OperationSupport] = None
    """
    - `supported`: This operation is supported by both the provider and Finch
    - `not_supported_by_finch`: This operation is not supported by Finch but
      supported by the provider
    - `not_supported_by_provider`: This operation is not supported by the provider,
      so Finch cannot support
    - `client_access_only`: This behavior is supported by the provider, but only
      available to the client and not to Finch
    """

    read: Optional[OperationSupport] = None
    """
    - `supported`: This operation is supported by both the provider and Finch
    - `not_supported_by_finch`: This operation is not supported by Finch but
      supported by the provider
    - `not_supported_by_provider`: This operation is not supported by the provider,
      so Finch cannot support
    - `client_access_only`: This behavior is supported by the provider, but only
      available to the client and not to Finch
    """

    update: Optional[OperationSupport] = None
    """
    - `supported`: This operation is supported by both the provider and Finch
    - `not_supported_by_finch`: This operation is not supported by Finch but
      supported by the provider
    - `not_supported_by_provider`: This operation is not supported by the provider,
      so Finch cannot support
    - `client_access_only`: This behavior is supported by the provider, but only
      available to the client and not to Finch
    """
