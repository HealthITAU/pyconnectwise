from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleHolidaylistsIdEndpoint import ScheduleHolidaylistsIdEndpoint
from pyconnectwise.endpoints.manage.ScheduleHolidaylistsInfoEndpoint import ScheduleHolidaylistsInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ScheduleHolidaylistsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "holidaylists", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(ScheduleHolidaylistsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ScheduleHolidaylistsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScheduleHolidaylistsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScheduleHolidaylistsIdEndpoint: The initialized ScheduleHolidaylistsIdEndpoint object.
        """
        child = ScheduleHolidaylistsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
