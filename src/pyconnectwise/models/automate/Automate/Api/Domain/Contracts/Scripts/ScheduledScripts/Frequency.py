
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class ScriptScheduleFrequency(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_schedule_frequency_id: (int | None) = Field(default=None, alias='ScriptScheduleFrequencyId')
    name: (str | None) = Field(default=None, alias='Name')

class MinutelyScheduleFrequency(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    minutely_interval: (int | None) = Field(default=None, alias='MinutelyInterval')
    exclusion_start_time: (str | None) = Field(default=None, alias='ExclusionStartTime')
    exclusion_end_time: (str | None) = Field(default=None, alias='ExclusionEndTime')

class HourlyScheduleFrequency(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    hourly_interval: (int | None) = Field(default=None, alias='HourlyInterval')
    exclusion_start_time: (str | None) = Field(default=None, alias='ExclusionStartTime')
    exclusion_end_time: (str | None) = Field(default=None, alias='ExclusionEndTime')

class MonthlyScheduleFrequency(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    runs_at: (str | None) = Field(default=None, alias='RunsAt')
    monthly_interval: (int | None) = Field(default=None, alias='MonthlyInterval')
    day: (int | None) = Field(default=None, alias='Day')

class DaysOfWeekSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    sunday: (bool | None) = Field(default=None, alias='Sunday')
    monday: (bool | None) = Field(default=None, alias='Monday')
    tuesday: (bool | None) = Field(default=None, alias='Tuesday')
    wednesday: (bool | None) = Field(default=None, alias='Wednesday')
    thursday: (bool | None) = Field(default=None, alias='Thursday')
    friday: (bool | None) = Field(default=None, alias='Friday')
    saturday: (bool | None) = Field(default=None, alias='Saturday')

class WeeksOfMonthSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    first: (bool | None) = Field(default=None, alias='First')
    second: (bool | None) = Field(default=None, alias='Second')
    third: (bool | None) = Field(default=None, alias='Third')
    fourth: (bool | None) = Field(default=None, alias='Fourth')
    last: (bool | None) = Field(default=None, alias='Last')

class DailyScriptRepeatFrequency(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    daily_script_repeat_frequency_id: (int | None) = Field(default=None, alias='DailyScriptRepeatFrequencyId')
    name: (str | None) = Field(default=None, alias='Name')

class WeeklyScheduleFrequency(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    runs_at: (str | None) = Field(default=None, alias='RunsAt')
    weeks_of_month_settings: (WeeksOfMonthSettings | None) = Field(default=None, alias='WeeksOfMonthSettings')
    days_of_week_settings: (DaysOfWeekSettings | None) = Field(default=None, alias='DaysOfWeekSettings')

class DailyRepeatSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    daily_script_repeat_frequency: (DailyScriptRepeatFrequency | None) = Field(default=None, alias='DailyScriptRepeatFrequency')
    daily_repeat_interval: (int | None) = Field(default=None, alias='DailyRepeatInterval')
    maximum_repetitions: (int | None) = Field(default=None, alias='MaximumRepetitions')

class DailyScheduleFrequency(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    runs_at: (str | None) = Field(default=None, alias='RunsAt')
    daily_interval: (int | None) = Field(default=None, alias='DailyInterval')
    days_of_week_settings: (DaysOfWeekSettings | None) = Field(default=None, alias='DaysOfWeekSettings')
    daily_repeat_settings: (DailyRepeatSettings | None) = Field(default=None, alias='DailyRepeatSettings')
