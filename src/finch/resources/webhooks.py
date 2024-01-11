# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import hmac
import json
import math
import base64
import hashlib
from typing import cast
from datetime import datetime, timezone, timedelta

from ..types import WebhookEvent
from .._types import (
    HeadersLike,
)
from .._utils import (
    get_required_header,
)
from .._models import construct_type
from .._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Webhooks", "AsyncWebhooks"]


class Webhooks(SyncAPIResource):
    def unwrap(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> WebhookEvent:
        """Validates that the given payload was sent by Finch and parses the payload."""
        self.verify_signature(payload=payload, headers=headers, secret=secret)
        return cast(
            WebhookEvent,
            construct_type(
                value=json.loads(payload),
                type_=WebhookEvent,  # type: ignore[arg-type]
            ),
        )

    def verify_signature(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> None:
        """Validates whether or not the webhook payload was sent by Finch.

        An error will be raised if the webhook payload was not sent by Finch.
        """
        if secret is None:
            secret = self._client.webhook_secret

        if secret is None:
            raise ValueError(
                "The webhook secret must either be set using the env var, FINCH_WEBHOOK_SECRET, on the client class, Finch(webhook_secret='123'), or passed to this function"
            )

        try:
            parsedSecret = base64.b64decode(secret)
        except Exception as err:
            raise ValueError("Bad secret") from err

        msg_id = get_required_header(headers, "finch-event-id")
        msg_timestamp = get_required_header(headers, "finch-timestamp")

        # validate the timestamp
        webhook_tolerance = timedelta(minutes=5)
        now = datetime.now(tz=timezone.utc)

        try:
            timestamp = datetime.fromtimestamp(float(msg_timestamp), tz=timezone.utc)
        except Exception as err:
            raise ValueError("Invalid timestamp header: " + msg_timestamp + ". Could not convert to timestamp") from err

        # too old
        if timestamp < (now - webhook_tolerance):
            raise ValueError("Webhook timestamp is too old")

        # too new
        if timestamp > (now + webhook_tolerance):
            raise ValueError("Webhook timestamp is too new")

        # create the signature
        body = payload.decode("utf-8") if isinstance(payload, bytes) else payload
        if not isinstance(body, str):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise ValueError(
                "Webhook body should be a string of JSON (or bytes which can be decoded to a utf-8 string), not a parsed dictionary."
            )

        timestamp_str = str(math.floor(timestamp.replace(tzinfo=timezone.utc).timestamp()))

        to_sign = f"{msg_id}.{timestamp_str}.{body}".encode()
        expected_signature = hmac.new(parsedSecret, to_sign, hashlib.sha256).digest()

        msg_signature = get_required_header(headers, "finch-signature")

        # Signature header can contain multiple signatures delimited by spaces
        passed_sigs = msg_signature.split(" ")

        for versioned_sig in passed_sigs:
            values = versioned_sig.split(",")
            if len(values) != 2:
                # signature is not formatted like {version},{signature}
                continue

            (version, signature) = values

            # Only verify prefix v1
            if version != "v1":
                continue

            sig_bytes = base64.b64decode(signature)
            if hmac.compare_digest(expected_signature, sig_bytes):
                # valid!
                return None

        raise ValueError("None of the given webhook signatures match the expected signature")


class AsyncWebhooks(AsyncAPIResource):
    def unwrap(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> WebhookEvent:
        """Validates that the given payload was sent by Finch and parses the payload."""
        self.verify_signature(payload=payload, headers=headers, secret=secret)
        return cast(
            WebhookEvent,
            construct_type(
                value=json.loads(payload),
                type_=WebhookEvent,  # type: ignore[arg-type]
            ),
        )

    def verify_signature(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> None:
        """Validates whether or not the webhook payload was sent by Finch.

        An error will be raised if the webhook payload was not sent by Finch.
        """
        if secret is None:
            secret = self._client.webhook_secret

        if secret is None:
            raise ValueError(
                "The webhook secret must either be set using the env var, FINCH_WEBHOOK_SECRET, on the client class, Finch(webhook_secret='123'), or passed to this function"
            )

        try:
            parsedSecret = base64.b64decode(secret)
        except Exception as err:
            raise ValueError("Bad secret") from err

        msg_id = get_required_header(headers, "finch-event-id")
        msg_timestamp = get_required_header(headers, "finch-timestamp")

        # validate the timestamp
        webhook_tolerance = timedelta(minutes=5)
        now = datetime.now(tz=timezone.utc)

        try:
            timestamp = datetime.fromtimestamp(float(msg_timestamp), tz=timezone.utc)
        except Exception as err:
            raise ValueError("Invalid timestamp header: " + msg_timestamp + ". Could not convert to timestamp") from err

        # too old
        if timestamp < (now - webhook_tolerance):
            raise ValueError("Webhook timestamp is too old")

        # too new
        if timestamp > (now + webhook_tolerance):
            raise ValueError("Webhook timestamp is too new")

        # create the signature
        body = payload.decode("utf-8") if isinstance(payload, bytes) else payload
        if not isinstance(body, str):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise ValueError(
                "Webhook body should be a string of JSON (or bytes which can be decoded to a utf-8 string), not a parsed dictionary."
            )

        timestamp_str = str(math.floor(timestamp.replace(tzinfo=timezone.utc).timestamp()))

        to_sign = f"{msg_id}.{timestamp_str}.{body}".encode()
        expected_signature = hmac.new(parsedSecret, to_sign, hashlib.sha256).digest()

        msg_signature = get_required_header(headers, "finch-signature")

        # Signature header can contain multiple signatures delimited by spaces
        passed_sigs = msg_signature.split(" ")

        for versioned_sig in passed_sigs:
            values = versioned_sig.split(",")
            if len(values) != 2:
                # signature is not formatted like {version},{signature}
                continue

            (version, signature) = values

            # Only verify prefix v1
            if version != "v1":
                continue

            sig_bytes = base64.b64decode(signature)
            if hmac.compare_digest(expected_signature, sig_bytes):
                # valid!
                return None

        raise ValueError("None of the given webhook signatures match the expected signature")
