# Finch Python API Library

[![PyPI version](https://img.shields.io/pypi/v/finch-api.svg)](https://pypi.org/project/finch-api/)

The Finch Python library provides convenient access to the Finch REST API from any Python 3.7+
application. It includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

## Documentation

The API documentation can be found [here](https://developer.tryfinch.com/).

## Installation

```sh
pip install finch-api
```

## Usage

```python
from finch import Finch

finch = Finch(
    access_token="my access token",
)

candidate = finch.ats.candidates.retrieve(
    "<candidate id>",
)
print(candidate.first_name)
```

## Async Usage

Simply import `AsyncFinch` instead of `Finch` and use `await` with each API call:

```python
from finch import AsyncFinch

finch = AsyncFinch(
    access_token="my access token",
)


async def main():
    candidate = await finch.ats.candidates.retrieve(
        "<candidate id>",
    )
    print(candidate.first_name)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Using Types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict), while responses are [Pydantic](https://pydantic-docs.helpmanual.io/) models. This helps provide autocomplete and documentation within your editor.

If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `"basic"`.

## Pagination

List methods in the Finch API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```python
import finch

finch = Finch()

all_jobs = []
# Automatically fetches more pages as needed.
for job in finch.ats.jobs.list():
    # Do something with job here
    all_jobs.append(job)
print(all_jobs)
```

Or, asynchronously:

```python
import asyncio
import finch

finch = AsyncFinch()


async def main() -> None:
    all_jobs = []
    # Iterate through items across all pages, issuing requests as needed.
    async for job in finch.ats.jobs.list():
        all_jobs.append(job)
    print(all_jobs)


asyncio.run(main())
```

Alternatively, you can use the `.has_next_page()`, `.next_page_info()`, or `.get_next_page()` methods for more granular control working with pages:

```python
first_page = await finch.ats.jobs.list()
if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.jobs)}")

# Remove `await` for non-async usage.
```

Or just work directly with the returned data:

```python
first_page = await finch.ats.jobs.list()

print(
    f"the current start offset for this page: {first_page.paging.offset}"
)  # => "the current start offset for this page: 1"
for job in first_page.jobs:
    print(job.id)

# Remove `await` for non-async usage.
```

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from finch import Finch

finch = Finch()

finch.hris.directory.list_individuals(
    path_params=[],
    params={},
)
```

## Handling errors

When the library is unable to connect to the API (e.g., due to network connection problems or a timeout), a subclass of `finch.APIConnectionError` is raised.

When the API returns a non-success status code (i.e., 4xx or 5xx
response), a subclass of `finch.APIStatusError` will be raised, containing `status_code` and `response` properties.

All errors inherit from `finch.APIError`.

```python
import finch
from finch import Finch

client = Finch()

try:
    client.hris.directory.list_individuals()
except finch.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except finch.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except finch.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors will be automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 409 Conflict, 429 Rate Limit,
and >=500 Internal errors will all be retried by default.

You can use the `max_retries` option to configure or disable this:

```python
from finch import Finch

# Configure the default for all requests:
finch = Finch(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
finch.with_options(max_retries=5).hris.directory.list_individuals()
```

### Timeouts

Requests time out after 60 seconds by default. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration):

```python
from finch import Finch

# Configure the default for all requests:
finch = Finch(
    # default is 60s
    timeout=20.0,
)

# More granular control:
finch = Finch(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
finch.with_options(timeout=5 * 1000).hris.directory.list_individuals()
```

On timeout, an `APITimeoutError` is thrown.

Note that requests which time out will be [retried twice by default](#retries).

## Default Headers

We automatically send the `Finch-API-Version` header set to `2020-09-17`.

If you need to, you can override it by setting default headers per-request or on the client object.

Be aware that doing so may result in incorrect types and other unexpected or undefined behavior in the SDK.

```python
from finch import Finch

finch = Finch(
    default_headers={"Finch-API-Version": "My-Custom-Value"},
)
```

## Advanced: Configuring custom URLs, proxies, and transports

You can configure the following keyword arguments when instantiating the client:

```python
import httpx
from finch import Finch

finch = Finch(
    # Use a custom base URL
    base_url="http://my.test.server.example.com:8083",
    proxies="http://my.test.proxy.example.com",
    transport=httpx.HTTPTransport(local_address="0.0.0.0"),
)
```

See the httpx documentation for information about the [`proxies`](https://www.python-httpx.org/advanced/#http-proxying) and [`transport`](https://www.python-httpx.org/advanced/#custom-transports) keyword arguments.

## Status

This package is in beta. Its internals and interfaces are not stable and subject to change without a major semver bump;
please reach out if you rely on any undocumented behavior.

We are keen for your feedback; please open an [issue](https://www.github.com/Finch-API/finch-api-python/issues) with questions, bugs, or suggestions.

## Requirements

Python 3.7 or higher.
