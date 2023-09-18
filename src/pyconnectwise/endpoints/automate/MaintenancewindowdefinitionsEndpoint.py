from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import AutomateMaintenanceWindowDefinition
from pyconnectwise.responses.paginated_response import PaginatedResponse


class MaintenancewindowdefinitionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Maintenancewindowdefinitions", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[AutomateMaintenanceWindowDefinition]:
        """
        Performs a GET request against the /Maintenancewindowdefinitions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AutomateMaintenanceWindowDefinition]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AutomateMaintenanceWindowDefinition,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[AutomateMaintenanceWindowDefinition]:
        """
        Performs a GET request against the /Maintenancewindowdefinitions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AutomateMaintenanceWindowDefinition]: The parsed response data.
        """
        return self._parse_many(
            AutomateMaintenanceWindowDefinition, super()._make_request("GET", data=data, params=params).json()
        )
