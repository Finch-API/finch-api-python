# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from finch import Finch, AsyncFinch
from finch._client import Finch, AsyncFinch

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
access_token = "My Access Token"


class TestTopLevel:
    strict_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = Finch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])


class TestAsyncTopLevel:
    strict_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=True)
    loose_client = AsyncFinch(base_url=base_url, access_token=access_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])
