from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel

class WarehouseModel(ConnectWiseModel):
    id: int
    name: str
    company: CompanyReferenceModel
    location: SystemLocationReferenceModel
    contact: ContactReferenceModel
    department: SystemDepartmentReferenceModel
    manager: MemberReferenceModel
    site: SiteReferenceModel
    location_xref: str
    location_default_flag: bool
    overall_default_flag: bool
    inactive_flag: bool
    locked_flag: bool
    currency: CurrencyReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True