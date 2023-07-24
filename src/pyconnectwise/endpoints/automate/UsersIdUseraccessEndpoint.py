from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate.Automate.Api.Domain.Contracts.Users import UserAccess
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class UsersIdUseraccessEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Useraccess", parent_endpoint=parent_endpoint)

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> UserAccess:
        """
        Performs a GET request against the /Users/{id}/Useraccess endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            UserAccess: The parsed response data.
        """
        return self._parse_one(
            UserAccess, super()._make_request("GET", data=data, params=params).json()
        )
