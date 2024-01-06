# Shared Types

```python
from finch.types import OperationSupport, OperationSupportMatrix, Paging
```

# Finch

Methods:

- <code>client.<a href="./src/finch/_client.py">get_access_token</a>(\*args) -> str</code>
- <code>client.<a href="./src/finch/_client.py">get_auth_url</a>(\*args) -> str</code>
- <code>client.<a href="./src/finch/_client.py">with_access_token</a>(\*args) -> Self</code>

# AccessTokens

Types:

```python
from finch.types import CreateAccessTokenResponse
```

Methods:

- <code title="post /auth/token">client.access_tokens.<a href="./src/finch/resources/access_tokens.py">create</a>(\*\*<a href="src/finch/types/access_token_create_params.py">params</a>) -> <a href="./src/finch/types/create_access_token_response.py">CreateAccessTokenResponse</a></code>

# HRIS

Types:

```python
from finch.types import Income, Location, Money
```

## CompanyResource

Types:

```python
from finch.types.hris import Company
```

Methods:

- <code title="get /employer/company">client.hris.company.<a href="./src/finch/resources/hris/company.py">retrieve</a>() -> <a href="./src/finch/types/hris/company.py">Company</a></code>

## Directory

Types:

```python
from finch.types.hris import IndividualInDirectory
```

Methods:

- <code title="get /employer/directory">client.hris.directory.<a href="./src/finch/resources/hris/directory.py">list</a>(\*\*<a href="src/finch/types/hris/directory_list_params.py">params</a>) -> <a href="./src/finch/types/hris/individual_in_directory.py">SyncIndividualsPage[IndividualInDirectory]</a></code>

## Individuals

Types:

```python
from finch.types.hris import Individual, IndividualResponse
```

Methods:

- <code title="post /employer/individual">client.hris.individuals.<a href="./src/finch/resources/hris/individuals.py">retrieve_many</a>(\*\*<a href="src/finch/types/hris/individual_retrieve_many_params.py">params</a>) -> <a href="./src/finch/types/hris/individual_response.py">SyncResponsesPage[IndividualResponse]</a></code>

## Employments

Types:

```python
from finch.types.hris import EmploymentData, EmploymentDataResponse
```

Methods:

- <code title="post /employer/employment">client.hris.employments.<a href="./src/finch/resources/hris/employments.py">retrieve_many</a>(\*\*<a href="src/finch/types/hris/employment_retrieve_many_params.py">params</a>) -> <a href="./src/finch/types/hris/employment_data_response.py">SyncResponsesPage[EmploymentDataResponse]</a></code>

## Payments

Types:

```python
from finch.types.hris import Payment
```

Methods:

- <code title="get /employer/payment">client.hris.payments.<a href="./src/finch/resources/hris/payments.py">list</a>(\*\*<a href="src/finch/types/hris/payment_list_params.py">params</a>) -> <a href="./src/finch/types/hris/payment.py">SyncSinglePage[Payment]</a></code>

## PayStatements

Types:

```python
from finch.types.hris import PayStatement, PayStatementResponse, PayStatementResponseBody
```

Methods:

- <code title="post /employer/pay-statement">client.hris.pay_statements.<a href="./src/finch/resources/hris/pay_statements.py">retrieve_many</a>(\*\*<a href="src/finch/types/hris/pay_statement_retrieve_many_params.py">params</a>) -> <a href="./src/finch/types/hris/pay_statement_response.py">SyncResponsesPage[PayStatementResponse]</a></code>

## Benefits

Types:

```python
from finch.types.hris import (
    BenefitContribution,
    BenefitFeaturesAndOperations,
    BenefitFrequency,
    BenefitType,
    BenefitsSupport,
    BenfitContribution,
    CompanyBenefit,
    CreateCompanyBenefitsResponse,
    SupportPerBenefitType,
    SupportedBenefit,
    UpdateCompanyBenefitResponse,
)
```

Methods:

- <code title="post /employer/benefits">client.hris.benefits.<a href="./src/finch/resources/hris/benefits/benefits.py">create</a>(\*\*<a href="src/finch/types/hris/benefit_create_params.py">params</a>) -> <a href="./src/finch/types/hris/create_company_benefits_response.py">CreateCompanyBenefitsResponse</a></code>
- <code title="get /employer/benefits/{benefit_id}">client.hris.benefits.<a href="./src/finch/resources/hris/benefits/benefits.py">retrieve</a>(benefit_id) -> <a href="./src/finch/types/hris/company_benefit.py">CompanyBenefit</a></code>
- <code title="post /employer/benefits/{benefit_id}">client.hris.benefits.<a href="./src/finch/resources/hris/benefits/benefits.py">update</a>(benefit_id, \*\*<a href="src/finch/types/hris/benefit_update_params.py">params</a>) -> <a href="./src/finch/types/hris/update_company_benefit_response.py">UpdateCompanyBenefitResponse</a></code>
- <code title="get /employer/benefits">client.hris.benefits.<a href="./src/finch/resources/hris/benefits/benefits.py">list</a>() -> <a href="./src/finch/types/hris/company_benefit.py">SyncSinglePage[CompanyBenefit]</a></code>
- <code title="get /employer/benefits/meta">client.hris.benefits.<a href="./src/finch/resources/hris/benefits/benefits.py">list_supported_benefits</a>() -> <a href="./src/finch/types/hris/supported_benefit.py">SyncSinglePage[SupportedBenefit]</a></code>

### Individuals

Types:

```python
from finch.types.hris.benefits import (
    EnrolledIndividual,
    IndividualBenefit,
    UnenrolledIndividual,
    IndividualEnrolledIDsResponse,
)
```

Methods:

- <code title="post /employer/benefits/{benefit_id}/individuals">client.hris.benefits.individuals.<a href="./src/finch/resources/hris/benefits/individuals.py">enroll_many</a>(benefit_id, \*\*<a href="src/finch/types/hris/benefits/individual_enroll_many_params.py">params</a>) -> <a href="./src/finch/types/hris/benefits/enrolled_individual.py">SyncSinglePage[EnrolledIndividual]</a></code>
- <code title="get /employer/benefits/{benefit_id}/enrolled">client.hris.benefits.individuals.<a href="./src/finch/resources/hris/benefits/individuals.py">enrolled_ids</a>(benefit_id) -> <a href="./src/finch/types/hris/benefits/individual_enrolled_ids_response.py">IndividualEnrolledIDsResponse</a></code>
- <code title="get /employer/benefits/{benefit_id}/individuals">client.hris.benefits.individuals.<a href="./src/finch/resources/hris/benefits/individuals.py">retrieve_many_benefits</a>(benefit_id, \*\*<a href="src/finch/types/hris/benefits/individual_retrieve_many_benefits_params.py">params</a>) -> <a href="./src/finch/types/hris/benefits/individual_benefit.py">SyncSinglePage[IndividualBenefit]</a></code>
- <code title="delete /employer/benefits/{benefit_id}/individuals">client.hris.benefits.individuals.<a href="./src/finch/resources/hris/benefits/individuals.py">unenroll_many</a>(benefit_id, \*\*<a href="src/finch/types/hris/benefits/individual_unenroll_many_params.py">params</a>) -> <a href="./src/finch/types/hris/benefits/unenrolled_individual.py">SyncSinglePage[UnenrolledIndividual]</a></code>

# Providers

Types:

```python
from finch.types import Provider
```

Methods:

- <code title="get /providers">client.providers.<a href="./src/finch/resources/providers.py">list</a>() -> <a href="./src/finch/types/provider.py">SyncSinglePage[Provider]</a></code>

# Account

Types:

```python
from finch.types import DisconnectResponse, Introspection
```

Methods:

- <code title="post /disconnect">client.account.<a href="./src/finch/resources/account.py">disconnect</a>() -> <a href="./src/finch/types/disconnect_response.py">DisconnectResponse</a></code>
- <code title="get /introspect">client.account.<a href="./src/finch/resources/account.py">introspect</a>() -> <a href="./src/finch/types/introspection.py">Introspection</a></code>

# Webhooks

Methods:

- <code>client.webhooks.<a href="./src/finch/resources/webhooks.py">unwrap</a>(\*args) -> object</code>
- <code>client.webhooks.<a href="./src/finch/resources/webhooks.py">verify_signature</a>(\*args) -> None</code>

# RequestForwarding

Types:

```python
from finch.types import RequestForwardingForwardResponse
```

Methods:

- <code title="post /forward">client.request_forwarding.<a href="./src/finch/resources/request_forwarding.py">forward</a>(\*\*<a href="src/finch/types/request_forwarding_forward_params.py">params</a>) -> <a href="./src/finch/types/request_forwarding_forward_response.py">RequestForwardingForwardResponse</a></code>

# Jobs

## Automated

Types:

```python
from finch.types.jobs import AutomatedAsyncJob, AutomatedCreateResponse
```

Methods:

- <code title="post /jobs/automated">client.jobs.automated.<a href="./src/finch/resources/jobs/automated.py">create</a>(\*\*<a href="src/finch/types/jobs/automated_create_params.py">params</a>) -> <a href="./src/finch/types/jobs/automated_create_response.py">AutomatedCreateResponse</a></code>
- <code title="get /jobs/automated/{job_id}">client.jobs.automated.<a href="./src/finch/resources/jobs/automated.py">retrieve</a>(job_id) -> <a href="./src/finch/types/jobs/automated_async_job.py">AutomatedAsyncJob</a></code>
- <code title="get /jobs/automated">client.jobs.automated.<a href="./src/finch/resources/jobs/automated.py">list</a>(\*\*<a href="src/finch/types/jobs/automated_list_params.py">params</a>) -> <a href="./src/finch/types/jobs/automated_async_job.py">SyncPage[AutomatedAsyncJob]</a></code>

## Manual

Types:

```python
from finch.types.jobs import ManualAsyncJob
```

Methods:

- <code title="get /jobs/manual/{job_id}">client.jobs.manual.<a href="./src/finch/resources/jobs/manual.py">retrieve</a>(job_id) -> <a href="./src/finch/types/jobs/manual_async_job.py">ManualAsyncJob</a></code>
