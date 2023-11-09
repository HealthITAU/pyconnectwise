from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesScheduleHolidaylistsIdEndpoint import SalesScheduleHolidaylistsIdEndpoint
from pyconnectwise.endpoints.manage.SalesScheduleHolidaylistsInfoEndpoint import SalesScheduleHolidaylistsInfoEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SalesScheduleHolidaylistsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "holidaylists", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(SalesScheduleHolidaylistsInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> SalesScheduleHolidaylistsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesScheduleHolidaylistsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SalesScheduleHolidaylistsIdEndpoint: The initialized SalesScheduleHolidaylistsIdEndpoint object.
        """
        child = SalesScheduleHolidaylistsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
