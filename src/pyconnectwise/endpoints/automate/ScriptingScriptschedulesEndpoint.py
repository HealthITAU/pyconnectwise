from typing import Any

from pyconnectwise.endpoints.automate.ScriptingScriptschedulesIdEndpoint import ScriptingScriptschedulesIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import AutomateScheduledScript
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScriptingScriptschedulesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Scriptschedules", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> ScriptingScriptschedulesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScriptingScriptschedulesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScriptingScriptschedulesIdEndpoint: The initialized ScriptingScriptschedulesIdEndpoint object.
        """
        child = ScriptingScriptschedulesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[AutomateScheduledScript]:
        """
        Performs a GET request against the /Scripting/Scriptschedules endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AutomateScheduledScript]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), AutomateScheduledScript, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AutomateScheduledScript]:
        """
        Performs a GET request against the /Scripting/Scriptschedules endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AutomateScheduledScript]: The parsed response data.
        """
        return self._parse_many(AutomateScheduledScript, super()._make_request("GET", data=data, params=params).json())
