from typing import Any

from pyconnectwise.endpoints.automate.UsersFoldersIdEndpoint import UsersFoldersIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate.Automate.Api.Domain.Contracts.Users import UserFolder
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class UsersFoldersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Folders", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> UsersFoldersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized UsersFoldersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            UsersFoldersIdEndpoint: The initialized UsersFoldersIdEndpoint object.
        """
        child = UsersFoldersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> UserFolder:
        """
        Performs a POST request against the /Users/Folders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            UserFolder: The parsed response data.
        """
        return self._parse_one(UserFolder, super()._make_request("POST", data=data, params=params).json())
