# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .w42005 import W42005
from .w42020 import W42020
from ..._utils import PropertyInfo

__all__ = ["DocumentRetreiveResponse"]

DocumentRetreiveResponse: TypeAlias = Annotated[Union[W42020, W42005], PropertyInfo(discriminator="type")]
