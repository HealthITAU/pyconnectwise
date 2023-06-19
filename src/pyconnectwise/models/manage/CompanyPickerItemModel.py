from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.CompanyStatusReferenceModel import CompanyStatusReferenceModel
from pyconnectwise.models.manage.CompanyTypeReferenceModel import CompanyTypeReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.CountryReferenceModel import CountryReferenceModel

class CompanyPickerItemModel(ConnectWiseModel):
    id: int
    member: MemberReferenceModel
    company: CompanyReferenceModel
    company_status: CompanyStatusReferenceModel
    company_type: CompanyTypeReferenceModel
    company_site: SiteReferenceModel
    company_location: SystemLocationReferenceModel
    company_country: CountryReferenceModel
    vendor_picker_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True