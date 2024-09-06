# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .company_event import CompanyEvent
from .payment_event import PaymentEvent
from .directory_event import DirectoryEvent
from .employment_event import EmploymentEvent
from .individual_event import IndividualEvent
from .pay_statement_event import PayStatementEvent
from .account_update_event import AccountUpdateEvent
from .job_completion_event import JobCompletionEvent

__all__ = ["WebhookEvent"]

WebhookEvent: TypeAlias = Union[
    AccountUpdateEvent,
    JobCompletionEvent,
    CompanyEvent,
    DirectoryEvent,
    EmploymentEvent,
    IndividualEvent,
    PaymentEvent,
    PayStatementEvent,
]
