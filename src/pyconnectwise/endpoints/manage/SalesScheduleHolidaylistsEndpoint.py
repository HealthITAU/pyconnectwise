from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesScheduleHolidaylistsIdEndpoint import SalesScheduleHolidaylistsIdEndpoint
from pyconnectwise.endpoints.manage.SalesScheduleHolidaylistsInfoEndpoint import SalesScheduleHolidaylistsInfoEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesScheduleHolidaylistsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "holidaylists", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(SalesScheduleHolidaylistsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesScheduleHolidaylistsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesScheduleHolidaylistsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesScheduleHolidaylistsIdEndpoint: The initialized SalesScheduleHolidaylistsIdEndpoint object.
        """
        child = SalesScheduleHolidaylistsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
