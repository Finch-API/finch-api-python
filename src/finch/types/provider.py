# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .hris.benefits_support import BenefitsSupport

__all__ = [
    "Provider",
    "AuthenticationMethod",
    "AuthenticationMethodSupportedFields",
    "AuthenticationMethodSupportedFieldsCompany",
    "AuthenticationMethodSupportedFieldsCompanyAccounts",
    "AuthenticationMethodSupportedFieldsCompanyDepartments",
    "AuthenticationMethodSupportedFieldsCompanyDepartmentsParent",
    "AuthenticationMethodSupportedFieldsCompanyEntity",
    "AuthenticationMethodSupportedFieldsCompanyLocations",
    "AuthenticationMethodSupportedFieldsDirectory",
    "AuthenticationMethodSupportedFieldsDirectoryIndividuals",
    "AuthenticationMethodSupportedFieldsDirectoryIndividualsManager",
    "AuthenticationMethodSupportedFieldsDirectoryPaging",
    "AuthenticationMethodSupportedFieldsEmployment",
    "AuthenticationMethodSupportedFieldsEmploymentDepartment",
    "AuthenticationMethodSupportedFieldsEmploymentEmployment",
    "AuthenticationMethodSupportedFieldsEmploymentIncome",
    "AuthenticationMethodSupportedFieldsEmploymentLocation",
    "AuthenticationMethodSupportedFieldsEmploymentManager",
    "AuthenticationMethodSupportedFieldsIndividual",
    "AuthenticationMethodSupportedFieldsIndividualEmails",
    "AuthenticationMethodSupportedFieldsIndividualPhoneNumbers",
    "AuthenticationMethodSupportedFieldsIndividualResidence",
    "AuthenticationMethodSupportedFieldsPayStatement",
    "AuthenticationMethodSupportedFieldsPayStatementPaging",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatements",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatementsEarnings",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployeeDeductions",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployerContributions",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployerDeductions",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatementsTaxes",
    "AuthenticationMethodSupportedFieldsPayment",
    "AuthenticationMethodSupportedFieldsPaymentPayPeriod",
]


class AuthenticationMethodSupportedFieldsCompanyAccounts(BaseModel):
    account_name: Optional[bool] = None

    account_number: Optional[bool] = None

    account_type: Optional[bool] = None

    institution_name: Optional[bool] = None

    routing_number: Optional[bool] = None


class AuthenticationMethodSupportedFieldsCompanyDepartmentsParent(BaseModel):
    name: Optional[bool] = None


class AuthenticationMethodSupportedFieldsCompanyDepartments(BaseModel):
    name: Optional[bool] = None

    parent: Optional[AuthenticationMethodSupportedFieldsCompanyDepartmentsParent] = None


class AuthenticationMethodSupportedFieldsCompanyEntity(BaseModel):
    subtype: Optional[bool] = None

    type: Optional[bool] = None


class AuthenticationMethodSupportedFieldsCompanyLocations(BaseModel):
    city: Optional[bool] = None

    country: Optional[bool] = None

    line1: Optional[bool] = None

    line2: Optional[bool] = None

    postal_code: Optional[bool] = None

    state: Optional[bool] = None


class AuthenticationMethodSupportedFieldsCompany(BaseModel):
    id: Optional[bool] = None

    accounts: Optional[AuthenticationMethodSupportedFieldsCompanyAccounts] = None

    departments: Optional[AuthenticationMethodSupportedFieldsCompanyDepartments] = None

    ein: Optional[bool] = None

    entity: Optional[AuthenticationMethodSupportedFieldsCompanyEntity] = None

    legal_name: Optional[bool] = None

    locations: Optional[AuthenticationMethodSupportedFieldsCompanyLocations] = None

    primary_email: Optional[bool] = None

    primary_phone_number: Optional[bool] = None


class AuthenticationMethodSupportedFieldsDirectoryIndividualsManager(BaseModel):
    id: Optional[bool] = None


class AuthenticationMethodSupportedFieldsDirectoryIndividuals(BaseModel):
    id: Optional[bool] = None

    department: Optional[bool] = None

    first_name: Optional[bool] = None

    is_active: Optional[bool] = None

    last_name: Optional[bool] = None

    manager: Optional[AuthenticationMethodSupportedFieldsDirectoryIndividualsManager] = None

    middle_name: Optional[bool] = None


class AuthenticationMethodSupportedFieldsDirectoryPaging(BaseModel):
    count: Optional[bool] = None

    offset: Optional[bool] = None


class AuthenticationMethodSupportedFieldsDirectory(BaseModel):
    individuals: Optional[AuthenticationMethodSupportedFieldsDirectoryIndividuals] = None

    paging: Optional[AuthenticationMethodSupportedFieldsDirectoryPaging] = None


class AuthenticationMethodSupportedFieldsEmploymentDepartment(BaseModel):
    name: Optional[bool] = None


class AuthenticationMethodSupportedFieldsEmploymentEmployment(BaseModel):
    subtype: Optional[bool] = None

    type: Optional[bool] = None


class AuthenticationMethodSupportedFieldsEmploymentIncome(BaseModel):
    amount: Optional[bool] = None

    currency: Optional[bool] = None

    unit: Optional[bool] = None


class AuthenticationMethodSupportedFieldsEmploymentLocation(BaseModel):
    city: Optional[bool] = None

    country: Optional[bool] = None

    line1: Optional[bool] = None

    line2: Optional[bool] = None

    postal_code: Optional[bool] = None

    state: Optional[bool] = None


class AuthenticationMethodSupportedFieldsEmploymentManager(BaseModel):
    id: Optional[bool] = None


class AuthenticationMethodSupportedFieldsEmployment(BaseModel):
    id: Optional[bool] = None

    class_code: Optional[bool] = None

    custom_fields: Optional[bool] = None

    department: Optional[AuthenticationMethodSupportedFieldsEmploymentDepartment] = None

    employment: Optional[AuthenticationMethodSupportedFieldsEmploymentEmployment] = None

    end_date: Optional[bool] = None

    first_name: Optional[bool] = None

    income_history: Optional[bool] = None

    income: Optional[AuthenticationMethodSupportedFieldsEmploymentIncome] = None

    is_active: Optional[bool] = None

    last_name: Optional[bool] = None

    location: Optional[AuthenticationMethodSupportedFieldsEmploymentLocation] = None

    manager: Optional[AuthenticationMethodSupportedFieldsEmploymentManager] = None

    middle_name: Optional[bool] = None

    start_date: Optional[bool] = None

    title: Optional[bool] = None


class AuthenticationMethodSupportedFieldsIndividualEmails(BaseModel):
    data: Optional[bool] = None

    type: Optional[bool] = None


class AuthenticationMethodSupportedFieldsIndividualPhoneNumbers(BaseModel):
    data: Optional[bool] = None

    type: Optional[bool] = None


class AuthenticationMethodSupportedFieldsIndividualResidence(BaseModel):
    city: Optional[bool] = None

    country: Optional[bool] = None

    line1: Optional[bool] = None

    line2: Optional[bool] = None

    postal_code: Optional[bool] = None

    state: Optional[bool] = None


class AuthenticationMethodSupportedFieldsIndividual(BaseModel):
    id: Optional[bool] = None

    dob: Optional[bool] = None

    emails: Optional[AuthenticationMethodSupportedFieldsIndividualEmails] = None

    encrypted_ssn: Optional[bool] = None

    ethnicity: Optional[bool] = None

    first_name: Optional[bool] = None

    gender: Optional[bool] = None

    last_name: Optional[bool] = None

    middle_name: Optional[bool] = None

    phone_numbers: Optional[AuthenticationMethodSupportedFieldsIndividualPhoneNumbers] = None

    preferred_name: Optional[bool] = None

    residence: Optional[AuthenticationMethodSupportedFieldsIndividualResidence] = None

    ssn: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPayStatementPaging(BaseModel):
    count: bool

    offset: bool


class AuthenticationMethodSupportedFieldsPayStatementPayStatementsEarnings(BaseModel):
    amount: Optional[bool] = None

    currency: Optional[bool] = None

    name: Optional[bool] = None

    type: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployeeDeductions(BaseModel):
    amount: Optional[bool] = None

    currency: Optional[bool] = None

    name: Optional[bool] = None

    pre_tax: Optional[bool] = None

    type: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployerContributions(BaseModel):
    amount: Optional[bool] = None

    currency: Optional[bool] = None

    name: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployerDeductions(BaseModel):
    amount: Optional[bool] = None

    currency: Optional[bool] = None

    name: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPayStatementPayStatementsTaxes(BaseModel):
    amount: Optional[bool] = None

    currency: Optional[bool] = None

    employer: Optional[bool] = None

    name: Optional[bool] = None

    type: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPayStatementPayStatements(BaseModel):
    earnings: Optional[AuthenticationMethodSupportedFieldsPayStatementPayStatementsEarnings] = None

    employee_deductions: Optional[AuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployeeDeductions] = None

    employer_contributions: Optional[
        AuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployerContributions
    ] = None

    employer_deductions: Optional[AuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployerDeductions] = None
    """[DEPRECATED] Use `employer_contributions` instead"""

    gross_pay: Optional[bool] = None

    individual_id: Optional[bool] = None

    net_pay: Optional[bool] = None

    payment_method: Optional[bool] = None

    taxes: Optional[AuthenticationMethodSupportedFieldsPayStatementPayStatementsTaxes] = None

    total_hours: Optional[bool] = None

    type: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPayStatement(BaseModel):
    paging: Optional[AuthenticationMethodSupportedFieldsPayStatementPaging] = None

    pay_statements: Optional[AuthenticationMethodSupportedFieldsPayStatementPayStatements] = None


class AuthenticationMethodSupportedFieldsPaymentPayPeriod(BaseModel):
    end_date: Optional[bool] = None

    start_date: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPayment(BaseModel):
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

    pay_period: Optional[AuthenticationMethodSupportedFieldsPaymentPayPeriod] = None


class AuthenticationMethodSupportedFields(BaseModel):
    company: Optional[AuthenticationMethodSupportedFieldsCompany] = None

    directory: Optional[AuthenticationMethodSupportedFieldsDirectory] = None

    employment: Optional[AuthenticationMethodSupportedFieldsEmployment] = None

    individual: Optional[AuthenticationMethodSupportedFieldsIndividual] = None

    pay_statement: Optional[AuthenticationMethodSupportedFieldsPayStatement] = None

    payment: Optional[AuthenticationMethodSupportedFieldsPayment] = None


class AuthenticationMethod(BaseModel):
    benefits_support: Optional[BenefitsSupport] = None
    """Each benefit type and their supported features.

    If the benefit type is not supported, the property will be null
    """

    supported_fields: Optional[AuthenticationMethodSupportedFields] = None
    """The supported data fields returned by our HR and payroll endpoints"""

    type: Optional[Literal["assisted", "credential", "api_token", "api_credential", "oauth"]] = None
    """The type of authentication method."""


class Provider(BaseModel):
    id: Optional[str] = None
    """The id of the payroll provider used in Connect."""

    authentication_methods: Optional[List[AuthenticationMethod]] = None
    """The list of authentication methods supported by the provider."""

    beta: Optional[bool] = None
    """`true` if the integration is in a beta state, `false` otherwise"""

    display_name: Optional[str] = None
    """The display name of the payroll provider."""

    icon: Optional[str] = None
    """The url to the official icon of the payroll provider."""

    logo: Optional[str] = None
    """The url to the official logo of the payroll provider."""

    manual: Optional[bool] = None
    """
    [DEPRECATED] Whether the Finch integration with this provider uses the Assisted
    Connect Flow by default. This field is now deprecated. Please check for a `type`
    of `assisted` in the `authentication_methods` field instead.
    """

    mfa_required: Optional[bool] = None
    """whether MFA is required for the provider."""

    primary_color: Optional[str] = None
    """The hex code for the primary color of the payroll provider."""

    products: Optional[List[str]] = None
    """The list of Finch products supported on this payroll provider."""
