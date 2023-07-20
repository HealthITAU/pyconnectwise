from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.KPIReferenceModel import KPIReferenceModel
from pyconnectwise.models.manage.ReportCardReferenceModel import ReportCardReferenceModel

class ReportCardDetailModel(ConnectWiseModel):
    id: int
    kpi: KPIReferenceModel
    sort_order: int
    report_card: ReportCardReferenceModel
    _info: dict[str, str]