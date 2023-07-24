from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate.Automate.Api.Domain.Contracts.Scripts.RunningScripts import RunningScript
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScriptingRunningscriptsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Runningscripts", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[RunningScript]:
        """
        Performs a GET request against the /Scripting/Runningscripts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RunningScript]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            RunningScript,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[RunningScript]:
        """
        Performs a GET request against the /Scripting/Runningscripts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RunningScript]: The parsed response data.
        """
        return self._parse_many(RunningScript, super()._make_request("GET", data=data, params=params).json())
