
from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Any
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class DeleteSearchesBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    search_ids: (list[int] | None) = Field(default=None, alias='SearchIds')

class DeleteSearchesBatchResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    search_id: (int | None) = Field(default=None, alias='SearchId')
    search_name: (str | None) = Field(default=None, alias='SearchName')
    result_details: (ResponseResult | None) = Field(default=None, alias='ResultDetails')

class SendToSearchesBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    search_ids: (list[int] | None) = Field(default=None, alias='SearchIds')
    folder_id: (int | None) = Field(default=None, alias='FolderId')

class SendToBatchResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    search_id: (int | None) = Field(default=None, alias='SearchId')
    result_details: (ResponseResult | None) = Field(default=None, alias='ResultDetails')

class SearchTargetType(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    search_target_type_id: (int | None) = Field(default=None, alias='SearchTargetTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class NodeType(Enum):
    AND_NODE = 'AndNode'
    OR_NODE = 'OrNode'
    COMPARISON_NODE = 'ComparisonNode'
    ANY_MEETS_NODE = 'AnyMeetsNode'
    NOT_NODE = 'NotNode'

class Operator(Enum):
    IS_TRUE = 'IsTrue'
    IS_FALSE = 'IsFalse'
    EQUALS = 'Equals'
    GREATER_THAN = 'GreaterThan'
    GREATER_THAN_EQUAL = 'GreaterThanEqual'
    LESS_THAN = 'LessThan'
    LESS_THAN_EQUAL = 'LessThanEqual'
    TEXT_LIKE = 'TextLike'
    NOT_EQUAL = 'NotEqual'
    NOT_TEXT_LIKE = 'NotTextLike'
    CONTAINS = 'Contains'
    NOT_CONTAINS = 'NotContains'
    IS_ASSIGNED = 'IsAssigned'
    IS_NOT_ASSIGNED = 'IsNotAssigned'
    HAS_ROLE = 'HasRole'
    NOT_HAS_ROLE = 'NotHasRole'

class FilterCriteria(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    left_operand: (str | None) = Field(default=None, alias='LeftOperand')
    operator: (Operator | None) = Field(default=None, alias='Operator')
    right_operand: (dict[(str, Any)] | None) = Field(default=None, alias='RightOperand')

class SearchesBatchResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    searches_results: (list[DeleteSearchesBatchResult] | None) = Field(default=None, alias='SearchesResults')
    contains_unsuccessful_results: (bool | None) = Field(default=None, alias='ContainsUnsuccessfulResults')

class SendToSearchesBatchResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    search_results: (list[SendToBatchResult] | None) = Field(default=None, alias='SearchResults')
    contains_unsuccessful_results: (bool | None) = Field(default=None, alias='ContainsUnsuccessfulResults')

class Search(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    search_id: (int | None) = Field(default=None, alias='SearchId')
    name: (str | None) = Field(default=None, alias='Name')
    search_target_type: (SearchTargetType | None) = Field(default=None, alias='SearchTargetType')
    search_folder: (Models.SearchFolder | None) = Field(default=None, alias='SearchFolder')
    update_date: (datetime | None) = Field(default=None, alias='UpdateDate')
    updated_by: (str | None) = Field(default=None, alias='UpdatedBy')
    is_read_only: (bool | None) = Field(default=None, alias='IsReadOnly')

class AdvancedSearchFilter(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    node_type: (NodeType | None) = Field(default=None, alias='NodeType')
    node_name: (str | None) = Field(default=None, alias='NodeName')
    filter_criterias: (list[FilterCriteria] | None) = Field(default=None, alias='FilterCriterias')
    child_nodes: (list[AdvancedSearchFilter] | None) = Field(default=None, alias='ChildNodes')
from . import ResponseResult
from .....LabTech import Models
