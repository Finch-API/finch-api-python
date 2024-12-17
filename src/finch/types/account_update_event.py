# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent
from .hris.benefits_support import BenefitsSupport
from .shared.connection_status_type import ConnectionStatusType

__all__ = [
    "AccountUpdateEvent",
    "AccountUpdateEventData",
    "AccountUpdateEventDataAuthenticationMethod",
    "AccountUpdateEventDataAuthenticationMethodSupportedFields",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompany",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompanyAccounts",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompanyDepartments",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompanyDepartmentsParent",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompanyEntity",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompanyLocations",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsDirectory",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsDirectoryIndividuals",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsDirectoryIndividualsManager",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsDirectoryPaging",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmployment",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmploymentDepartment",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmploymentEmployment",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmploymentIncome",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmploymentLocation",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmploymentManager",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsIndividual",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsIndividualEmails",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsIndividualPhoneNumbers",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsIndividualResidence",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayGroup",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatement",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPaging",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPayStatements",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPayStatementsEarnings",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployeeDeductions",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployerContributions",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPayStatementsTaxes",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayment",
    "AccountUpdateEventDataAuthenticationMethodSupportedFieldsPaymentPayPeriod",
]


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompanyAccounts(BaseModel):
    account_name: Optional[bool] = None

    account_number: Optional[bool] = None

    account_type: Optional[bool] = None

    institution_name: Optional[bool] = None

    routing_number: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompanyDepartmentsParent(BaseModel):
    name: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompanyDepartments(BaseModel):
    name: Optional[bool] = None

    parent: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompanyDepartmentsParent] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompanyEntity(BaseModel):
    subtype: Optional[bool] = None

    type: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompanyLocations(BaseModel):
    city: Optional[bool] = None

    country: Optional[bool] = None

    line1: Optional[bool] = None

    line2: Optional[bool] = None

    postal_code: Optional[bool] = None

    state: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompany(BaseModel):
    id: Optional[bool] = None

    accounts: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompanyAccounts] = None

    departments: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompanyDepartments] = None

    ein: Optional[bool] = None

    entity: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompanyEntity] = None

    legal_name: Optional[bool] = None

    locations: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompanyLocations] = None

    primary_email: Optional[bool] = None

    primary_phone_number: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsDirectoryIndividualsManager(BaseModel):
    id: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsDirectoryIndividuals(BaseModel):
    id: Optional[bool] = None

    department: Optional[bool] = None

    first_name: Optional[bool] = None

    is_active: Optional[bool] = None

    last_name: Optional[bool] = None

    manager: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsDirectoryIndividualsManager] = None

    middle_name: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsDirectoryPaging(BaseModel):
    count: Optional[bool] = None

    offset: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsDirectory(BaseModel):
    individuals: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsDirectoryIndividuals] = None

    paging: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsDirectoryPaging] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmploymentDepartment(BaseModel):
    name: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmploymentEmployment(BaseModel):
    subtype: Optional[bool] = None

    type: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmploymentIncome(BaseModel):
    amount: Optional[bool] = None

    currency: Optional[bool] = None

    unit: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmploymentLocation(BaseModel):
    city: Optional[bool] = None

    country: Optional[bool] = None

    line1: Optional[bool] = None

    line2: Optional[bool] = None

    postal_code: Optional[bool] = None

    state: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmploymentManager(BaseModel):
    id: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmployment(BaseModel):
    id: Optional[bool] = None

    class_code: Optional[bool] = None

    custom_fields: Optional[bool] = None

    department: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmploymentDepartment] = None

    employment: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmploymentEmployment] = None

    employment_status: Optional[bool] = None

    end_date: Optional[bool] = None

    first_name: Optional[bool] = None

    income_history: Optional[bool] = None

    income: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmploymentIncome] = None

    is_active: Optional[bool] = None

    last_name: Optional[bool] = None

    location: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmploymentLocation] = None

    manager: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmploymentManager] = None

    middle_name: Optional[bool] = None

    start_date: Optional[bool] = None

    title: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsIndividualEmails(BaseModel):
    data: Optional[bool] = None

    type: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsIndividualPhoneNumbers(BaseModel):
    data: Optional[bool] = None

    type: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsIndividualResidence(BaseModel):
    city: Optional[bool] = None

    country: Optional[bool] = None

    line1: Optional[bool] = None

    line2: Optional[bool] = None

    postal_code: Optional[bool] = None

    state: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsIndividual(BaseModel):
    id: Optional[bool] = None

    dob: Optional[bool] = None

    emails: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsIndividualEmails] = None

    encrypted_ssn: Optional[bool] = None

    ethnicity: Optional[bool] = None

    first_name: Optional[bool] = None

    gender: Optional[bool] = None

    last_name: Optional[bool] = None

    middle_name: Optional[bool] = None

    phone_numbers: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsIndividualPhoneNumbers] = None

    preferred_name: Optional[bool] = None

    residence: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsIndividualResidence] = None

    ssn: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayGroup(BaseModel):
    id: Optional[bool] = None

    individual_ids: Optional[bool] = None

    name: Optional[bool] = None

    pay_frequencies: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPaging(BaseModel):
    count: bool

    offset: bool


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPayStatementsEarnings(BaseModel):
    amount: Optional[bool] = None

    currency: Optional[bool] = None

    name: Optional[bool] = None

    type: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployeeDeductions(BaseModel):
    amount: Optional[bool] = None

    currency: Optional[bool] = None

    name: Optional[bool] = None

    pre_tax: Optional[bool] = None

    type: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployerContributions(
    BaseModel
):
    amount: Optional[bool] = None

    currency: Optional[bool] = None

    name: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPayStatementsTaxes(BaseModel):
    amount: Optional[bool] = None

    currency: Optional[bool] = None

    employer: Optional[bool] = None

    name: Optional[bool] = None

    type: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPayStatements(BaseModel):
    earnings: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPayStatementsEarnings] = (
        None
    )

    employee_deductions: Optional[
        AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployeeDeductions
    ] = None

    employer_contributions: Optional[
        AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployerContributions
    ] = None

    gross_pay: Optional[bool] = None

    individual_id: Optional[bool] = None

    net_pay: Optional[bool] = None

    payment_method: Optional[bool] = None

    taxes: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPayStatementsTaxes] = None

    total_hours: Optional[bool] = None

    type: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatement(BaseModel):
    paging: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPaging] = None

    pay_statements: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatementPayStatements] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsPaymentPayPeriod(BaseModel):
    end_date: Optional[bool] = None

    start_date: Optional[bool] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayment(BaseModel):
    id: Optional[bool] = None

    company_debit: Optional[bool] = None

    debit_date: Optional[bool] = None

    employee_taxes: Optional[bool] = None

    employer_taxes: Optional[bool] = None

    gross_pay: Optional[bool] = None

    individual_ids: Optional[bool] = None

    net_pay: Optional[bool] = None

    pay_date: Optional[bool] = None

    pay_frequencies: Optional[bool] = None

    pay_group_ids: Optional[bool] = None

    pay_period: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsPaymentPayPeriod] = None


class AccountUpdateEventDataAuthenticationMethodSupportedFields(BaseModel):
    company: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsCompany] = None

    directory: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsDirectory] = None

    employment: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsEmployment] = None

    individual: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsIndividual] = None

    pay_group: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayGroup] = None

    pay_statement: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayStatement] = None

    payment: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFieldsPayment] = None


class AccountUpdateEventDataAuthenticationMethod(BaseModel):
    benefits_support: Optional[BenefitsSupport] = None
    """Each benefit type and their supported features.

    If the benefit type is not supported, the property will be null
    """

    supported_fields: Optional[AccountUpdateEventDataAuthenticationMethodSupportedFields] = None
    """The supported data fields returned by our HR and payroll endpoints"""

    type: Optional[Literal["assisted", "credential", "api_token", "api_credential", "oauth"]] = None
    """The type of authentication method."""


class AccountUpdateEventData(BaseModel):
    authentication_method: AccountUpdateEventDataAuthenticationMethod

    status: ConnectionStatusType


class AccountUpdateEvent(BaseWebhookEvent):
    data: Optional[AccountUpdateEventData] = None

    event_type: Optional[Literal["account.updated"]] = None
