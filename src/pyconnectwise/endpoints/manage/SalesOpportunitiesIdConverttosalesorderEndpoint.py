from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IPostable
from pyconnectwise.models.manage import Order
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SalesOpportunitiesIdConverttosalesorderEndpoint(
    ConnectWiseEndpoint, IPostable[Order, ConnectWiseManageRequestParams]
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "convertToSalesOrder", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, Order)

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Order:
        """
        Performs a POST request against the /sales/opportunities/{id}/convertToSalesOrder endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Order: The parsed response data.
        """
        return self._parse_one(Order, super()._make_request("POST", data=data, params=params).json())
