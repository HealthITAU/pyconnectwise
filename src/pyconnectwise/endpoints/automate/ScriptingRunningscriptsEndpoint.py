from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.automate import AutomateRunningScript
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class ScriptingRunningscriptsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AutomateRunningScript], ConnectWiseAutomateRequestParams],
    IPaginateable[AutomateRunningScript, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Runningscripts", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AutomateRunningScript])
        IPaginateable.__init__(self, AutomateRunningScript)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[AutomateRunningScript]:
        """
        Performs a GET request against the /Scripting/Runningscripts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AutomateRunningScript]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AutomateRunningScript,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[AutomateRunningScript]:
        """
        Performs a GET request against the /Scripting/Runningscripts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AutomateRunningScript]: The parsed response data.
        """
        return self._parse_many(
            AutomateRunningScript,
            super()._make_request("GET", data=data, params=params).json(),
        )
