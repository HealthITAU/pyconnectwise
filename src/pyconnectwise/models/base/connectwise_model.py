from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from pyconnectwise.utils.naming import to_camel_case
from typing import Type, Any, TypeVar, get_type_hints
from typing import ForwardRef

Model = TypeVar("Model", bound="BaseModel")


class ConnectWiseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel_case,
        populate_by_name=True,
        use_enum_values=True,
        protected_namespaces=(),
    )
