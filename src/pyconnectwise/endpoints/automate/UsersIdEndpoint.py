from typing import Any

from pyconnectwise.endpoints.automate.UsersIdAuthlinkEndpoint import UsersIdAuthlinkEndpoint
from pyconnectwise.endpoints.automate.UsersIdChangepasswordEndpoint import UsersIdChangepasswordEndpoint
from pyconnectwise.endpoints.automate.UsersIdFavoritesEndpoint import UsersIdFavoritesEndpoint
from pyconnectwise.endpoints.automate.UsersIdSettingsEndpoint import UsersIdSettingsEndpoint
from pyconnectwise.endpoints.automate.UsersIdUseraccessEndpoint import UsersIdUseraccessEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import AutomateUser
from pyconnectwise.responses.paginated_response import PaginatedResponse


class UsersIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.useraccess = self._register_child_endpoint(UsersIdUseraccessEndpoint(client, parent_endpoint=self))
        self.settings = self._register_child_endpoint(UsersIdSettingsEndpoint(client, parent_endpoint=self))
        self.authlink = self._register_child_endpoint(UsersIdAuthlinkEndpoint(client, parent_endpoint=self))
        self.favorites = self._register_child_endpoint(UsersIdFavoritesEndpoint(client, parent_endpoint=self))
        self.changepassword = self._register_child_endpoint(UsersIdChangepasswordEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[AutomateUser]:
        """
        Performs a GET request against the /Users/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AutomateUser]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), AutomateUser, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AutomateUser:
        """
        Performs a GET request against the /Users/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateUser: The parsed response data.
        """
        return self._parse_one(AutomateUser, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /Users/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AutomateUser:
        """
        Performs a PATCH request against the /Users/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateUser: The parsed response data.
        """
        return self._parse_one(AutomateUser, super()._make_request("PATCH", data=data, params=params).json())
