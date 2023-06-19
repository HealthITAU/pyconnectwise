from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class FrequencyUnit(str, Enum):
    Minutes = 'Minutes'
    Hours = 'Hours'
    Days = 'Days'
    Months = 'Months'
class ExecutionTime(str, Enum):
    Once = 'Once'
    MultipleTimes = 'MultipleTimes'
    Continuously = 'Continuously'

class WorkflowEventModel(ConnectWiseModel):
    id: int
    name: str
    event_condition: str
    frequency_unit: FrequencyUnit
    frequency_of_execution: int
    max_number_of_execution: int
    execution_time: ExecutionTime
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True