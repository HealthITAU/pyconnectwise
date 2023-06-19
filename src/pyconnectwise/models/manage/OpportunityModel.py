from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.OpportunityTypeReferenceModel import OpportunityTypeReferenceModel
from pyconnectwise.models.manage.OpportunityStageReferenceModel import OpportunityStageReferenceModel
from pyconnectwise.models.manage.OpportunityStatusReferenceModel import OpportunityStatusReferenceModel
from pyconnectwise.models.manage.OpportunityPriorityReferenceModel import OpportunityPriorityReferenceModel
from pyconnectwise.models.manage.OpportunityProbabilityReferenceModel import OpportunityProbabilityReferenceModel
from pyconnectwise.models.manage.OpportunityRatingReferenceModel import OpportunityRatingReferenceModel
from pyconnectwise.models.manage.CampaignReferenceModel import CampaignReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pyconnectwise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel

class OpportunityModel(ConnectWiseModel):
    id: int
    name: str
    expected_close_date: str
    type: OpportunityTypeReferenceModel
    stage: OpportunityStageReferenceModel
    status: OpportunityStatusReferenceModel
    priority: OpportunityPriorityReferenceModel
    notes: str
    probability: OpportunityProbabilityReferenceModel
    source: str
    rating: OpportunityRatingReferenceModel
    campaign: CampaignReferenceModel
    primary_sales_rep: MemberReferenceModel
    secondary_sales_rep: MemberReferenceModel
    location_id: int
    business_unit_id: int
    company: CompanyReferenceModel
    contact: ContactReferenceModel
    site: SiteReferenceModel
    customer_p_o: str
    pipeline_change_date: str
    date_became_lead: str
    closed_date: str
    closed_by: MemberReferenceModel
    total_sales_tax: float
    ship_to_company: CompanyReferenceModel
    ship_to_contact: ContactReferenceModel
    ship_to_site: SiteReferenceModel
    bill_to_company: CompanyReferenceModel
    bill_to_contact: ContactReferenceModel
    bill_to_site: SiteReferenceModel
    billing_terms: BillingTermsReferenceModel
    tax_code: TaxCodeReferenceModel
    currency: CurrencyReferenceModel
    company_location_id: int
    technical_contact: ContactReferenceModel
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True