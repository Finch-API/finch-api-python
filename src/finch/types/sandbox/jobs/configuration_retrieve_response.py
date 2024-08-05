# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .sandbox_job_configuration import SandboxJobConfiguration

__all__ = ["ConfigurationRetrieveResponse"]

ConfigurationRetrieveResponse: TypeAlias = List[SandboxJobConfiguration]
