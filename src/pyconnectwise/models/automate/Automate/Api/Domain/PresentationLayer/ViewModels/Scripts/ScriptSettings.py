
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class UserClass(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_class_id: (int | None) = Field(default=None, alias='UserClassId')
    name: (str | None) = Field(default=None, alias='Name')

class TicketEntryCategory(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ticket_category_id: (int | None) = Field(default=None, alias='TicketCategoryId')
    name: (str | None) = Field(default=None, alias='Name')

class CloseTicketTrigger(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    close_ticket_trigger_type_id: (int | None) = Field(default=None, alias='CloseTicketTriggerTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class TimeEntryTechnician(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: (int | None) = Field(default=None, alias='UserId')
    name: (str | None) = Field(default=None, alias='Name')

class StopTimerTrigger(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    stop_timer_trigger_type_id: (int | None) = Field(default=None, alias='StopTimerTriggerTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class TimeEntryCategory(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    time_category_id: (int | None) = Field(default=None, alias='TimeCategoryId')
    name: (str | None) = Field(default=None, alias='Name')

class ScriptSettingsViewModel(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_classes: (list[UserClass] | None) = Field(default=None, alias='UserClasses')
    ticket_categories: (list[TicketEntryCategory] | None) = Field(default=None, alias='TicketCategories')
    close_ticket_triggers: (list[CloseTicketTrigger] | None) = Field(default=None, alias='CloseTicketTriggers')
    users: (list[TimeEntryTechnician] | None) = Field(default=None, alias='Users')
    stop_timer_triggers: (list[StopTimerTrigger] | None) = Field(default=None, alias='StopTimerTriggers')
    ticket_time_categories: (list[TimeEntryCategory] | None) = Field(default=None, alias='TicketTimeCategories')
