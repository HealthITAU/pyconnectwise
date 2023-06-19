from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ServiceItemReferenceModel import ServiceItemReferenceModel
from pyconnectwise.models.manage.BoardReferenceModel import BoardReferenceModel

class BoardItemAssociationModel(ConnectWiseModel):
    id: int
    sub_type_association_ids: list[int]
    add_all_sub_types_flag: bool
    remove_all_sub_types_flag: bool
    item: ServiceItemReferenceModel
    board: BoardReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True