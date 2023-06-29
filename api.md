# Finch

Methods:

- <code>client.<a href="./src/finch/_client.py">get_access_token</a>(\*args) -> str</code>
- <code>client.<a href="./src/finch/_client.py">get_auth_url</a>(\*args) -> str</code>

# ATS

## Candidates

Types:

```python
from finch.types.ats import Candidate
```

Methods:

- <code title="get /ats/candidates/{candidate_id}">client.ats.candidates.<a href="./src/finch/resources/ats/candidates.py">retrieve</a>(candidate_id) -> <a href="./src/finch/types/ats/candidate.py">Candidate</a></code>
- <code title="get /ats/candidates">client.ats.candidates.<a href="./src/finch/resources/ats/candidates.py">list</a>(\*\*<a href="src/finch/types/ats/candidate_list_params.py">params</a>) -> <a href="./src/finch/types/ats/candidate.py">SyncCandidatesPage[Candidate]</a></code>

## Applications

Types:

```python
from finch.types.ats import Application
```

Methods:

- <code title="get /ats/applications/{application_id}">client.ats.applications.<a href="./src/finch/resources/ats/applications.py">retrieve</a>(application_id) -> <a href="./src/finch/types/ats/application.py">Application</a></code>
- <code title="get /ats/applications">client.ats.applications.<a href="./src/finch/resources/ats/applications.py">list</a>(\*\*<a href="src/finch/types/ats/application_list_params.py">params</a>) -> <a href="./src/finch/types/ats/application.py">SyncApplicationsPage[Application]</a></code>

## Stages

Types:

```python
from finch.types.ats import Stage
```

Methods:

- <code title="get /ats/stages">client.ats.stages.<a href="./src/finch/resources/ats/stages.py">list</a>() -> <a href="./src/finch/types/ats/stage.py">SyncSinglePage[Stage]</a></code>

## Jobs

Types:

```python
from finch.types.ats import Job
```

Methods:

- <code title="get /ats/jobs/{job_id}">client.ats.jobs.<a href="./src/finch/resources/ats/jobs.py">retrieve</a>(job_id) -> <a href="./src/finch/types/ats/job.py">Job</a></code>
- <code title="get /ats/jobs">client.ats.jobs.<a href="./src/finch/resources/ats/jobs.py">list</a>(\*\*<a href="src/finch/types/ats/job_list_params.py">params</a>) -> <a href="./src/finch/types/ats/job.py">SyncJobsPage[Job]</a></code>

## Offers

Types:

```python
from finch.types.ats import Offer
```

Methods:

- <code title="get /ats/offers/{offer_id}">client.ats.offers.<a href="./src/finch/resources/ats/offers.py">retrieve</a>(offer_id) -> <a href="./src/finch/types/ats/offer.py">Offer</a></code>
- <code title="get /ats/offers">client.ats.offers.<a href="./src/finch/resources/ats/offers.py">list</a>(\*\*<a href="src/finch/types/ats/offer_list_params.py">params</a>) -> <a href="./src/finch/types/ats/offer.py">SyncOffersPage[Offer]</a></code>

# HRIS

Types:

```python
from finch.types import Income, Location, Money, Paging
```

## CompanyResource

Types:

```python
from finch.types.hris import Company
```

Methods:

- <code title="get /employer/company">client.hris.company.<a href="./src/finch/resources/hris/company.py">retrieve</a>() -> <a href="./src/finch/types/hris/company.py">Company</a></code>

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
from finch.types.hris import (
    PayStatement,
    PayStatementResponse,
    PayStatementResponseBody,
)
```

Methods:

- <code title="post /employer/pay-statement">client.hris.pay_statements.<a href="./src/finch/resources/hris/pay_statements.py">retrieve_many</a>(\*\*<a href="src/finch/types/hris/pay_statement_retrieve_many_params.py">params</a>) -> <a href="./src/finch/types/hris/pay_statement_response.py">SyncResponsesPage[PayStatementResponse]</a></code>

## Directory

Types:

```python
from finch.types.hris import IndividualInDirectory
```

Methods:

- <code title="get /employer/directory">client.hris.directory.<a href="./src/finch/resources/hris/directory.py">list_individuals</a>(\*\*<a href="src/finch/types/hris/directory_list_individuals_params.py">params</a>) -> <a href="./src/finch/types/hris/individual_in_directory.py">SyncIndividualsPage[IndividualInDirectory]</a></code>

## Individuals

Types:

```python
from finch.types.hris import Individual, IndividualResponse
```

Methods:

- <code title="post /employer/individual">client.hris.individuals.<a href="./src/finch/resources/hris/individuals/individuals.py">retrieve_many</a>(\*\*<a href="src/finch/types/hris/individual_retrieve_many_params.py">params</a>) -> <a href="./src/finch/types/hris/individual_response.py">SyncResponsesPage[IndividualResponse]</a></code>

### EmploymentData

Types:

```python
from finch.types.hris.individuals import EmploymentData, EmploymentDataResponse
```

Methods:

- <code title="post /employer/employment">client.hris.individuals.employment_data.<a href="./src/finch/resources/hris/individuals/employment_data.py">retrieve_many</a>(\*\*<a href="src/finch/types/hris/individuals/employment_data_retrieve_many_params.py">params</a>) -> <a href="./src/finch/types/hris/individuals/employment_data_response.py">SyncResponsesPage[EmploymentDataResponse]</a></code>

## Benefits

Types:

```python
from finch.types.hris import (
    BenefitFrequency,
    BenefitType,
    BenfitContribution,
    CompanyBenefit,
    CreateCompanyBenefitsResponse,
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
- <code title="delete /employer/benefits/{benefit_id}/individuals">client.hris.benefits.individuals.<a href="./src/finch/resources/hris/benefits/individuals.py">unenroll</a>(benefit_id, \*\*<a href="src/finch/types/hris/benefits/individual_unenroll_params.py">params</a>) -> <a href="./src/finch/types/hris/benefits/unenrolled_individual.py">SyncSinglePage[UnenrolledIndividual]</a></code>

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
