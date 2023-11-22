from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleHolidaylistsIdEndpoint import ScheduleHolidaylistsIdEndpoint
from pyconnectwise.endpoints.manage.ScheduleHolidaylistsInfoEndpoint import ScheduleHolidaylistsInfoEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ScheduleHolidaylistsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "holidaylists", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(ScheduleHolidaylistsInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> ScheduleHolidaylistsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScheduleHolidaylistsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ScheduleHolidaylistsIdEndpoint: The initialized ScheduleHolidaylistsIdEndpoint object.
        """
        child = ScheduleHolidaylistsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
