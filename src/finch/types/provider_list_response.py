# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ProviderListResponse",
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
    "AuthenticationMethodSupportedFieldsPayGroup",
    "AuthenticationMethodSupportedFieldsPayStatement",
    "AuthenticationMethodSupportedFieldsPayStatementPaging",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatements",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatementsEarnings",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployeeDeductions",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployerContributions",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatementsTaxes",
    "AuthenticationMethodSupportedFieldsPayment",
    "AuthenticationMethodSupportedFieldsPaymentPayPeriod",
    "AuthenticationMethodSupportedFieldsPlanDependents",
    "AuthenticationMethodSupportedFieldsPlanDependentsCoverage",
    "AuthenticationMethodSupportedFieldsPlanDependentsCoverageEnrollments",
    "AuthenticationMethodSupportedFieldsPlanEnrollments",
    "AuthenticationMethodSupportedFieldsPlanEnrollmentsContributions",
    "AuthenticationMethodSupportedFieldsPlanEnrollmentsContributionsEmployeeContribution",
    "AuthenticationMethodSupportedFieldsPlanEnrollmentsContributionsEmployerContribution",
    "AuthenticationMethodSupportedFieldsPlans",
    "AuthenticationMethodSupportedFieldsPlansCarrier",
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

    employment_status: Optional[bool] = None

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


class AuthenticationMethodSupportedFieldsPayGroup(BaseModel):
    id: Optional[bool] = None

    individual_ids: Optional[bool] = None

    name: Optional[bool] = None

    pay_frequencies: Optional[bool] = None


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


class AuthenticationMethodSupportedFieldsPlanDependentsCoverageEnrollments(BaseModel):
    id: Optional[bool] = None

    type: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPlanDependentsCoverage(BaseModel):
    enrollments: Optional[AuthenticationMethodSupportedFieldsPlanDependentsCoverageEnrollments] = None

    individual_id: Optional[bool] = None

    relationship_to_individual: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPlanDependents(BaseModel):
    coverage: Optional[AuthenticationMethodSupportedFieldsPlanDependentsCoverage] = None

    date_of_birth: Optional[bool] = None

    dependent_id: Optional[bool] = None

    first_name: Optional[bool] = None

    gender: Optional[bool] = None

    last_name: Optional[bool] = None

    middle_name: Optional[bool] = None

    ssn: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPlanEnrollmentsContributionsEmployeeContribution(BaseModel):
    amount: Optional[bool] = None

    currency: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPlanEnrollmentsContributionsEmployerContribution(BaseModel):
    amount: Optional[bool] = None

    currency: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPlanEnrollmentsContributions(BaseModel):
    employee_contribution: Optional[
        AuthenticationMethodSupportedFieldsPlanEnrollmentsContributionsEmployeeContribution
    ] = None

    employer_contribution: Optional[
        AuthenticationMethodSupportedFieldsPlanEnrollmentsContributionsEmployerContribution
    ] = None

    frequency: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPlanEnrollments(BaseModel):
    id: Optional[bool] = None

    contributions: Optional[AuthenticationMethodSupportedFieldsPlanEnrollmentsContributions] = None

    coverage_end_date: Optional[bool] = None

    coverage_start_date: Optional[bool] = None

    coverage_tier: Optional[bool] = None

    dependent_ids: Optional[bool] = None

    individual_id: Optional[bool] = None

    plan_id: Optional[bool] = None

    status: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPlansCarrier(BaseModel):
    id: Optional[bool] = None

    name: Optional[bool] = None


class AuthenticationMethodSupportedFieldsPlans(BaseModel):
    id: Optional[bool] = None

    carrier: Optional[AuthenticationMethodSupportedFieldsPlansCarrier] = None

    coverage_tiers: Optional[bool] = None

    deduction_codes: Optional[bool] = None

    description: Optional[bool] = None

    end_date: Optional[bool] = None

    name: Optional[bool] = None

    network_type: Optional[bool] = None

    start_date: Optional[bool] = None

    type: Optional[bool] = None


class AuthenticationMethodSupportedFields(BaseModel):
    """The supported data fields returned by our HR, payroll, and benefits endpoints"""

    company: Optional[AuthenticationMethodSupportedFieldsCompany] = None

    directory: Optional[AuthenticationMethodSupportedFieldsDirectory] = None

    employment: Optional[AuthenticationMethodSupportedFieldsEmployment] = None

    individual: Optional[AuthenticationMethodSupportedFieldsIndividual] = None

    pay_group: Optional[AuthenticationMethodSupportedFieldsPayGroup] = None

    pay_statement: Optional[AuthenticationMethodSupportedFieldsPayStatement] = None

    payment: Optional[AuthenticationMethodSupportedFieldsPayment] = None

    plan_dependents: Optional[AuthenticationMethodSupportedFieldsPlanDependents] = None

    plan_enrollments: Optional[AuthenticationMethodSupportedFieldsPlanEnrollments] = None

    plans: Optional[AuthenticationMethodSupportedFieldsPlans] = None


class AuthenticationMethod(BaseModel):
    type: Literal["assisted", "credential", "api_token", "api_credential", "oauth", "api"]
    """The type of authentication method"""

    benefits_support: Optional[Dict[str, Optional[object]]] = None
    """The supported benefit types and their configurations"""

    supported_fields: Optional[AuthenticationMethodSupportedFields] = None
    """The supported data fields returned by our HR, payroll, and benefits endpoints"""


class ProviderListResponse(BaseModel):
    id: str
    """The id of the payroll provider used in Connect."""

    display_name: str
    """The display name of the payroll provider."""

    products: List[str]
    """The list of Finch products supported on this payroll provider."""

    authentication_methods: Optional[List[AuthenticationMethod]] = None
    """The authentication methods supported by the provider."""

    beta: Optional[bool] = None
    """`true` if the integration is in a beta state, `false` otherwise"""

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
