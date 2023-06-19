from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class ConnectWiseHostedSetupModelType(str, Enum):
    Tab = 'Tab'
    Pod = 'Pod'
    ToolbarButton = 'ToolbarButton'

class ConnectWiseHostedSetupModel(ConnectWiseModel):
    id: int
    screen_id: int
    description: str
    url: str
    type: ConnectWiseHostedSetupModelType
    client_id: str
    origin: str
    pod_height: int
    toolbar_button_dialog_height: int
    toolbar_button_dialog_width: int
    toolbar_button_text: str
    toolbar_button_tool_tip: str
    toolbar_button_icon_document_id: int
    disabled_flag: bool
    location_ids: list[int]
    locations_enabled_flag: bool
    created_by: str
    date_created: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True