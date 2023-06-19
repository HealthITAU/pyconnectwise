from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from enum import Enum
class ProblemSort(str, Enum):
    Ascending = 'Ascending'
    Descending = 'Descending'
class InternalAnalysisSort(str, Enum):
    Ascending = 'Ascending'
    Descending = 'Descending'
class ResolutionSort(str, Enum):
    Ascending = 'Ascending'
    Descending = 'Descending'
class AllSort(str, Enum):
    Ascending = 'Ascending'
    Descending = 'Descending'

class BoardInfoModel(ConnectWiseModel):
    id: int
    name: str
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    project_flag: bool
    inactive_flag: bool
    closed_loop_discussions_flag: bool
    closed_loop_internal_analysis_flag: bool
    closed_loop_resolution_flag: bool
    closed_loop_all_flag: bool
    problem_sort: ProblemSort
    internal_analysis_sort: InternalAnalysisSort
    resolution_sort: ResolutionSort
    all_sort: AllSort
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True