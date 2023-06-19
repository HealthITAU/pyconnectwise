from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.ServiceSurveyReferenceModel import ServiceSurveyReferenceModel
from pyconnectwise.models.manage.BoardReferenceModel import BoardReferenceModel
from pyconnectwise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
class ServiceEmailTemplateModelType(str, Enum):
    Any = 'Any'
    Closed = 'Closed'
    Invoice = 'Invoice'
    New = 'New'
    SalesOrder = 'SalesOrder'
    PurchaseOrder = 'PurchaseOrder'
    RMA = 'RMA'
    Specific = 'Specific'

class ServiceEmailTemplateModel(ConnectWiseModel):
    id: int
    type: ServiceEmailTemplateModelType
    service_survey: ServiceSurveyReferenceModel
    service_board: BoardReferenceModel
    use_sender_flag: bool
    first_name: str
    last_name: str
    email_address: str
    subject: str
    body: str
    copy_sender_flag: bool
    tasks_flag: bool
    resource_records_flag: bool
    external_contact_notifications: bool
    internal_contact_notifications: bool
    service_status: ServiceStatusReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True