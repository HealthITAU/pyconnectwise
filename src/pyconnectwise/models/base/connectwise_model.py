from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from pyconnectwise.utils.naming import to_camel_case

class ConnectWiseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel_case,
        populate_by_name=True,
        use_enum_values=True,
        protected_namespaces=(),
    )
