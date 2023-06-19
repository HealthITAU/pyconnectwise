from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ManagedDevicesIntegrationReferenceModel import ManagedDevicesIntegrationReferenceModel
from pyconnectwise.models.manage.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pyconnectwise.models.manage.IvItemReferenceModel import IvItemReferenceModel
from pyconnectwise.models.manage.ConfigurationTypeReferenceModel import ConfigurationTypeReferenceModel

class ManagedDevicesIntegrationCrossReferenceModel(ConnectWiseModel):
    id: int
    managed_devices_integration: ManagedDevicesIntegrationReferenceModel
    vendor_type: str
    vendor_level: str
    agreement_type: AgreementTypeReferenceModel
    product: IvItemReferenceModel
    configuration_type: ConfigurationTypeReferenceModel
    inactive_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True