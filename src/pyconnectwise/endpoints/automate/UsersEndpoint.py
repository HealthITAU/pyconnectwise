from pyconnectwise.endpoints.automate.UsersFoldersEndpoint import UsersFoldersEndpoint
from pyconnectwise.endpoints.automate.UsersIdEndpoint import UsersIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.automate import AutomateUser
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class UsersEndpoint(ConnectWiseEndpoint, IPostable[AutomateUser, ConnectWiseAutomateRequestParams]):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "Users", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, AutomateUser)

        self.folders = self._register_child_endpoint(UsersFoldersEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> UsersIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized UsersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            UsersIdEndpoint: The initialized UsersIdEndpoint object.
        """
        child = UsersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> AutomateUser:
        """
        Performs a POST request against the /Users endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateUser: The parsed response data.
        """
        return self._parse_one(AutomateUser, super()._make_request("POST", data=data, params=params).json())
