from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CertificationReferenceModel import CertificationReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel

class MemberCertificationModel(ConnectWiseModel):
    id: int
    certification: CertificationReferenceModel
    percent_complete: int
    date_received: str
    date_expires: str
    certification_number: str
    notes: str
    member: MemberReferenceModel
    company: CompanyReferenceModel
    _info: dict[str, str]