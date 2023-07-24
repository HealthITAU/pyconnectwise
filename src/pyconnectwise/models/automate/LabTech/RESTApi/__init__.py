
from __future__ import annotations
from enum import Enum
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class Type(Enum):
    UNDEFINED = 'Undefined'
    ASCENDING = 'Ascending'
    DESCENDING = 'Descending'

class QueryOptionOrderBy(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: (str | None) = Field(default=None, alias='Name')
    type: (Type | None) = Field(default=None, alias='Type')

class QueryOptionExpand(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    field_name: (str | None) = Field(default=None, alias='FieldName')
    page: (int | None) = Field(default=None, alias='Page')
    page_size: (int | None) = Field(default=None, alias='PageSize')
    condition: (str | None) = Field(default=None, alias='Condition')
    expands: (dict[(str, QueryOptionExpand)] | None) = Field(default=None, alias='Expands')
    order_by: (QueryOptionOrderBy | None) = Field(default=None, alias='OrderBy')
    included_fields: (list[str] | None) = Field(default=None, alias='IncludedFields')
    excluded_fields: (list[str] | None) = Field(default=None, alias='ExcludedFields')

class QueryOptions(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    order_by: (QueryOptionOrderBy | None) = Field(default=None, alias='OrderBy')
    page: (int | None) = Field(default=None, alias='Page')
    page_size: (int | None) = Field(default=None, alias='PageSize')
    condition: (str | None) = Field(default=None, alias='Condition')
    expands: (dict[(str, QueryOptionExpand)] | None) = Field(default=None, alias='Expands')
    included_fields: (list[str] | None) = Field(default=None, alias='IncludedFields')
    excluded_fields: (list[str] | None) = Field(default=None, alias='ExcludedFields')
    ids: (list[str] | None) = Field(default=None, alias='Ids')
    timeout: (int | None) = Field(default=None, alias='Timeout')
