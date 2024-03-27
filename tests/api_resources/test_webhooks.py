# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import Any, cast
from datetime import datetime, timezone, timedelta

import pytest
import time_machine
from pydantic import BaseModel

from finch import Finch, AsyncFinch

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    timestamp = "1676312382"
    fake_now = datetime.fromtimestamp(float(timestamp), tz=timezone.utc)

    payload = """{"company_id":"720be419-0293-4d32-a707-32179b0827ab"}"""
    signature = "m7y0TV2C+hlHxU42wCieApTSTaA8/047OAplBqxIV/s="
    headers = {
        "Finch-Event-Id": "msg_2Lh9KRb0pzN4LePd3XiA4v12Axj",
        "finch-timestamp": timestamp,
        "finch-signature": f"v1,{signature}",
    }
    secret = "5WbX5kEWLlfzsGNjH64I8lOOqUB6e8FH"

    @time_machine.travel(fake_now)
    def test_unwrap(self, client: Finch) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret

        obj = client.webhooks.unwrap(payload, headers, secret=secret)
        assert isinstance(obj, BaseModel)

    @time_machine.travel(fake_now)
    def test_verify_signature(self, client: Finch) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret
        signature = self.signature
        verify = client.webhooks.verify_signature

        assert verify(payload=payload, headers=headers, secret=secret) is None

        with pytest.raises(ValueError, match="Webhook timestamp is too old"):
            with time_machine.travel(self.fake_now + timedelta(minutes=6)):
                assert verify(payload=payload, headers=headers, secret=secret) is False

        with pytest.raises(ValueError, match="Webhook timestamp is too new"):
            with time_machine.travel(self.fake_now - timedelta(minutes=6)):
                assert verify(payload=payload, headers=headers, secret=secret) is False

        # wrong secret
        with pytest.raises(ValueError, match=r"Bad secret"):
            verify(payload=payload, headers=headers, secret="invalid secret")

        invalid_signature_message = "None of the given webhook signatures match the expected signature"
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers=headers,
                secret=base64.b64encode(b"foo").decode("utf-8"),
            )

        # multiple signatures
        invalid_signature = base64.b64encode(b"my_sig").decode("utf-8")
        assert (
            verify(
                payload=payload,
                headers={**headers, "finch-signature": f"v1,{invalid_signature} v1,{signature}"},
                secret=secret,
            )
            is None
        )

        # different signature version
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers={**headers, "finch-signature": f"v2,{signature}"},
                secret=secret,
            )

        assert (
            verify(
                payload=payload,
                headers={**headers, "finch-signature": f"v2,{signature} v1,{signature}"},
                secret=secret,
            )
            is None
        )

        # missing version
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers={**headers, "finch-signature": signature},
                secret=secret,
            )

        # non-string payload
        with pytest.raises(ValueError, match=r"Webhook body should be a string"):
            verify(
                payload=cast(Any, {"payload": payload}),
                headers=headers,
                secret=secret,
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    timestamp = "1676312382"
    fake_now = datetime.fromtimestamp(float(timestamp), tz=timezone.utc)

    payload = """{"company_id":"720be419-0293-4d32-a707-32179b0827ab"}"""
    signature = "m7y0TV2C+hlHxU42wCieApTSTaA8/047OAplBqxIV/s="
    headers = {
        "Finch-Event-Id": "msg_2Lh9KRb0pzN4LePd3XiA4v12Axj",
        "finch-timestamp": timestamp,
        "finch-signature": f"v1,{signature}",
    }
    secret = "5WbX5kEWLlfzsGNjH64I8lOOqUB6e8FH"

    @time_machine.travel(fake_now)
    def test_unwrap(self, async_client: AsyncFinch) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret

        obj = async_client.webhooks.unwrap(payload, headers, secret=secret)
        assert isinstance(obj, BaseModel)

    @time_machine.travel(fake_now)
    def test_verify_signature(self, async_client: AsyncFinch) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret
        signature = self.signature
        verify = async_client.webhooks.verify_signature

        assert verify(payload=payload, headers=headers, secret=secret) is None

        with pytest.raises(ValueError, match="Webhook timestamp is too old"):
            with time_machine.travel(self.fake_now + timedelta(minutes=6)):
                assert verify(payload=payload, headers=headers, secret=secret) is False

        with pytest.raises(ValueError, match="Webhook timestamp is too new"):
            with time_machine.travel(self.fake_now - timedelta(minutes=6)):
                assert verify(payload=payload, headers=headers, secret=secret) is False

        # wrong secret
        with pytest.raises(ValueError, match=r"Bad secret"):
            verify(payload=payload, headers=headers, secret="invalid secret")

        invalid_signature_message = "None of the given webhook signatures match the expected signature"
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers=headers,
                secret=base64.b64encode(b"foo").decode("utf-8"),
            )

        # multiple signatures
        invalid_signature = base64.b64encode(b"my_sig").decode("utf-8")
        assert (
            verify(
                payload=payload,
                headers={**headers, "finch-signature": f"v1,{invalid_signature} v1,{signature}"},
                secret=secret,
            )
            is None
        )

        # different signature version
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers={**headers, "finch-signature": f"v2,{signature}"},
                secret=secret,
            )

        assert (
            verify(
                payload=payload,
                headers={**headers, "finch-signature": f"v2,{signature} v1,{signature}"},
                secret=secret,
            )
            is None
        )

        # missing version
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers={**headers, "finch-signature": signature},
                secret=secret,
            )

        # non-string payload
        with pytest.raises(ValueError, match=r"Webhook body should be a string"):
            verify(
                payload=cast(Any, {"payload": payload}),
                headers=headers,
                secret=secret,
            )
