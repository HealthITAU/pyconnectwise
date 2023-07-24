
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class UserClassAccess(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_class_id: (int | None) = Field(default=None, alias='UserClassId')
    name: (str | None) = Field(default=None, alias='Name')
    can_execute: (bool | None) = Field(default=None, alias='CanExecute')
    can_edit: (bool | None) = Field(default=None, alias='CanEdit')

class TicketEntryCategory(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ticket_category_id: (int | None) = Field(default=None, alias='TicketCategoryId')
    name: (str | None) = Field(default=None, alias='Name')
    is_overridden: (bool | None) = Field(default=None, alias='IsOverridden')
    custom_value: (str | None) = Field(default=None, alias='CustomValue')

class CloseTicketTrigger(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    close_ticket_trigger_type_id: (int | None) = Field(default=None, alias='CloseTicketTriggerTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class TimeEntryCategory(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    time_category_id: (int | None) = Field(default=None, alias='TimeCategoryId')
    name: (str | None) = Field(default=None, alias='Name')
    is_overridden: (bool | None) = Field(default=None, alias='IsOverridden')
    custom_value: (str | None) = Field(default=None, alias='CustomValue')

class StopTimerTrigger(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    stop_timer_trigger_type_id: (int | None) = Field(default=None, alias='StopTimerTriggerTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class TimeEntryTechnician(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: (int | None) = Field(default=None, alias='UserId')
    name: (str | None) = Field(default=None, alias='Name')
    is_overridden: (bool | None) = Field(default=None, alias='IsOverridden')
    custom_value: (str | None) = Field(default=None, alias='CustomValue')

class TicketEntrySettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ticket_subject: (str | None) = Field(default=None, alias='TicketSubject')
    ticket_requestor: (str | None) = Field(default=None, alias='TicketRequestor')
    ticket_category: (TicketEntryCategory | None) = Field(default=None, alias='TicketCategory')
    close_ticket_trigger: (CloseTicketTrigger | None) = Field(default=None, alias='CloseTicketTrigger')

class TimeEntrySettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ticket_id: (str | None) = Field(default=None, alias='TicketId')
    minutes_to_log: (str | None) = Field(default=None, alias='MinutesToLog')
    time_category: (TimeEntryCategory | None) = Field(default=None, alias='TimeCategory')
    stop_timer_trigger: (StopTimerTrigger | None) = Field(default=None, alias='StopTimerTrigger')
    notes: (str | None) = Field(default=None, alias='Notes')
    technician: (TimeEntryTechnician | None) = Field(default=None, alias='Technician')
