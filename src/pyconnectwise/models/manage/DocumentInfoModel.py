from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class DocumentInfoModel(ConnectWiseModel):
    id: int
    title: str
    file_name: str
    server_file_name: str
    owner: str
    link_flag: bool
    image_flag: bool
    public_flag: bool
    html_template_flag: bool
    read_only_flag: bool
    size: int
    url_flag: bool
    guid: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True