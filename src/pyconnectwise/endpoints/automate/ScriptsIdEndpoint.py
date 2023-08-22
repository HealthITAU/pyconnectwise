from typing import Any

from pyconnectwise.endpoints.automate.ScriptsIdCopyEndpoint import ScriptsIdCopyEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import AutomateScript
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScriptsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.copy = self._register_child_endpoint(ScriptsIdCopyEndpoint(client, parent_endpoint=self))

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AutomateScript:
        """
        Performs a GET request against the /Scripts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateScript: The parsed response data.
        """
        return self._parse_one(AutomateScript, super()._make_request("GET", data=data, params=params).json())

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AutomateScript:
        """
        Performs a PUT request against the /Scripts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateScript: The parsed response data.
        """
        return self._parse_one(AutomateScript, super()._make_request("PUT", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /Scripts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)
