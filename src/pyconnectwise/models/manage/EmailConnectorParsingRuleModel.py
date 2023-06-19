from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.EmailConnectorParsingStyleReferenceModel import EmailConnectorParsingStyleReferenceModel
from pyconnectwise.models.manage.EmailConnectorParsingVariableReferenceModel import EmailConnectorParsingVariableReferenceModel
from pyconnectwise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pyconnectwise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pyconnectwise.models.manage.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pyconnectwise.models.manage.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pyconnectwise.models.manage.ServiceItemReferenceModel import ServiceItemReferenceModel
from pyconnectwise.models.manage.BoardReferenceModel import BoardReferenceModel

class EmailConnectorParsingRuleModel(ConnectWiseModel):
    id: int
    parsing_style: EmailConnectorParsingStyleReferenceModel
    priority: int
    parsing_variable: EmailConnectorParsingVariableReferenceModel
    search_term: str
    service_priority: PriorityReferenceModel
    service_status: ServiceStatusReferenceModel
    service_type: ServiceTypeReferenceModel
    service_sub_type: ServiceSubTypeReferenceModel
    service_item: ServiceItemReferenceModel
    service_board: BoardReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True