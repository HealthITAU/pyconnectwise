from __future__ import annotations
from pydantic import BaseModel
from pyconnectwise.utils.naming import to_camel_case
from typing import Optional, Type, Any, TypeVar

Model = TypeVar('Model', bound='BaseModel')

class ConnectWiseModel(BaseModel):

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True

    @classmethod
    def construct(cls: Type['ConnectWiseModel'], **values: Any) -> 'ConnectWiseModel':
        """
        Overriding Pydantics construct method to allow for nested models.
        """
        m = cls.__new__(cls)
        fields_values: dict[str, Any] = {}

        def handle_nested_model(field, value):
            if issubclass(field.type_, BaseModel):
                if isinstance(value, list):
                    return [field.type_.construct(**v) for v in value]
                else:
                    return field.type_.construct(**value)
            else:
                return value

        for name, field in cls.__fields__.items():
            if field.alt_alias and field.alias in values:
                fields_values[name] = handle_nested_model(field, values[field.alias])
            elif name in values:
                fields_values[name] = handle_nested_model(field, values[name])
            elif not field.required:
                fields_values[name] = field.get_default()
            else:
                value = values.get(name)
                if value is None:
                    fields_values[name] = None
                    continue
                fields_values[name] = handle_nested_model(field, value)

        object.__setattr__(m, '__dict__', fields_values)
        object.__setattr__(m, '__fields_set__', set(values.keys()))
        m._init_private_attributes()
        return m
