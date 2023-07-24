
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class DatesScheduleSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    monthly_occurrence: (list[str] | None) = Field(default=None, alias='MonthlyOccurrence')
    dates: (list[int] | None) = Field(default=None, alias='Dates')
    last_day_of_month: (bool | None) = Field(default=None, alias='LastDayOfMonth')

class DaysScheduleSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    monthly_occurrence: (list[str] | None) = Field(default=None, alias='MonthlyOccurrence')
    weekly_occurrence: (list[str] | None) = Field(default=None, alias='WeeklyOccurrence')
    daily_occurrence: (list[str] | None) = Field(default=None, alias='DailyOccurrence')

class PatchTuesdayScheduleSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    delay_in_days: (int | None) = Field(default=None, alias='DelayInDays')

class PatchingPolicySchedule(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    use_schedule: (bool | None) = Field(default=None, alias='UseSchedule')
    window_start: (str | None) = Field(default=None, alias='WindowStart')
    window_duration: (str | None) = Field(default=None, alias='WindowDuration')
    policy_schedule_type: (str | None) = Field(default=None, alias='PolicyScheduleType')
    dates_settings: (DatesScheduleSettings | None) = Field(default=None, alias='DatesSettings')
    days_settings: (DaysScheduleSettings | None) = Field(default=None, alias='DaysSettings')
    patch_tuesday_settings: (PatchTuesdayScheduleSettings | None) = Field(default=None, alias='PatchTuesdaySettings')
