
from __future__ import annotations
from enum import Enum
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class DataType(Enum):
    TYPE_BOOLEAN = 'TypeBoolean'
    TYPE_NUMBER = 'TypeNumber'
    TYPE_TEXT = 'TypeText'
    TYPE_VERSION = 'TypeVersion'
    TYPE_DATE = 'TypeDate'
    TYPE_ASSIGNED = 'TypeAssigned'
    TYPE_EQUALITY = 'TypeEquality'
    TYPE_ROLE = 'TypeRole'

class DataLookUpType(Enum):
    NONE = 'None'
    STATIC = 'Static'
    DYNAMIC = 'Dynamic'

class SearchValueLookUp(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (str | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class AdvancedSearchDataLookup(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (str | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class SearchAttributes(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    key: (str | None) = Field(default=None, alias='Key')
    text: (str | None) = Field(default=None, alias='Text')
    description: (str | None) = Field(default=None, alias='Description')
    data_type: (DataType | None) = Field(default=None, alias='DataType')
    data_look_up_type: (DataLookUpType | None) = Field(default=None, alias='DataLookUpType')
    data_lookup: (list[SearchValueLookUp] | None) = Field(default=None, alias='DataLookup')
    collection_node: (str | None) = Field(default=None, alias='CollectionNode')

class AdvancedSearchDynamicLookup(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    search_key: (str | None) = Field(default=None, alias='SearchKey')
    advanced_search_data_lookups: (list[AdvancedSearchDataLookup] | None) = Field(default=None, alias='AdvancedSearchDataLookups')

class AdvancedSearchDetails(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    search: (Searches.Search | None) = Field(default=None, alias='Search')
    advanced_search_filter: (Searches.AdvancedSearchFilter | None) = Field(default=None, alias='AdvancedSearchFilter')

class SearchLookUpBase(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    search_node: (str | None) = Field(default=None, alias='SearchNode')
    is_leaf_node: (bool | None) = Field(default=None, alias='IsLeafNode')
    child_nodes: (list[SearchLookUpBase] | None) = Field(default=None, alias='ChildNodes')
    attributes: (SearchAttributes | None) = Field(default=None, alias='Attributes')

class AdvancedSearchLookUp(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    look_up_nodes: (list[SearchLookUpBase] | None) = Field(default=None, alias='LookUpNodes')
    collection_nodes: (list[str] | None) = Field(default=None, alias='CollectionNodes')
from ..Contracts import Searches
