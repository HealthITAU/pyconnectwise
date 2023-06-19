from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class MarketplaceImportType(str, Enum):
    Agreements = 'Agreements'
    Configurations = 'Configurations'
    CRMSurveys = 'CRMSurveys'
    CustomReports = 'CustomReports'
    CustomerPortalTypes = 'CustomerPortalTypes'
    HTMLEmailTemplates = 'HTMLEmailTemplates'
    Products = 'Products'
    ProjectBoards = 'ProjectBoards'
    ProjectTemplates = 'ProjectTemplates'
    ReportWriterReports = 'ReportWriterReports'
    ServiceBoards = 'ServiceBoards'
    TicketTemplates = 'TicketTemplates'
    Views = 'Views'

class MarketplaceImportModel(ConnectWiseModel):
    id: int
    marketplace_import_type: MarketplaceImportType
    marketplace_object: list[Any]
    required_fields: list[str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True