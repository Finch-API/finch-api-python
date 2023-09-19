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

The full API of this library can be found in [api.md](https://www.github.com/Finch-API/finch-api-python/blob/main/api.md).

```python
from finch import Finch

client = Finch(
    access_token="my access token",
)

page = client.hris.directory.list_individuals(
    candidate_id="<candidate id>",
)
directory = page.individuals[0]
print(directory.first_name)
```

## Async Usage

Simply import `AsyncFinch` instead of `Finch` and use `await` with each API call:

```python
from finch import AsyncFinch

client = AsyncFinch(
    access_token="my access token",
)


async def main():
    page = await client.hris.directory.list_individuals(
        candidate_id="<candidate id>",
    )
    print(page.individuals[0].first_name)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Using Types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev), which provide helper methods for things like serializing back into json ([v1](https://docs.pydantic.dev/1.10/usage/models/), [v2](https://docs.pydantic.dev/latest/usage/serialization/)). To get a dictionary, you can call `dict(model)`.

This helps provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `"basic"`.

## Pagination

List methods in the Finch API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```python
import finch

client = Finch()

all_directories = []
# Automatically fetches more pages as needed.
for directory in client.hris.directory.list_individuals():
    # Do something with directory here
    all_directories.append(directory)
print(all_directories)
```

Or, asynchronously:

```python
import asyncio
import finch

client = AsyncFinch()


async def main() -> None:
    all_directories = []
    # Iterate through items across all pages, issuing requests as needed.
    async for directory in client.hris.directory.list_individuals():
        all_directories.append(directory)
    print(all_directories)


asyncio.run(main())
```

Alternatively, you can use the `.has_next_page()`, `.next_page_info()`, or `.get_next_page()` methods for more granular control working with pages:

```python
first_page = await client.hris.directory.list_individuals()
if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.individuals)}")

# Remove `await` for non-async usage.
```

Or just work directly with the returned data:

```python
first_page = await client.hris.directory.list_individuals()

print(
    f"the current start offset for this page: {first_page.paging.offset}"
)  # => "the current start offset for this page: 1"
for directory in first_page.individuals:
    print(directory.id)

# Remove `await` for non-async usage.
```

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from finch import Finch

client = Finch()

client.hris.directory.list_individuals(
    path_params=[],
    params={},
)
```

## Webhook Verification

We provide helper methods for verifying that a webhook request came from Finch, and not a malicious third party.

You can use `finch.webhooks.verify_signature(body: string, headers, secret?) -> None` or `finch.webhooks.unwrap(body: string, headers, secret?) -> Payload`,
both of which will raise an error if the signature is invalid.

Note that the "body" parameter must be the raw JSON string sent from the server (do not parse it first).
The `.unwrap()` method can parse this JSON for you into a `Payload` object.

For example, in [FastAPI](https://fastapi.tiangolo.com/):

```py
@app.post('/my-webhook-handler')
async def handler(request: Request):
    body = await request.body()
    secret = os.environ['FINCH_WEBHOOK_SECRET']  # env var used by default; explicit here.
    payload = client.webhooks.unwrap(body, request.headers, secret)
    print(payload)

    return {'ok': True}
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
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors will all be retried by default.

You can use the `max_retries` option to configure or disable this:

```python
from finch import Finch

# Configure the default for all requests:
client = Finch(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).hris.directory.list_individuals()
```

### Timeouts

Requests time out after 1 minute by default. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration):

```python
from finch import Finch

# Configure the default for all requests:
client = Finch(
    # default is 60s
    timeout=20.0,
)

# More granular control:
client = Finch(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5 * 1000).hris.directory.list_individuals()
```

On timeout, an `APITimeoutError` is thrown.

Note that requests which time out will be [retried twice by default](#retries).

## Default Headers

We automatically send the `Finch-API-Version` header set to `2020-09-17`.

If you need to, you can override it by setting default headers per-request or on the client object.

Be aware that doing so may result in incorrect types and other unexpected or undefined behavior in the SDK.

```python
from finch import Finch

client = Finch(
    default_headers={"Finch-API-Version": "My-Custom-Value"},
)
```

## Advanced

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly null, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Configuring custom URLs, proxies, and transports

You can configure the following keyword arguments when instantiating the client:

```python
import httpx
from finch import Finch

client = Finch(
    # Use a custom base URL
    base_url="http://my.test.server.example.com:8083",
    proxies="http://my.test.proxy.example.com",
    transport=httpx.HTTPTransport(local_address="0.0.0.0"),
)
```

See the httpx documentation for information about the [`proxies`](https://www.python-httpx.org/advanced/#http-proxying) and [`transport`](https://www.python-httpx.org/advanced/#custom-transports) keyword arguments.

### Managing HTTP resources

By default we will close the underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__) is called but you can also manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

## Versioning

This package generally attempts to follow [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/Finch-API/finch-api-python/issues) with questions, bugs, or suggestions.

## Requirements

Python 3.7 or higher.
