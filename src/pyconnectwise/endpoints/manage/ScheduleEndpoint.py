from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleCalendarsEndpoint import ScheduleCalendarsEndpoint
from pyconnectwise.endpoints.manage.ScheduleColorsEndpoint import ScheduleColorsEndpoint
from pyconnectwise.endpoints.manage.ScheduleDetailsEndpoint import ScheduleDetailsEndpoint
from pyconnectwise.endpoints.manage.ScheduleEntriesEndpoint import ScheduleEntriesEndpoint
from pyconnectwise.endpoints.manage.ScheduleHolidayListsEndpoint import ScheduleHolidayListsEndpoint
from pyconnectwise.endpoints.manage.SchedulePortalcalendarsEndpoint import SchedulePortalcalendarsEndpoint
from pyconnectwise.endpoints.manage.ScheduleReminderTimesEndpoint import ScheduleReminderTimesEndpoint
from pyconnectwise.endpoints.manage.ScheduleStatusesEndpoint import ScheduleStatusesEndpoint
from pyconnectwise.endpoints.manage.ScheduleTypesEndpoint import ScheduleTypesEndpoint

class ScheduleEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "schedule")
        
        self.calendars = self.register_child_endpoint(
            ScheduleCalendarsEndpoint(client, parent_endpoint=self)
        )
        self.colors = self.register_child_endpoint(
            ScheduleColorsEndpoint(client, parent_endpoint=self)
        )
        self.details = self.register_child_endpoint(
            ScheduleDetailsEndpoint(client, parent_endpoint=self)
        )
        self.entries = self.register_child_endpoint(
            ScheduleEntriesEndpoint(client, parent_endpoint=self)
        )
        self.holidayLists = self.register_child_endpoint(
            ScheduleHolidayListsEndpoint(client, parent_endpoint=self)
        )
        self.portalcalendars = self.register_child_endpoint(
            SchedulePortalcalendarsEndpoint(client, parent_endpoint=self)
        )
        self.reminderTimes = self.register_child_endpoint(
            ScheduleReminderTimesEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            ScheduleStatusesEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            ScheduleTypesEndpoint(client, parent_endpoint=self)
        )