# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .benefit_support_type import BenefitSupportType

__all__ = [
    "Provider",
    "AuthenticationMethod",
    "AuthenticationMethodBenefitsSupport",
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
    "AuthenticationMethodSupportedFieldsIndividual",
    "AuthenticationMethodSupportedFieldsIndividualEmails",
    "AuthenticationMethodSupportedFieldsIndividualPhoneNumbers",
    "AuthenticationMethodSupportedFieldsIndividualResidence",
    "AuthenticationMethodSupportedFieldsPayStatement",
    "AuthenticationMethodSupportedFieldsPayStatementPaging",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatements",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatementsEarnings",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployeeDeductions",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployerDeductions",
    "AuthenticationMethodSupportedFieldsPayStatementPayStatementsTaxes",
    "AuthenticationMethodSupportedFieldsPayment",
    "AuthenticationMethodSupportedFieldsPaymentPayPeriod",
]


class AuthenticationMethodBenefitsSupport(BaseModel):
    retirement_401k: Optional[BenefitSupportType] = FieldInfo(alias="401k", default=None)

    retirement_401k_loan: Optional[BenefitSupportType] = FieldInfo(alias="401k_loan", default=None)

    retirement_401k_roth: Optional[BenefitSupportType] = FieldInfo(alias="401k_roth", default=None)

    retirement_403b: Optional[BenefitSupportType] = FieldInfo(alias="403b", default=None)

    retirement_403b_roth: Optional[BenefitSupportType] = FieldInfo(alias="403b_roth", default=None)

    retirement_457: Optional[BenefitSupportType] = FieldInfo(alias="457", default=None)

    retirement_457_roth: Optional[BenefitSupportType] = FieldInfo(alias="457_roth", default=None)

    commuter: Optional[BenefitSupportType] = None

    custom_post_tax: Optional[BenefitSupportType] = None

    custom_pre_tax: Optional[BenefitSupportType] = None

    fsa_dependent_care: Optional[BenefitSupportType] = None

    fsa_medical: Optional[BenefitSupportType] = None

    hsa_post: Optional[BenefitSupportType] = None

    hsa_pre: Optional[BenefitSupportType] = None

    s125_dental: Optional[BenefitSupportType] = None

    s125_medical: Optional[BenefitSupportType] = None

    s125_vision: Optional[BenefitSupportType] = None

    simple: Optional[BenefitSupportType] = None

    simple_ira: Optional[BenefitSupportType] = None


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

    department: Optional[object] = None

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

    manager: Optional[object] = None

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

    employer_deductions: Optional[AuthenticationMethodSupportedFieldsPayStatementPayStatementsEmployerDeductions] = None

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

    pay_period: Optional[AuthenticationMethodSupportedFieldsPaymentPayPeriod] = None


class AuthenticationMethodSupportedFields(BaseModel):
    company: Optional[AuthenticationMethodSupportedFieldsCompany] = None

    directory: Optional[AuthenticationMethodSupportedFieldsDirectory] = None

    employment: Optional[AuthenticationMethodSupportedFieldsEmployment] = None

    individual: Optional[AuthenticationMethodSupportedFieldsIndividual] = None

    pay_statement: Optional[AuthenticationMethodSupportedFieldsPayStatement] = None

    payment: Optional[AuthenticationMethodSupportedFieldsPayment] = None


class AuthenticationMethod(BaseModel):
    benefits_support: Optional[AuthenticationMethodBenefitsSupport] = None
    """Each benefit type and their supported features.

    If the benefit type is not supported, the property will be null
    """

    supported_fields: Optional[AuthenticationMethodSupportedFields] = None
    """The supported data fields returned by our HR and payroll endpoints"""

    type: Optional[Literal["assisted", "credential", "api_token", "oauth"]] = None
    """The type of authentication method."""


class Provider(BaseModel):
    id: Optional[str] = None
    """The id of the payroll provider used in Connect."""

    authentication_methods: Optional[List[AuthenticationMethod]] = None
    """The list of authentication methods supported by the provider."""

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
