from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class FileUploadSettingModel(ConnectWiseModel):
    id: int
    restrict_file_types_flag: bool
    global_file_size_limit: int
    _info: dict[str, str]