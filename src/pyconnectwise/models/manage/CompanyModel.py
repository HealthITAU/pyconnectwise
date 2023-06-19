from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CompanyStatusReferenceModel import CompanyStatusReferenceModel
from pyconnectwise.models.manage.CountryReferenceModel import CountryReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.MarketDescriptionReferenceModel import MarketDescriptionReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SicCodeReferenceModel import SicCodeReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.OwnershipTypeReferenceModel import OwnershipTypeReferenceModel
from pyconnectwise.models.manage.TimeZoneSetupReferenceModel import TimeZoneSetupReferenceModel
from pyconnectwise.models.manage.CalendarReferenceModel import CalendarReferenceModel
from pyconnectwise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pyconnectwise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pyconnectwise.models.manage.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pyconnectwise.models.manage.PricingScheduleReferenceModel import PricingScheduleReferenceModel
from pyconnectwise.models.manage.EntityTypeReferenceModel import EntityTypeReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.BillingDeliveryReferenceModel import BillingDeliveryReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.CompanyTypeReferenceModel import CompanyTypeReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel

class CompanyModel(ConnectWiseModel):
    id: int
    identifier: str
    name: str
    status: CompanyStatusReferenceModel
    address_line1: str
    address_line2: str
    city: str
    state: str
    zip: str
    country: CountryReferenceModel
    phone_number: str
    fax_number: str
    website: str
    territory: SystemLocationReferenceModel
    market: MarketDescriptionReferenceModel
    account_number: str
    default_contact: ContactReferenceModel
    date_acquired: str
    sic_code: SicCodeReferenceModel
    parent_company: CompanyReferenceModel
    annual_revenue: float
    number_of_employees: int
    year_established: int
    revenue_year: int
    ownership_type: OwnershipTypeReferenceModel
    time_zone_setup: TimeZoneSetupReferenceModel
    lead_source: str
    lead_flag: bool
    unsubscribe_flag: bool
    calendar: CalendarReferenceModel
    user_defined_field1: str
    user_defined_field2: str
    user_defined_field3: str
    user_defined_field4: str
    user_defined_field5: str
    user_defined_field6: str
    user_defined_field7: str
    user_defined_field8: str
    user_defined_field9: str
    user_defined_field10: str
    vendor_identifier: str
    tax_identifier: str
    tax_code: TaxCodeReferenceModel
    billing_terms: BillingTermsReferenceModel
    invoice_template: InvoiceTemplateReferenceModel
    pricing_schedule: PricingScheduleReferenceModel
    company_entity_type: EntityTypeReferenceModel
    bill_to_company: CompanyReferenceModel
    billing_site: SiteReferenceModel
    billing_contact: ContactReferenceModel
    invoice_delivery_method: BillingDeliveryReferenceModel
    invoice_to_email_address: str
    invoice_c_c_email_address: str
    deleted_flag: bool
    date_deleted: str
    deleted_by: str
    mobile_guid: str
    facebook_url: str
    twitter_url: str
    linked_in_url: str
    currency: CurrencyReferenceModel
    territory_manager: MemberReferenceModel
    reseller_identifier: str
    is_vendor_flag: bool
    types: list[CompanyTypeReferenceModel]
    site: SiteReferenceModel
    integrator_tags: list[str]
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True