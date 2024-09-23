from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IGettable, IPostable
from pyconnectwise.models.change_request import ChangeRequestMsg, ChangeRequestObject, LoginObject, LoginMsg
from pyconnectwise.types import JSON, ConnectWiseChangeApprovalRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class LoginEndpoint(
    ConnectWiseEndpoint,
    IPostable[LoginMsg, ConnectWiseChangeApprovalRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "login", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, LoginMsg)

    def post(self, data: JSON | None = None, params: ConnectWiseChangeApprovalRequestParams | None = None) -> LoginMsg:
        """
        Performs a GET request against the /api/change_requests endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ChangeRequestMsg]: The parsed response data.
        """
        obj = self._parse_one(LoginObject, super()._make_request("POST", data=data, params=params).json())
        return obj.msg
