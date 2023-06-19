from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pyconnectwise.models.manage.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pyconnectwise.models.manage.ServiceItemReferenceModel import ServiceItemReferenceModel
from pyconnectwise.models.manage.ServiceTemplateReferenceModel import ServiceTemplateReferenceModel
from pyconnectwise.models.manage.BoardReferenceModel import BoardReferenceModel
from enum import Enum
class SummarySetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class DiscussionSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class InternalAnalysisSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class ResolutionSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class TasksSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class DocumentsSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class ResourcesSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class BudgetHoursSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class FinanceInformationSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'
class SendNotesAsEmailSetting(str, Enum):
    Append = 'Append'
    Overwrite = 'Overwrite'
    Ignore = 'Ignore'

class BoardAutoTemplateModel(ConnectWiseModel):
    id: int
    type: ServiceTypeReferenceModel
    subtype: ServiceSubTypeReferenceModel
    item: ServiceItemReferenceModel
    service_template: ServiceTemplateReferenceModel
    board: BoardReferenceModel
    summary_setting: SummarySetting
    discussion_setting: DiscussionSetting
    internal_analysis_setting: InternalAnalysisSetting
    resolution_setting: ResolutionSetting
    tasks_setting: TasksSetting
    documents_setting: DocumentsSetting
    resources_setting: ResourcesSetting
    budget_hours_setting: BudgetHoursSetting
    finance_information_setting: FinanceInformationSetting
    send_notes_as_email_setting: SendNotesAsEmailSetting
    auto_apply_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True