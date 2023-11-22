from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdForecastCopyIdEndpoint import (
    SalesOpportunitiesIdForecastCopyIdEndpoint,
)

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SalesOpportunitiesIdForecastCopyEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "copy", parent_endpoint=parent_endpoint)

    def id(self, _id: int) -> SalesOpportunitiesIdForecastCopyIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesIdForecastCopyIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SalesOpportunitiesIdForecastCopyIdEndpoint: The initialized SalesOpportunitiesIdForecastCopyIdEndpoint object.
        """
        child = SalesOpportunitiesIdForecastCopyIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
