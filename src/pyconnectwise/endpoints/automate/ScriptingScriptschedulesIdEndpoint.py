from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import AutomateScheduledScript
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScriptingScriptschedulesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /Scripting/Scriptschedules/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AutomateScheduledScript:
        """
        Performs a PATCH request against the /Scripting/Scriptschedules/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateScheduledScript: The parsed response data.
        """
        return self._parse_one(AutomateScheduledScript, super()._make_request("PATCH", data=data, params=params).json())
