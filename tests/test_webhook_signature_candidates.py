from __future__ import annotations

import hmac
import time
import base64
import hashlib

import pytest

from finch import Finch, AsyncFinch

PAYLOAD = '{"company_id":"test-company"}'
SECRET = base64.b64encode(b"test-webhook-key").decode()


def headers_with_signature(malformed: str, valid_first: bool, include_valid: bool = True) -> dict[str, str]:
    timestamp = str(int(time.time()))
    event_id = "test-event"
    signed = f"{event_id}.{timestamp}.{PAYLOAD}".encode()
    signature = base64.b64encode(hmac.new(b"test-webhook-key", signed, hashlib.sha256).digest()).decode()
    candidates = [f"v1,{malformed}"]
    if include_valid:
        candidates.insert(0 if valid_first else 1, f"v1,{signature}")
    return {
        "finch-event-id": event_id,
        "finch-timestamp": timestamp,
        "finch-signature": " ".join(candidates),
    }


@pytest.mark.parametrize("is_async", [False, True], ids=["sync", "async"])
@pytest.mark.parametrize("malformed", ["a", "a=", "é"])
@pytest.mark.parametrize("valid_first", [False, True])
async def test_valid_signature_is_checked_despite_malformed_candidate(
    is_async: bool, malformed: str, valid_first: bool
) -> None:
    client = AsyncFinch(access_token="test-token") if is_async else Finch(access_token="test-token")
    try:
        assert (
            client.webhooks.verify_signature(PAYLOAD, headers_with_signature(malformed, valid_first), secret=SECRET)
            is None
        )
    finally:
        if isinstance(client, AsyncFinch):
            await client.close()
        else:
            client.close()


@pytest.mark.parametrize("is_async", [False, True], ids=["sync", "async"])
@pytest.mark.parametrize("malformed", ["a", "a=", "é"])
async def test_malformed_candidate_alone_is_rejected(is_async: bool, malformed: str) -> None:
    client = AsyncFinch(access_token="test-token") if is_async else Finch(access_token="test-token")
    try:
        with pytest.raises(ValueError):
            client.webhooks.verify_signature(
                PAYLOAD, headers_with_signature(malformed, False, include_valid=False), secret=SECRET
            )
    finally:
        if isinstance(client, AsyncFinch):
            await client.close()
        else:
            client.close()
