from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from pyconnectwise.utils.naming import to_camel_case
from typing import Optional, Type, Any, TypeVar

Model = TypeVar('Model', bound='BaseModel')

class ConnectWiseModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel_case, populate_by_name=True, use_enum_values=True, protected_namespaces=())

    @classmethod
    def model_construct(cls: Type['ConnectWiseModel'], **values: Any) -> 'ConnectWiseModel':
        """
        Overriding Pydantics construct method to allow for nested models.
        """
        m = cls.__new__(cls)
        fields_values: dict[str, Any] = {}
        defaults: dict[str, Any] = {}

        def handle_nested_model(field, value):
            if issubclass(type(field.annotation), BaseModel):
                if isinstance(value, list):
                    return [field.annotation.model_construct(**v) for v in value]
                else:
                    return field.annotation.model_construct(**value)
            else:
                return value

        for name, field in cls.model_fields.items():
            if field.alias and field.alias in values:
                fields_values[name] = handle_nested_model(field, values[field.alias])
            elif name in values:
                fields_values[name] = handle_nested_model(field, values[name])
            elif not field.is_required():
                defaults[name] = field.get_default(call_default_factory=True)
        fields_values.update(defaults)

        _extra: dict[str, Any] | None = None
        if cls.model_config.get('extra') == 'allow':
            _extra = {}
            for k, v in values.items():
                _extra[k] = v
        else:
            fields_values.update(values)
        object.__setattr__(m, '__dict__', fields_values)
        object.__setattr__(m, '__pydantic_fields_set__', fields_values.keys())
        if not cls.__pydantic_root_model__:
            object.__setattr__(m, '__pydantic_extra__', _extra)

        if cls.__pydantic_post_init__:
            m.model_post_init(None)
        elif not cls.__pydantic_root_model__:
            # Note: if there are any private attributes, cls.__pydantic_post_init__ would exist
            # Since it doesn't, that means that `__pydantic_private__` should be set to None
            object.__setattr__(m, '__pydantic_private__', None)

        return m
