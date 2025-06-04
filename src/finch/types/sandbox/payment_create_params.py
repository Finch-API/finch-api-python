# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from ..hris.pay_statement_param import PayStatementParam

__all__ = ["PaymentCreateParams"]


class PaymentCreateParams(TypedDict, total=False):
    end_date: str

    pay_statements: Iterable[PayStatementParam]

    start_date: str
