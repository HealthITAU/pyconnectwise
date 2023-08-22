from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import AutomateAuthInformation, AutomateTokenResult
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ApitokenEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Apitoken", parent_endpoint=parent_endpoint)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AutomateAuthInformation:
        """
        Performs a GET request against the /Apitoken endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateAuthInformation: The parsed response data.
        """
        return self._parse_one(AutomateAuthInformation, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AutomateTokenResult:
        """
        Performs a POST request against the /Apitoken endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateTokenResult: The parsed response data.
        """
        return self._parse_one(AutomateTokenResult, super()._make_request("POST", data=data, params=params).json())
