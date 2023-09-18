from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleCalendarsEndpoint import ScheduleCalendarsEndpoint
from pyconnectwise.endpoints.manage.ScheduleColorsEndpoint import ScheduleColorsEndpoint
from pyconnectwise.endpoints.manage.ScheduleDetailsEndpoint import ScheduleDetailsEndpoint
from pyconnectwise.endpoints.manage.ScheduleEntriesEndpoint import ScheduleEntriesEndpoint
from pyconnectwise.endpoints.manage.ScheduleHolidaylistsEndpoint import ScheduleHolidaylistsEndpoint
from pyconnectwise.endpoints.manage.SchedulePortalcalendarsEndpoint import SchedulePortalcalendarsEndpoint
from pyconnectwise.endpoints.manage.ScheduleRemindertimesEndpoint import ScheduleRemindertimesEndpoint
from pyconnectwise.endpoints.manage.ScheduleStatusesEndpoint import ScheduleStatusesEndpoint
from pyconnectwise.endpoints.manage.ScheduleTypesEndpoint import ScheduleTypesEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScheduleEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "schedule", parent_endpoint=parent_endpoint)

        self.colors = self._register_child_endpoint(ScheduleColorsEndpoint(client, parent_endpoint=self))
        self.calendars = self._register_child_endpoint(ScheduleCalendarsEndpoint(client, parent_endpoint=self))
        self.holidaylists = self._register_child_endpoint(ScheduleHolidaylistsEndpoint(client, parent_endpoint=self))
        self.holiday_lists = self._register_child_endpoint(ScheduleHolidaylistsEndpoint(client, parent_endpoint=self))
        self.details = self._register_child_endpoint(ScheduleDetailsEndpoint(client, parent_endpoint=self))
        self.entries = self._register_child_endpoint(ScheduleEntriesEndpoint(client, parent_endpoint=self))
        self.types = self._register_child_endpoint(ScheduleTypesEndpoint(client, parent_endpoint=self))
        self.reminder_times = self._register_child_endpoint(ScheduleRemindertimesEndpoint(client, parent_endpoint=self))
        self.statuses = self._register_child_endpoint(ScheduleStatusesEndpoint(client, parent_endpoint=self))
        self.portalcalendars = self._register_child_endpoint(
            SchedulePortalcalendarsEndpoint(client, parent_endpoint=self)
        )
