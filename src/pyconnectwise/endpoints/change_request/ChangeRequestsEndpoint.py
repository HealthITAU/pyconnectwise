from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.change_request.ChangeRequestIdEndpoint import ChangeRequestIdEndpoint
from pyconnectwise.interfaces import IGettable, IPostable
from pyconnectwise.models.change_request import ChangeRequestMsg, ChangeRequestGetObject
from pyconnectwise.types import JSON, ConnectWiseChangeApprovalRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ChangeRequestsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ChangeRequestMsg], ConnectWiseChangeApprovalRequestParams],
    IPostable[ChangeRequestMsg, ConnectWiseChangeApprovalRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "change_request", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ChangeRequestMsg])
        IPostable.__init__(self, ChangeRequestMsg)

    def id(self, _id: int) -> ChangeRequestIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ChangeRequestIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ChangeRequestIdEndpoint: The initialized ChangeRequestIdEndpoint object.
        """
        child = ChangeRequestIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def get(
        self, data: JSON | None = None, params: ConnectWiseChangeApprovalRequestParams | None = None
    ) -> list[ChangeRequestMsg]:
        """
        Performs a GET request against the /api/change_requests endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ChangeRequestMsg]: The parsed response data.
        """
        obj = self._parse_one(ChangeRequestGetObject, super()._make_request("GET", data=data, params=params).json())
        return obj.msg.data

    def post(
        self, data: JSON | None = None, params: ConnectWiseChangeApprovalRequestParams | None = None
    ) -> ChangeRequestMsg:
        """
        Performs a POST request against the /api/change_requests endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ChangeRequestMsg: The parsed response data.
        """
        return self._parse_one(ChangeRequestMsg, super()._make_request("POST", data=data, params=params).json())
