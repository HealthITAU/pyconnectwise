from typing import Any

from pyconnectwise.endpoints.automate.UsersFoldersEndpoint import UsersFoldersEndpoint
from pyconnectwise.endpoints.automate.UsersIdEndpoint import UsersIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import AutomateUser
from pyconnectwise.responses.paginated_response import PaginatedResponse


class UsersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Users", parent_endpoint=parent_endpoint)

        self.folders = self._register_child_endpoint(UsersFoldersEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> UsersIdEndpoint:
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

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AutomateUser:
        """
        Performs a POST request against the /Users endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateUser: The parsed response data.
        """
        return self._parse_one(AutomateUser, super()._make_request("POST", data=data, params=params).json())
