from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ServiceSurveyReferenceModel import ServiceSurveyReferenceModel
from pyconnectwise.models.manage.BillingStatusReferenceModel import BillingStatusReferenceModel

class InvoiceEmailTemplateModel(ConnectWiseModel):
    id: int
    name: str
    service_survey: ServiceSurveyReferenceModel
    use_sender_flag: bool
    first_name: str
    last_name: str
    email_address: str
    subject: str
    body: str
    copy_sender_flag: bool
    invoice_status: BillingStatusReferenceModel
    attach_invoice_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True